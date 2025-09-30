# Librarian Project Roadmap

*Last updated: December 2024*  
*Target: Meshtastic-focused digital librarian for off-grid knowledge sharing*

## Executive Summary

This roadmap outlines the development path for the Librarian project - a free, open-source, Meshtastic-focused digital librarian that can reply to direct messages and respond to group chat messages that start with "librarian" or are replies to its own posts. The system will run on a Raspberry Pi 5 with local LLM capabilities, providing offline-first knowledge sharing through the Meshtastic LoRa network.

## Project Goals

- **Primary Goal**: Create a self-contained, off-grid Librarian node that can answer questions via Meshtastic DMs and group chat
- **Secondary Goal**: Provide scheduled announcements to group channels
- **Tertiary Goal**: Build a foundation for future features like BBS, MUD, and multi-agent personas

## Architecture Overview

The system consists of several key components:
- **Meshtastic Adapter**: USB serial communication with LoRa radio
- **Message Router**: Classifies incoming messages (DMs, group mentions, announcements)
- **Persistent Queue**: Disk-backed message queue for reliability
- **RAG Service**: Local knowledge base with vector search
- **LLM Client**: Local Ollama integration with Qwen3-4B model
- **Announcement Scheduler**: Timed message broadcasting
- **Operator CLI**: Management and monitoring interface

---

## Phase 1: Foundation & Core Infrastructure (Weeks 1-4)

### 1.1 Project Setup & Structure
- [ ] **1.1.1** Create project directory structure following the specification
- [ ] **1.1.2** Set up Python virtual environment and dependencies
- [ ] **1.1.3** Create basic configuration system (`config.toml`)
- [ ] **1.1.4** Implement logging system with structured JSON output
- [ ] **1.1.5** Create basic CLI framework with argparse
- [ ] **1.1.6** Set up testing framework and initial test structure

### 1.2 Configuration Management
- [ ] **1.2.1** Implement TOML configuration parser
- [ ] **1.2.2** Create secrets management for channel PSKs
- [ ] **1.2.3** Add configuration validation and error handling
- [ ] **1.2.4** Implement configuration reload functionality
- [ ] **1.2.5** Create default configuration templates

### 1.3 Logging & Monitoring
- [ ] **1.3.1** Implement structured JSON logging
- [ ] **1.3.2** Add log rotation (daily or 5MB)
- [ ] **1.3.3** Create log tail functionality for CLI
- [ ] **1.3.4** Add performance metrics collection
- [ ] **1.3.5** Implement error tracking and reporting

### 1.4 Basic RAG Pipeline
- [ ] **1.4.1** Create document ingestion system for project/org history
- [ ] **1.4.2** Implement basic text chunking and preprocessing
- [ ] **1.4.3** Add simple vector embeddings generation
- [ ] **1.4.4** Create basic retrieval system for document search
- [ ] **1.4.5** Implement simple query processing and response generation

---

## Phase 2: Meshtastic Integration (Weeks 5-8)

### 2.1 Meshtastic Adapter Development
- [ ] **2.1.1** Research and implement Meshtastic Python library integration
- [ ] **2.1.2** Create USB serial communication layer
- [ ] **2.1.3** Implement auto-discovery of serial devices
- [ ] **2.1.4** Add connection management and error handling
- [ ] **2.1.5** Create message serialization/deserialization

### 2.2 Message Handling System
- [ ] **2.2.1** Implement message classification (DM, group, admin)
- [ ] **2.2.2** Create message routing logic
- [ ] **2.2.3** Add message filtering and validation
- [ ] **2.2.4** Implement rate limiting and backpressure handling
- [ ] **2.2.5** Create message acknowledgment system

### 2.3 Group Chat Integration
- [ ] **2.3.1** Implement group channel subscription
- [ ] **2.3.2** Add message parsing for "librarian" mentions
- [ ] **2.3.3** Create reply detection for librarian posts
- [ ] **2.3.4** Implement group message broadcasting
- [ ] **2.3.5** Add message threading support

### 2.4 Direct Message System
- [ ] **2.4.1** Implement DM reception and parsing
- [ ] **2.4.2** Create DM response system
- [ ] **2.4.3** Add message queuing for DMs
- [ ] **2.4.4** Implement DM acknowledgment ("Consulting the archives...")
- [ ] **2.4.5** Create DM response formatting

---

## Phase 3: Persistent Queue System (Weeks 9-10)

### 3.1 Queue Implementation
- [ ] **3.1.1** Design disk-backed queue data structure
- [ ] **3.1.2** Implement FIFO queue with JSON records
- [ ] **3.1.3** Add queue persistence across reboots
- [ ] **3.1.4** Create queue monitoring and statistics
- [ ] **3.1.5** Implement queue recovery and repair

### 3.2 Queue Management
- [ ] **3.2.1** Add priority field support (future use)
- [ ] **3.2.2** Implement queue depth monitoring
- [ ] **3.2.3** Create queue inspection CLI commands
- [ ] **3.2.4** Add queue cleanup and maintenance
- [ ] **3.2.5** Implement queue performance metrics

---

## Phase 4: Advanced RAG System Development (Weeks 11-16)

### 4.1 Enhanced Corpus Ingestion
- [ ] **4.1.1** Implement advanced document parsing (PDF, TXT, MD)
- [ ] **4.1.2** Create intelligent text chunking and preprocessing
- [ ] **4.1.3** Add metadata extraction and tagging
- [ ] **4.1.4** Implement corpus indexing system
- [ ] **4.1.5** Create corpus validation and testing

### 4.2 Advanced Vector Database Integration
- [ ] **4.2.1** Integrate ChromaDB or FAISS for embeddings
- [ ] **4.2.2** Implement advanced embedding generation pipeline
- [ ] **4.2.3** Create vector index management
- [ ] **4.2.4** Add embedding model configuration
- [ ] **4.2.5** Implement vector database backup/restore

### 4.3 Retrieval System
- [ ] **4.3.1** Implement k-NN vector search
- [ ] **4.3.2** Add hybrid lexical/vector search
- [ ] **4.3.3** Create re-ranking system
- [ ] **4.3.4** Implement query expansion
- [ ] **4.3.5** Add retrieval quality metrics

### 4.4 RAG Pipeline
- [ ] **4.4.1** Create prompt assembly system
- [ ] **4.4.2** Implement context window management
- [ ] **4.4.3** Add response quality validation
- [ ] **4.4.4** Create RAG performance monitoring
- [ ] **4.4.5** Implement RAG testing framework

---

## Phase 5: LLM Integration (Weeks 17-20)

### 5.1 Ollama Integration
- [ ] **5.1.1** Install and configure Ollama on Pi 5
- [ ] **5.1.2** Download and test Qwen3-4B model
- [ ] **5.1.3** Create Ollama client wrapper
- [ ] **5.1.4** Implement model configuration management
- [ ] **5.1.5** Add model performance monitoring

### 5.2 LLM Client Development
- [ ] **5.2.1** Implement streaming and non-streaming generation
- [ ] **5.2.2** Create prompt template system
- [ ] **5.2.3** Add response formatting and validation
- [ ] **5.2.4** Implement context length management
- [ ] **5.2.5** Create LLM error handling and retry logic

### 5.3 Response Generation
- [ ] **5.3.1** Implement compact response generation
- [ ] **5.3.2** Add message chunking for long responses
- [ ] **5.3.3** Create response quality filtering
- [ ] **5.3.4** Implement response caching
- [ ] **5.3.5** Add response performance metrics

---

## Phase 6: Announcement System (Weeks 21-22)

### 6.1 Schedule Management
- [ ] **6.1.1** Create YAML schedule parser
- [ ] **6.1.2** Implement event template system
- [ ] **6.1.3** Add schedule validation and testing
- [ ] **6.1.4** Create schedule reload functionality
- [ ] **6.1.5** Implement schedule backup/restore

### 6.2 Announcement Scheduler
- [ ] **6.2.1** Implement timed announcement system
- [ ] **6.2.2** Add relative notification support (T-30, T-10, START)
- [ ] **6.2.3** Create announcement de-duplication
- [ ] **6.2.4** Implement urgent broadcast override
- [ ] **6.2.5** Add announcement logging and tracking

### 6.3 Message Templates
- [ ] **6.3.1** Create template system for announcements
- [ ] **6.3.2** Implement variable substitution
- [ ] **6.3.3** Add template validation
- [ ] **6.3.4** Create template testing framework
- [ ] **6.3.5** Implement template customization

---

## Phase 7: Operator CLI (Weeks 23-24)

### 7.1 CLI Framework
- [ ] **7.1.1** Implement comprehensive CLI with subcommands
- [ ] **7.1.2** Add status monitoring commands
- [ ] **7.1.3** Create broadcast functionality
- [ ] **7.1.4** Implement schedule management commands
- [ ] **7.1.5** Add corpus management commands

### 7.2 Monitoring & Diagnostics
- [ ] **7.2.1** Create system status dashboard
- [ ] **7.2.2** Add queue depth monitoring
- [ ] **7.2.3** Implement service health checks
- [ ] **7.2.4** Create performance metrics display
- [ ] **7.2.5** Add error reporting and diagnostics

### 7.3 Management Commands
- [ ] **7.3.1** Implement urgent broadcast override
- [ ] **7.3.2** Add configuration reload
- [ ] **7.3.3** Create corpus re-ingestion
- [ ] **7.3.4** Implement log management
- [ ] **7.3.5** Add system maintenance commands

---

## Phase 8: Integration & Testing (Weeks 25-28)

### 8.1 System Integration
- [ ] **8.1.1** Integrate all components into unified system
- [ ] **8.1.2** Implement service orchestration
- [ ] **8.1.3** Add inter-component communication
- [ ] **8.1.4** Create system startup/shutdown procedures
- [ ] **8.1.5** Implement error recovery and resilience

### 8.2 End-to-End Testing
- [ ] **8.2.1** Create comprehensive test suite
- [ ] **8.2.2** Implement integration tests
- [ ] **8.2.3** Add performance testing
- [ ] **8.2.4** Create load testing scenarios
- [ ] **8.2.5** Implement stress testing

### 8.3 Field Testing
- [ ] **8.3.1** Set up two-radio mesh test environment
- [ ] **8.3.2** Conduct 4-hour continuous operation test
- [ ] **8.3.3** Perform battery life testing (6-8 hours)
- [ ] **8.3.4** Test power-loss recovery
- [ ] **8.3.5** Validate message delivery and response accuracy

---

## Phase 9: Deployment & Operations (Weeks 29-32)

### 9.1 Systemd Integration
- [ ] **9.1.1** Create systemd service files
- [ ] **9.1.2** Implement auto-restart functionality
- [ ] **9.1.3** Add service dependency management
- [ ] **9.1.4** Create service monitoring
- [ ] **9.1.5** Implement graceful shutdown

### 9.2 Installation & Setup
- [ ] **9.2.1** Create installation scripts
- [ ] **9.2.2** Implement dependency management
- [ ] **9.2.3** Add configuration setup automation
- [ ] **9.2.4** Create system requirements validation
- [ ] **9.2.5** Implement one-click deployment

### 9.3 Documentation & Runbooks
- [ ] **9.3.1** Create comprehensive README
- [ ] **9.3.2** Write installation guide
- [ ] **9.3.3** Create operator runbook
- [ ] **9.3.4** Add troubleshooting guide
- [ ] **9.3.5** Create maintenance procedures

---

## Phase 10: Advanced Features (Weeks 33-40)

### 10.1 Enhanced Message Handling
- [ ] **10.1.1** Implement @mention detection in group chat
- [ ] **10.1.2** Add message threading support
- [ ] **10.1.3** Create conversation context tracking
- [ ] **10.1.4** Implement message history
- [ ] **10.1.5** Add conversation analytics

### 10.2 Advanced RAG Features
- [ ] **10.2.1** Implement multi-modal content support
- [ ] **10.2.2** Add semantic search improvements
- [ ] **10.2.3** Create knowledge graph integration
- [ ] **10.2.4** Implement query understanding
- [ ] **10.2.5** Add response personalization

### 10.3 Performance Optimization
- [ ] **10.3.1** Implement response caching
- [ ] **10.3.2** Add query optimization
- [ ] **10.3.3** Create resource usage monitoring
- [ ] **10.3.4** Implement adaptive performance tuning
- [ ] **10.3.5** Add scalability improvements

---

## Phase 11: Future Roadmap Features (Post-MVP)

### 11.1 BBS Layer
- [ ] **11.1.1** Implement public bulletin board system
- [ ] **11.1.2** Create message board management
- [ ] **11.1.3** Add user authentication
- [ ] **11.1.4** Implement message moderation
- [ ] **11.1.5** Create board synchronization

### 11.2 MUD Integration
- [ ] **11.2.1** Implement MUD micro-engine
- [ ] **11.2.2** Create NPC librarian persona
- [ ] **11.2.3** Add interactive commands
- [ ] **11.2.4** Implement game state management
- [ ] **11.2.5** Create multiplayer support

### 11.3 Multi-Agent System
- [ ] **11.3.1** Implement guild-specific personas
- [ ] **11.3.2** Create agent coordination
- [ ] **11.3.3** Add specialized knowledge bases
- [ ] **11.3.4** Implement agent communication
- [ ] **11.3.5** Create agent performance monitoring

### 11.4 Inter-Node Synchronization
- [ ] **11.4.1** Implement LoRa-based sync
- [ ] **11.4.2** Add IPFS integration for content sharing
- [ ] **11.4.3** Create conflict resolution
- [ ] **11.4.4** Implement sync monitoring
- [ ] **11.4.5** Add sync performance optimization

---

## Success Criteria

### MVP Completion Criteria
- [ ] **Installation**: Deployable on fresh Pi 5 in ≤60 minutes
- [ ] **Meshtastic Integration**: Connects to radio, posts 3 timed announcements
- [ ] **DM Handling**: Processes 10 scripted DM queries with ≥90% accuracy
- [ ] **Reliability**: Survives power loss with no message loss
- [ ] **Offline Operation**: Runs ≥6 hours on battery power
- [ ] **CLI Functionality**: All operator commands working

### Performance Targets
- [ ] **Response Time**: Median DM answer time < 3 minutes
- [ ] **Reliability**: ≥95% scheduled announcements sent on time
- [ ] **Accuracy**: ≥90% operator-rated "correct/helpful" responses
- [ ] **Uptime**: Zero data loss across power cycles

### Quality Assurance
- [ ] **Testing**: Comprehensive test suite with unit, integration, and field tests
- [ ] **Documentation**: Complete installation and operation guides
- [ ] **Monitoring**: Full observability with structured logging
- [ ] **Security**: Proper secrets management and sanitization

---

## Risk Mitigation

### Technical Risks
- **LLM Performance**: Test multiple models, implement fallbacks
- **Memory Constraints**: Optimize for Pi 5 limitations, implement caching
- **LoRa Reliability**: Add retry logic, implement message queuing
- **Power Management**: Test battery life, implement graceful degradation

### Operational Risks
- **Deployment Complexity**: Create automated installation scripts
- **Configuration Errors**: Add validation and testing tools
- **Monitoring Gaps**: Implement comprehensive logging and metrics
- **Recovery Procedures**: Create detailed runbooks and testing

---

## Resource Requirements

### Hardware
- Raspberry Pi 5 (16GB RAM)
- Meshtastic LoRa radio (USB)
- SD card or SSD (64GB+)
- Power supply and battery backup
- Optional: Cooling fan, case

### Software Dependencies
- Python 3.9+
- Ollama (ARM build)
- Meshtastic Python library
- ChromaDB or FAISS
- Systemd services
- Standard Linux utilities

### Development Tools
- Git for version control
- Python virtual environment
- Testing frameworks (pytest)
- Code formatting tools
- Documentation generators

---

## Timeline Summary

- **Weeks 1-4**: Foundation & Infrastructure
- **Weeks 5-8**: Meshtastic Integration
- **Weeks 9-10**: Queue System
- **Weeks 11-16**: RAG System
- **Weeks 17-20**: LLM Integration
- **Weeks 21-22**: Announcement System
- **Weeks 23-24**: Operator CLI
- **Weeks 25-28**: Integration & Testing
- **Weeks 29-32**: Deployment & Operations
- **Weeks 33-40**: Advanced Features

**Total Development Time**: ~40 weeks (10 months)

---

## Conclusion

This roadmap provides a comprehensive path from initial development to a fully functional Meshtastic-focused digital librarian. The phased approach ensures steady progress while maintaining quality and reliability. The system will be capable of handling direct messages and group chat interactions as specified, with a strong foundation for future enhancements.

The key to success will be maintaining focus on the core requirements while building a robust, maintainable system that can operate reliably in off-grid environments. Regular testing and validation at each phase will ensure the final system meets all specified requirements and performance targets.
