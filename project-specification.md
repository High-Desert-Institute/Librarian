# High Desert Librarian — v1 Project Specification (Simplified Architecture)

*Last updated: December 2024 · Target deployment: Burning Man Decompression 2025 (SF)*
*Primary owner:* High Desert Institute (HDI) · *Guild alignment:* **Lorekeepers** (lead), **Cyberpony Express**, **Flying Robots**

---

## 0) Executive Summary

We're building a **radically simplified Librarian** node: a Raspberry Pi 5 (16 GB) connected via USB to its **own Meshtastic LoRa radio**. The system consists of just **two Python scripts** that work together through CSV message files.

**Script 1: `message_monitor.py`** - Monitors the radio and logs all messages to CSV files  
**Script 2: `response_generator.py`** - Monitors CSV files and generates responses for librarian mentions

At Decompression, it will:
* **Log all messages** to CSV files with full metadata (sender, timestamp, content, etc.)
* **Answer DMs** and group messages starting with "librarian" via local chatbot
* **Queue responses** for future sending back through the radio
* Embrace **natural delay**: responses are generated when compute is ready

This simplified MVP focuses on core functionality with maximum transparency and debuggability.

---

## 1) Scope

### In-Scope (Simplified MVP)

* Two Python scripts with:

  * **Message Monitor**: Meshtastic integration (USB) + CSV logging
  * **Response Generator**: CSV monitoring + chatbot responses
  * CSV-based message storage with full metadata
  * DM Q&A and group message responses
  * Local chatbot integration (Ollama)
  * Fully offline operation
  * Simulation modes for testing

### Out-of-Scope (Simplified MVP)

* Complex multi-phase development
* Advanced RAG systems
* Multi-node sync (LoRa/IPFS)
* BBS/MUD user experiences
* Internet services (cloud LLMs, SaaS dashboards)
* Rich UI beyond CSV files
* Complex configuration systems

---

## 2) Goals & Success Criteria

**Goals**

* Reliable message logging to CSV files
* Useful, accurate responses to DMs and librarian mentions
* Fully offline, solar/battery operation
* Maximum transparency and debuggability

**Success Metrics**

* ≥95% of messages logged to CSV files with complete metadata
* Median response generation time < 3 min under typical load
* ≥90% operator-rated "correct/helpful" responses on a 20-question test set
* Zero data loss across power cycles (CSV files + logs)
* Both scripts run in simulation mode for testing
* Deployable on fresh Pi 5 in ≤60 minutes
* 6+ hours battery operation
* Complete offline functionality

---

## 3) System Overview

### 3.1 Actors

* **Attendee**: Sends DMs to Librarian; mentions "librarian" in group chats
* **Operator**: Starts/stops scripts, monitors CSV files, checks logs
* **Message Monitor**: Receives messages via Meshtastic; logs to CSV files
* **Response Generator**: Monitors CSV files; generates responses via chatbot

### 3.2 "Natural Delay" Principle

* **No artificial slowdown**. Responses take time due to:

  * Single-board compute limits (Pi 5)
  * Local LLM inference
  * CSV file processing delays
* **Interaction philosophy**: Attendees expect reflective pacing; responses are queued and sent when ready.

---

## 4) Architecture

### 4.1 Components

1. **Message Monitor Script** (`message_monitor.py`)

   * USB serial connection to Meshtastic radio
   * Logs all messages to CSV files with full metadata
   * Creates separate CSV files for each chat (DM or group)
   * Handles message state: `incoming`, `queued`, `outgoing`, `sent`

2. **Response Generator Script** (`response_generator.py`)

   * Monitors CSV files for messages needing responses
   * Detects DMs and group messages starting with "librarian"
   * Builds conversation context from previous messages
   * Generates responses using local chatbot (Ollama)
   * Queues responses for future sending

3. **CSV Message Storage**

   * Each radio gets its own directory: `messages/{hardware_id}/`
   * Each chat gets its own CSV file within the radio directory
   * Columns: `state`, `timestamp`, `sender`, `message`, `message_id`, `chat_type`, `chat_id`
   * Provides complete audit trail of all messages
   * Supports multiple radios on the same system

4. **Local Chatbot Integration**

   * Ollama integration with Qwen3-4B model
   * Fallback simulation mode for testing
   * Context-aware response generation

5. **Logging System**

   * Structured logging for both scripts
   * Console and file output for monitoring
   * Simulation modes for testing without hardware

### 4.2 Data Flow (text diagram)

```
[Meshtastic Radio] → [Message Monitor] → [CSV Files] → [Response Generator] → [Queued Responses]
                                                              ↑                        ↓
                                                      [Chatbot/Ollama] ← [Context Building]
```

### 4.3 Directory Layout

```
librarian/
├─ message_monitor.py     # Message monitoring script
├─ response_generator.py  # Response generation script
├─ requirements.txt       # Python dependencies
├─ messages/              # CSV files organized by radio hardware ID
│  ├─ radio_001/         # Radio hardware ID directory
│  │  ├─ dm_user123.csv  # Direct message chat
│  │  ├─ group_decomp25.csv # Group chat
│  │  └─ ...
│  ├─ radio_002/         # Second radio hardware ID
│  │  ├─ dm_user456.csv
│  │  └─ ...
│  └─ ...
├─ logs/                  # Log files
│  ├─ message_monitor.log
│  └─ response_generator.log
├─ README.md              # Project documentation
```

---

## 5) Functional Requirements

### 5.1 Message Monitor Script

* Connect over USB; auto-discover serial port
* Join group channels and receive DMs
* Log all messages to CSV files with full metadata
* Support simulation mode for testing without radio
* Provide CLI commands: `--test`, `--status`

### 5.2 Response Generator Script

* Monitor CSV files for messages needing responses
* Detect DMs and group messages starting with "librarian"
* Build conversation context from previous messages
* Generate responses using local chatbot (Ollama)
* Queue responses for future sending
* Support simulation mode for testing without Ollama
* Provide CLI commands: `--test`, `--status`

### 5.3 CSV Message Storage

* Each radio gets its own directory: `messages/{hardware_id}/`
* Each chat gets its own CSV file within the radio directory
* Columns: `state`, `timestamp`, `sender`, `message`, `message_id`, `chat_type`, `chat_id`
* Complete audit trail of all messages and responses

### 5.4 Natural Delay Handling

* **No artificial sleep**; responses take time due to compute limitations
* Responses are queued and sent when ready
* All operations logged for complete transparency

---

## 6) Non-Functional Requirements

* **Offline-first**: no internet required; all assets local
* **Resilience**: survive hard power loss; auto-restart via systemd
* **Observability**: structured logs; rotate daily or 5 MB
* **Resource limits**: cap LLM context/response to fit Pi 5 RAM/CPU/GPU (no GPU assumed)
* **Security**: channel PSKs not in repo; file perms 0600; sanitize outbound text
* **CLI-first**: all operations executable from command line
* **Test mode**: simulation mode for testing without hardware

---

## 7) Installation and Operations

### 7.1 Install Steps (Pi 5)

1. Flash **Raspberry Pi OS (64-bit, Lite)**
2. `sudo apt update && sudo apt install -y python3-pip git jq tmux`
3. Install **Ollama** (ARM build) and `ollama pull qwen3:4b-instruct-q4`
4. `pip install -r requirements.txt`
5. Clone repository
6. Test Meshtastic serial connection

### 7.2 Services (systemd)

* `librarian-message-monitor.service` — starts message monitor script
* `librarian-response-generator.service` — starts response generator script
* `librarian-ollama.service` — ensures Ollama running

### 7.3 Logging

* Structured logs in `./logs/`
* Rotate daily or 5 MB (whichever first)
* Console output for real-time monitoring

---

## 8) Testing Plan

### 8.1 Simulation Testing

* Test both scripts in simulation mode
* Verify CSV file creation and message logging
* Test response generation and queuing

### 8.2 Hardware Testing

* Test with actual Meshtastic radio
* Test Ollama integration and response generation
* Test message sending through radio
* Test system performance under load

### 8.3 Validation and Quality Assurance

* Create test data sets for response quality validation
* Test response accuracy and helpfulness
* Validate CSV file integrity and data consistency
* Test logging completeness and accuracy

---

## 9) Acceptance Criteria (MVP "Done")

* [ ] Installable on a fresh Pi 5 via README in ≤60 minutes
* [ ] Both scripts run in simulation mode for testing
* [ ] Handles **10 scripted DM queries** with ≥90% correct/helpful rating
* [ ] Survives a power yank with no lost queued messages
* [ ] Operable entirely offline for ≥6 hours on battery
* [ ] CLI commands work for all operations
