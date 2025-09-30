# High Desert Librarian — v1 Project Specification (MVP + Roadmap)

*Last updated: Sep 30, 2025 · Target deployment: Burning Man Decompression 2025 (SF)*
*Primary owner:* High Desert Institute (HDI) · *Guild alignment:* **Lorekeepers** (lead), **Cyberpony Express**, **Flying Robots**

---

## 0) Executive Summary

We’re building a **self-contained, off-grid Librarian** node: a Raspberry Pi 5 (16 GB) connected via USB to its **own Meshtastic LoRa radio**. At Decompression, it will:

* **Post timely announcements** to a Meshtastic group channel (e.g. `decomp25`)
* **Answer DMs** about the schedule and collaborating orgs via a **local RAG** pipeline (no internet)
* Run a **local Ollama** with a small LLM (e.g., **Qwen3-4B**) on solar/battery power
* Embrace **natural delay**: messages are queued; answers arrive when compute is ready (no artificial slowdown)

This MVP is the first concrete “oracle” in the HDI stack. Future versions add **BBS**, **MUD**, **multi-agent guild personas**, **inter-node library sync**, and **local web UI**.

---

## 1) Scope

### In-Scope (MVP)

* One Pi-based Librarian node with:

  * Meshtastic integration (USB)
  * Group announcements to `#decomp25`
  * DM Q&A using a local RAG pipeline
  * Operator CLI for status + manual broadcasts
  * Fully offline operation
  * Durable queue and restart-safe services

### Out-of-Scope (MVP)

* Multi-node sync (LoRa/IPFS)
* BBS/MUD user experiences
* Internet services (cloud LLMs, SaaS dashboards)
* Rich UI beyond Operator CLI

---

## 2) Goals & Success Criteria

**Goals**

* Reliable announcements throughout the event
* Useful, accurate DM answers about schedule/orgs
* Fully offline, solar/battery operation

**Success Metrics**

* ≥95% scheduled announcements sent within their window
* Median DM answer time < 3 min under typical load
* ≥90% operator-rated “correct/helpful” RAG responses on a 20-question test set
* Zero data loss across power cycles (queue + logs)

---

## 3) System Overview

### 3.1 Actors

* **Attendee**: Reads announcements in `#decomp25`; DMs the Librarian
* **Operator**: Starts/stops services, loads schedule, pushes urgent notices
* **Librarian** (service): Receives/sends messages via Meshtastic; runs queue, RAG, LLM

### 3.2 “Natural Delay” Principle

* **No artificial slowdown**. Responses take time due to:

  * Single-board compute limits (Pi 5)
  * Local LLM inference
  * Queue backlog during peaks
* **Interaction philosophy**: Attendees expect reflective pacing; we may send a quick ack (“Consulting the archives…”) so users know their DM was received.

---

## 4) Architecture

### 4.1 Components

1. **Meshtastic Adapter**

   * USB serial to radio; subscribes to `#decomp25` + DM endpoint
   * Normalizes inbound messages; posts outbound messages

2. **Ingress Router**

   * Classifies messages: **ANNOUNCE** (ignore), **DM** (enqueue), **ADMIN** (operator command)
   * Applies channel/identity filters

3. **Persistent Queue**

   * FIFO for DMs (JSON records)
   * Disk-backed (survives reboot); simple priority field reserved (future)

4. **RAG Service**

   * Local corpus (schedule, org docs); markdown-based knowledge base
   * Shell-based file operations (grep, cat, head, tail, sed) for document search and retrieval
   * Direct file access with security constraints and input sanitization

5. **LLM Client** (Ollama)

   * Local **Qwen3-4B** (quantized)
   * Streaming or non-streaming generation

6. **Announcement Scheduler**

   * Reads `schedule.yml`; sends timed messages
   * Supports “T-30, T-10, START” templates + ad-hoc override

7. **Operator CLI**

   * Inspect queue/state/logs
   * Send urgent broadcast; reload configs; rotate logs

8. **Config & Secrets**

   * `config.toml` checked in (non-secret)
   * Channel keys/PSKs stored in root-only file

### 4.2 Data Flow (text diagram)

```
[Meshtastic Radio] ⇄ [Meshtastic Adapter] → [Ingress Router] → [Queue]
                                                       ↓             ↑
                                                 [Operator CLI]      │
                                                       ↓             │
                          [Announcement Scheduler] → [Adapter] ← [Responder Worker]
                                                           ↑         │
                                                     [LLM Client] ← [RAG Service] ← [Shell Tools + Knowledge Base]
```

### 4.3 Directory Layout

```
hdl/
├─ app/
│  ├─ adapter/           # Meshtastic I/O
│  ├─ ingress/           # classify/route inbound
│  ├─ queue/             # disk-backed queue
│  ├─ rag/               # ingest, embed, retrieve
│  ├─ llm/               # ollama client
│  ├─ announce/          # scheduler
│  ├─ responder/         # dequeue + answer DMs
│  ├─ cli/               # operator CLI
│  └─ common/            # config, logging, utils
├─ configs/
│  ├─ config.toml        # non-secret config
│  ├─ channels.secrets   # PSKs/keys (0600)
│  ├─ schedule.yml       # event schedule and templates
│  └─ orgs.yml           # org short blurbs, canonical names
├─ corpus/
│  ├─ docs/              # PDFs, txt, md (input)
│  ├─ processed/         # chunked, cleaned markdown files
│  └─ knowledge/          # organized markdown knowledge base
├─ ops/
│  ├─ systemd/*.service
│  ├─ scripts/*.sh
│  └─ runbook.md
├─ tests/
│  ├─ unit/
│  ├─ integration/
│  └─ fixtures/
└─ README.md
```

---

## 5) Functional Requirements

### 5.1 Meshtastic Integration

* Connect over USB; auto-discover serial port (override in `config.toml`)
* Join a **group channel** (e.g., `decomp25`) with PSK
* Receive:

  * Group messages (ignored unless operator or mention rules later)
  * **DMs to Librarian node** (enqueued)
* Send:

  * Announcements to group
  * DM replies to requestors
* Rate and size aware (LoRa is low-bandwidth; keep messages concise; allow chunking if needed)

### 5.2 Announcements

* Parse `schedule.yml` for events + message templates
* Support relative notifications (e.g., T-30m, T-10m, START)
* Operator CLI can push **urgent** broadcast ignoring schedule
* De-dup guard (don’t repost the same item in case of restart)

### 5.3 DM Q&A (RAG)

* Enqueue DM with metadata: sender, timestamp, text, channel
* Worker loop:

  1. Formulate retrieval query
  2. Search markdown files using shell tools (grep, cat, head, tail)
  3. Compose compact prompt (low-bandwidth output)
  4. Generate answer with Qwen3-4B
  5. Post reply DM; log Q/A pair for eval
* If schedule query detected, prefer structured lookup (exact time/place) before LLM

### 5.4 Natural Delay Handling

* **No artificial sleep**; end-to-end latency depends on queue + inference
* Optional **ack** DM after enqueue (configurable):

  * “📚 Noted. Consulting the archives…”
* No request timeouts; all DMs will be answered eventually
* Backpressure: if queue length > threshold, send a **polite backlog notice** in the ack

### 5.5 Operator CLI

* `hdl status` — services, queue depth, last announce, last error
* `hdl broadcast "msg"` — immediate group message
* `hdl schedule reload` — re-read `schedule.yml`
* `hdl corpus ingest` — (re)organize markdown knowledge base
* `hdl tail` — follow logs
* Exit codes standard Unix semantics

---

## 6) Non-Functional Requirements

* **Offline-first**: no internet required; all assets local
* **Resilience**: survive hard power loss; auto-restart via systemd
* **Observability**: structured logs; rotate daily or 5 MB
* **Resource limits**: cap LLM context/response to fit Pi 5 RAM/CPU/GPU (no GPU assumed)
* **Security**: channel PSKs not in repo; file perms 0600; sanitize outbound text

---

## 7) Configuration Schemas (MVP)

### 7.1 `config.toml`

```toml
[node]
name = "hdl-librarian-01"
serial_device = "/dev/ttyACM0"   # auto-discover fallback
time_zone = "America/Los_Angeles"

[meshtastic]
group_channel = "decomp25"
dm_ack_enabled = true
dm_ack_text = "📚 Noted. Consulting the archives…"
backlog_notice_threshold = 8
backlog_notice_text = "⏳ Many queries in queue; replies may take a bit."

[ollama]
host = "127.0.0.1"
port = 11434
model = "qwen3:4b-instruct-q4"
max_tokens = 256
temperature = 0.3

[rag]
knowledge_path = "./corpus/knowledge"
max_chunk_tokens = 350
search_tools = ["grep", "cat", "head", "tail", "sed"]
security_enabled = true

[announce]
schedule_file = "./configs/schedule.yml"
pre_start_offsets = [30, 10]  # minutes before start
post_start_repeat_minutes = 0 # 0 = no repeat

[logging]
level = "INFO"
dir = "./logs"
```

### 7.2 `channels.secrets` (permissions 0600)

```
# group_channel:psk
decomp25:BASE64_OR_HEX_PSK_VALUE
```

### 7.3 `schedule.yml`

```yaml
meta:
  event_name: "Decompression 2025"
  location: "TBD, San Francisco"
  tz: "America/Los_Angeles"
  default_stage: "Main Stage"

templates:
  pre: "⏰ {title} at {stage} starts in {mins} min. {blurb}"
  start: "🎬 NOW: {title} at {stage}. {blurb}"
  change: "🔁 Update: {title} at {stage} new time {new_time}"

events:
  - id: "act-001"
    title: "Opening Procession"
    stage: "Plaza"
    start: "2025-10-12T17:30:00"
    end:   "2025-10-12T17:50:00"
    blurb: "Kickoff parade. Bring noise!"
  - id: "act-002"
    title: "Fire Performance"
    stage: "Temple Stage"
    start: "2025-10-12T21:30:00"
    end:   "2025-10-12T22:00:00"
    blurb: "Fuel your awe; keep distance."
```

### 7.4 `orgs.yml`

```yaml
orgs:
  - key: "bwb"
    names: ["Burners Without Borders", "BWB"]
    short: "A BM community initiative for civic impact and disaster relief."
  - key: "hdi"
    names: ["High Desert Institute", "HDI"]
    short: "Building resilient off-grid knowledge and community infrastructure."
```

---

## 8) Corpus & RAG Ingestion

### 8.1 Corpus Sources (initial)

* **Schedule** (from `schedule.yml` → organized markdown files)
* **Organizations** capsules (`orgs.yml` + 1-page blurbs in `corpus/docs/orgs/`)
* **Programming details** (e.g., stage maps, policies)
* Preferred formats: `.md`, `.txt`, `.pdf` (extract to text)

### 8.2 Ingestion Pipeline

* Normalize → split into chunks (~300–500 tokens)
* Organize markdown files in `./corpus/knowledge/` directory structure
* Maintain file metadata: `source_path`, `title`, `updated_at`
* Rebuild via `hdl corpus ingest`

### 8.3 Retrieval Strategy

* Primary: shell-based file search using grep for text matching
* Secondary: direct file reading using cat/head/tail for content access
* File filtering and sorting within knowledge directory only
* Security: input sanitization and path validation for all operations

### 8.4 Prompting Guidelines (compact, LoRa-friendly)

**System:**

> You are the High Desert Librarian at Decompression 2025. Answer clearly and concisely for a low-bandwidth radio chat. Prefer exact times/places from the schedule. If unknown, say you don’t know and suggest where to check onsite.

**User template (assembled):**

```
QUESTION: {user_text}
RELEVANT EXCERPTS:
- {passage_1}
- {passage_2}
...
Please answer in ≤4 short lines.
```

---

## 9) Operations

### 9.1 Install Steps (Pi 5)

1. Flash **Raspberry Pi OS (64-bit, Lite)**
2. `sudo apt update && sudo apt install -y python3-pip git jq tmux`
3. Install **Ollama** (ARM build) and `ollama pull qwen3:4b-instruct-q4`
4. `pip install meshtastic python-dotenv uvloop` (or requirements.txt)
5. Clone repo, place `configs/`, `corpus/`
6. Organize knowledge base: `hdl corpus ingest`
7. Test Meshtastic serial connection (see `ops/scripts/meshtastic_probe.sh`)

### 9.2 Services (systemd)

* `hdl-ollama.service` — ensures Ollama running
* `hdl-core.service` — starts adapter, ingress, queue, responder, scheduler
* `hdl-target.service` — aggregate target (Wants=)

*Minimal unit (example):*

```ini
[Unit]
Description=HDL Core
After=network-online.target hdl-ollama.service
Wants=hdl-ollama.service

[Service]
User=pi
WorkingDirectory=/home/pi/hdl
ExecStart=/usr/bin/python3 -m app.cli run-core
Restart=always
RestartSec=2
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

### 9.3 Power & Resilience

* Use SSD over SD if possible; mount with `noatime`
* Enable systemd auto-restart; test hard power pulls
* Keep CPU temps < 80 °C; small fan recommended

### 9.4 Logging

* JSON logs in `./logs/`
* Rotate daily or 5 MB (whichever first)
* `hdl tail` for quick inspection

---

## 10) Message Handling Details

### 10.1 Inbound Classification

* **Group message**: ignore unless operator override or @mention support (future)
* **DM**: enqueue record:

```json
{
  "id":"uuid",
  "from":"mesh_user_id",
  "ts":"2025-10-12T20:15:04Z",
  "text":"when is fire performance?",
  "seen":false,
  "tries":0
}
```

### 10.2 Outbound Behavior

* If `dm_ack_enabled`, send ack immediately
* On answer ready, send concise reply (avoid multi-message where possible)
* If chunking required, include “(1/2) … (2/2)” markers

### 10.3 Backpressure & Errors

* If queue length > threshold, ack includes backlog notice
* If answering fails (LLM error), retry up to N with exponential backoff; on final fail, send apology and log

---

## 11) Security & Privacy

* **Channel PSK** stored in `channels.secrets` (0600)
* Do not echo personal info; DMs are ephemeral, but logs store minimal metadata for QA
* Provide `--anonymize` log export tool for post-event analysis
* Sanitization: strip control chars, limit max output length

---

## 12) Testing Plan

### 12.1 Unit

* Adapter I/O stubs; queue durability; schedule parser; prompt assembly; retry logic

### 12.2 Integration

* End-to-end DM → queue → RAG → LLM → reply with a mock radio
* Schedule triggers fire at T-30/T-10/START with fake clock

### 12.3 Field / Soak

* Two-radio mesh bench test (indoor) for 4 hours continuous
* Battery test: 6–8 hours under expected load (scripted DM cadence)
* Power-loss test: yank power 3×; verify no data loss and services recover

### 12.4 Accuracy/Fit

* 20-question gold set (schedule + orgs) with expected short answers
* Target ≥90% “correct/helpful” on operator review

---

## 13) Event Runbook (Condensed)

**Day -7 to -2**

* Finalize schedule.yml/orgs.yml
* Re-ingest corpus; run QA gold set
* Label node; pack cables, spare SD, fan, PSU

**Day -1**

* Full dress rehearsal: 60-min soak; push test announcement
* Write down serial device path and PSK checksum

**Event Day**

* Set up solar/battery; boot; `hdl status`
* Push “System online” broadcast
* Monitor queue depth; use CLI for urgent changes

**Post-Event**

* Export anonymized logs + Q/A pairs
* Capture incident notes and improvement backlog

---

## 14) Roadmap (Build on MVP)

### Near-Term (1–2 sprints)

* **BBS layer** (public boards) riding Meshtastic
* **MUD micro-engine** (commands, NPC librarian persona)
* **Multi-agent personas** per guild (Lorekeeper, Courier, Farmer)
* **Local web UI** (LAN only) with status + docs (static)

### Mid-Term

* **Inter-node sync** (LoRa opportunistic, IPFS when possible)
* **Content packs** (zip of corpus + markdown files for drop-in updates)
* **Priority queues** (urgent vs normal DM; operator priority)
* **Hybrid retrieval** (fuzzy name resolution, schedule macros)

### Long-Term

* **Deployed librarians** at HDI outposts (High Ground, Sky Spring)
* **Federated oracles**: mesh of librarians sharing curated knowledge
* **Richer modalities**: maps, ASCII diagrams, QR fallbacks to local LAN content
* **Hardware variants**: drone/rover-mounted courier nodes (Flying Robots)

---

## 15) Acceptance Criteria (MVP “Done”)

* [ ] Installable on a fresh Pi 5 via README in ≤60 minutes
* [ ] Connects to Meshtastic, posts **3 timed announcements** on schedule
* [ ] Handles **10 scripted DM queries** with ≥90% correct/helpful rating
* [ ] Survives a power yank with no lost queued messages
* [ ] Operable entirely offline for ≥6 hours on battery
* [ ] Operator CLI covers status, broadcast, schedule reload, ingest, tail

---

## 16) Implementation Notes & Tips

* **Model choice**: start with `qwen3:4b-instruct-q4` (small context, low temp). If latency is too high, consider even smaller variants or aggressive chunking and top-k=4.
* **Responses**: prefer direct facts (“9:30 pm at Temple Stage”) in ≤4 lines.
* **Schedule fast-path**
