# Librarian

A free, open-source, Meshtastic-focused, digital librarian to help you find what you need and answer complex questions.

## Development Styleguides

Before contributing, please read the relevant styleguide files in `styleguides/`:

- **`styleguides/README.md`** - Styleguide overview
- **`styleguides/cli-development.md`** - CLI logging and interpretability guidelines
- **`styleguides/python-cli-development.md`** - Python-specific CLI development practices
- **`styleguides/java-cli-development.md`** - Java-specific CLI development practices

Then follow the application-specific requirements found in `project-specification.md`.

## Project Overview

The Librarian is a self-contained, off-grid digital assistant designed to operate on a Raspberry Pi 5 with local LLM capabilities. It provides knowledge sharing through the Meshtastic LoRa network, enabling communities to access information and ask questions even when disconnected from the internet.

### Key Features

- **Direct Message Q&A**: Responds to private messages with answers from a local knowledge base
- **Group Chat Integration**: Monitors group channels for messages starting with "librarian" or replies to its own posts
- **Scheduled Announcements**: Automatically posts timed announcements to group channels
- **Offline Operation**: Fully functional without internet connectivity
- **Local RAG System**: Retrieval-Augmented Generation using local markdown documents and shell-based search
- **Natural Delay Philosophy**: Responses take time due to compute limitations, creating a reflective interaction style

## Repository Structure

```
Librarian/
├── AGENTS.md                    # Redirects to README.md for agent orientation
├── project-specification.md     # Detailed technical specification and requirements
├── project-roadmap.md          # Comprehensive development roadmap
├── social-context.md           # Social context, partnerships, and community impact
├── README.md                   # This file - project overview and current status
├── meshtastic/                  # Meshtastic service application
├── api/                         # REST API service application
├── shared/                      # Shared code between applications
├── configs/                     # Configuration files
├── corpus/                      # Knowledge base (markdown files)
├── ops/                         # Operations and deployment
├── tests/                       # Test suites
└── styleguides/                 # Development style guides
    ├── README.md               # Styleguide overview
    ├── cli-development.md      # CLI logging and interpretability guidelines
    ├── java-cli-development.md # Java-specific CLI development practices
    └── python-cli-development.md # Python-specific CLI development practices
```


## Current Project Status

### Development Phase: **Planning & Foundation**

The project is currently in the initial planning phase. The comprehensive roadmap has been created and outlines the development phases.

### Completed Tasks
- [x] Project specification and requirements analysis
- [x] Comprehensive roadmap creation (`project-roadmap.md`)
- [x] Development styleguide documentation
- [x] Repository structure setup

### Next Steps (Phase 1: Foundation & Core Infrastructure)

The immediate next steps include:

1. **Project Setup and CLI Framework** (Phase 1.1)
   - Create project structure and basic CLI framework
   - Implement structured JSON logging system
   - Add log rotation and performance metrics
   - Create testing framework with pytest
   - Add Makefile for common development tasks

2. **Configuration and Secrets Management** (Phase 1.2)
   - Implement TOML-based configuration system
   - Create secrets management for channel PSKs
   - Add configuration validation and error handling
   - Implement secrets file permissions (0600)
   - Create configuration documentation

## Project Roadmap

The complete development plan is detailed in [`project-roadmap.md`](project-roadmap.md), which includes:

### 11 Development Phases
1. **Foundation & Core Infrastructure**
2. **Meshtastic Integration**
3. **Persistent Queue System**
4. **Advanced RAG System Development**
5. **LLM Integration**
6. **Announcement System**
7. **Operator CLI**
8. **Integration & Testing**
9. **Deployment & Operations**
10. **Advanced Features**
11. **Future Roadmap Features** (Post-MVP)

### Success Criteria
- Deployable on fresh Pi 5 in ≤60 minutes
- ≥90% accuracy on DM responses
- ≥95% reliability for scheduled announcements
- 6+ hours battery operation
- Complete offline functionality

## Technical Architecture

The system consists of several key components:

- **Meshtastic Adapter**: USB serial communication with LoRa radio
- **Message Router**: Classifies incoming messages (DMs, group mentions, announcements)
- **Persistent Queue**: Disk-backed message queue for reliability
- **RAG Service**: Local markdown knowledge base with shell-based file search
- **LLM Client**: Local Ollama integration with Qwen3-4B model
- **REST API Service**: HTTP API for chat processing and system management (separate process)
- **Announcement Scheduler**: Timed message broadcasting
- **Operator CLI**: Management and monitoring interface

## Getting Started

### Prerequisites
- Raspberry Pi 5 (16GB RAM recommended)
- Meshtastic LoRa radio (USB connection)
- Python 3.9+
- Ollama (ARM build)
- Standard Linux utilities

### Installation (Future)
Once development is complete, installation will be:
1. Flash Raspberry Pi OS (64-bit, Lite)
2. Install dependencies via automated script
3. Clone repository and configure
4. Run `hdl corpus ingest` to build knowledge base
5. Start services with `hdl run-core`

## Contributing

Before contributing, please read the styleguides listed at the top of this README and the detailed technical requirements in `project-specification.md`.

### Documentation Maintenance

**CRITICAL**: Always update this `README.md` file whenever:
- Project details or structure change
- Progress is made on the roadmap
- New features are added or completed
- Repository structure is modified
- Development status changes

This `README.md` serves as the primary human-readable documentation and must remain current with all project changes. It should include:
- Current project status and phase
- Recent progress and completed tasks
- Updated repository structure
- Current roadmap position
- Any changes to development approach or requirements

### Development Workflow
1. Follow CLI-first development practices
2. Implement comprehensive logging
3. Create test mode functionality
4. Update README.md with any changes
5. Follow the roadmap for feature development

## Documentation

- **`project-specification.md`**: Complete technical specification
- **`project-roadmap.md`**: Detailed development timeline
- **`social-context.md`**: Social context, partnerships, and community impact
- **`styleguides/`**: Development best practices

## License

This project is free and open-source. See the project specification for licensing details.

## Contact

For questions about the project, please refer to the project specification and roadmap documents. The project follows a structured development approach with clear phases and milestones.

---

*Last updated: December 2024*
*Current phase: Planning & Foundation*
*Next milestone: Phase 1.1 - Project Setup and CLI Framework*