# Librarian Project Roadmap

## Roadmap Status Legend

- **[ ]** - Not started
- **[?]** - In progress / Testing / Development  
- **[x]** - Completed and tested

**Important**: This roadmap must be kept current. Update checkbox status whenever tasks are started, completed, or when project details change. All changes to the project should be reflected in this roadmap.

---

## Phase 1: Foundation and Core Infrastructure

### 1.1 Project Setup and CLI Framework
- [ ] **1.1.1** Create project structure with separate `meshtastic/` and `api/` applications
- [ ] **1.1.2** Implement structured JSON logging system
- [ ] **1.1.3** Add log rotation and performance metrics
- [ ] **1.1.4** Create testing framework with pytest
- [ ] **1.1.5** Add Makefile for common development tasks
- [ ] **1.1.6** Set up shared code structure in `shared/` directory

### 1.2 Configuration and Secrets Management
- [ ] **1.2.1** Implement TOML-based configuration system
- [ ] **1.2.2** Create secrets management for channel PSKs
- [ ] **1.2.3** Add configuration validation and error handling
- [ ] **1.2.4** Implement secrets file permissions (0600)
- [ ] **1.2.5** Create configuration documentation

### 1.3 Logging and Monitoring
- [ ] **1.3.1** Implement structured JSON logging
- [ ] **1.3.2** Add log rotation (daily or 5MB, 5 backups)
- [ ] **1.3.3** Create log tailing functionality
- [ ] **1.3.4** Add performance metrics collection
- [ ] **1.3.5** Implement system health monitoring

### 1.4 Knowledge Base Setup
- [ ] **1.4.1** Create knowledge directory structure
- [ ] **1.4.2** Implement markdown file organization
- [ ] **1.4.3** Add file metadata and tagging system
- [ ] **1.4.4** Create knowledge base validation
- [ ] **1.4.5** Implement file discovery and indexing

### 1.5 Universal Chat Interface (Multi-Modal Foundation)
- [ ] **1.5.1** Create universal message processor for any source
- [ ] **1.5.2** Implement response router for multiple interfaces
- [ ] **1.5.3** Build universal chat interface coordinator
- [ ] **1.5.4** Add CLI chat interface for testing
- [ ] **1.5.5** Create message/response data structures

---

## Phase 2: REST API Development

### 2.1 REST API Foundation
- [ ] **2.1.1** Design REST API architecture as separate application in `api/` directory
- [ ] **2.1.2** Implement FastAPI/Flask web framework integration
- [ ] **2.1.3** Create API authentication and authorization system
- [ ] **2.1.4** Add API documentation with OpenAPI/Swagger
- [ ] **2.1.5** Implement API versioning and error handling
- [ ] **2.1.6** Create separate systemd service for API application
- [ ] **2.1.7** Set up shared code structure in `shared/` directory

### 2.2 Core API Endpoints
- [ ] **2.2.1** Implement `/chat` endpoint for message processing
- [ ] **2.2.2** Create `/health` endpoint for system status
- [ ] **2.2.3** Add `/stats` endpoint for system statistics
- [ ] **2.2.4** Implement `/admin` endpoints for system management
- [ ] **2.2.5** Create WebSocket support for real-time chat

### 2.3 API Integration
- [ ] **2.3.1** Integrate REST API with universal chat interface
- [ ] **2.3.2** Add API response routing to response router
- [ ] **2.3.3** Implement API rate limiting and security
- [ ] **2.3.4** Add API logging and monitoring
- [ ] **2.3.5** Create API configuration management
- [ ] **2.3.6** Implement inter-process communication between API and Meshtastic services

---

## Phase 3: Comprehensive Test Suite

### 3.1 Test Framework Setup
- [ ] **3.1.1** Create test directory structure (`tests/api/`)
- [ ] **3.1.2** Implement pytest-based test framework
- [ ] **3.1.3** Add test data fixtures and mock services
- [ ] **3.1.4** Create test configuration management
- [ ] **3.1.5** Implement test result logging and reporting

### 3.2 API Test Suite
- [ ] **3.2.1** Create REST API endpoint tests
- [ ] **3.2.2** Implement chat interface integration tests
- [ ] **3.2.3** Add RAG pipeline API tests
- [ ] **3.2.4** Create authentication and authorization tests
- [ ] **3.2.5** Implement API performance and load tests

### 3.3 Feature Test Suite
- [ ] **3.3.1** Create message processing tests for all sources
- [ ] **3.3.2** Implement response routing tests
- [ ] **3.3.3** Add RAG pipeline functionality tests
- [ ] **3.3.4** Create configuration and secrets tests
- [ ] **3.3.5** Implement logging and monitoring tests

### 3.4 Test Automation
- [ ] **3.4.1** Add Makefile `test-all` recipe
- [ ] **3.4.2** Implement continuous integration test pipeline
- [ ] **3.4.3** Create test result reporting and notifications
- [ ] **3.4.4** Add test coverage reporting
- [ ] **3.4.5** Implement automated test execution on changes

### 3.5 Test Requirements for New Features
- [ ] **3.5.1** Define test requirements for all new features
- [ ] **3.5.2** Create test templates for common feature types
- [ ] **3.5.3** Implement test validation in CI/CD pipeline
- [ ] **3.5.4** Add test documentation and guidelines
- [ ] **3.5.5** Create test maintenance and update procedures

### 3.6 Random Seed Control for Testing
- [ ] **3.6.1** Implement random seed configuration for LLM responses
- [ ] **3.6.2** Add seed-based test data generation
- [ ] **3.6.3** Create deterministic test scenarios
- [ ] **3.6.4** Implement seed validation in test framework
- [ ] **3.6.5** Add seed documentation and best practices

---

## Phase 4: Meshtastic Integration

### 4.1 Meshtastic Adapter Development
- [ ] **4.1.1** Implement USB serial communication with LoRa radio
- [ ] **4.1.2** Create message parsing for `#decomp25` channel
- [ ] **4.1.3** Add direct message (DM) endpoint handling
- [ ] **4.1.4** Implement message normalization and formatting
- [ ] **4.1.5** Create Meshtastic connection management

### 4.2 Message Classification
- [ ] **4.2.1** Implement message router for different types
- [ ] **4.2.2** Add DM detection and processing
- [ ] **4.2.3** Create group mention detection ("librarian")
- [ ] **4.2.4** Add reply detection for librarian posts
- [ ] **4.2.5** Implement message threading support

### 4.3 Group Chat Integration
- [ ] **4.3.1** Implement group message broadcasting
- [ ] **4.3.2** Add message parsing for "librarian" mentions
- [ ] **4.3.3** Create reply detection for librarian posts
- [ ] **4.3.4** Implement group message broadcasting
- [ ] **4.3.5** Add message threading support

### 4.4 Direct Message System
- [ ] **4.4.1** Implement DM reception and parsing
- [ ] **4.4.2** Create DM response system
- [ ] **4.4.3** Add message queuing for DMs
- [ ] **4.4.4** Implement DM acknowledgment ("Consulting the archives...")
- [ ] **4.4.5** Create DM response formatting

### 4.5 Meshtastic Node Tracking and Relationship Management
- [ ] **4.5.1** Implement node discovery and logging system
- [ ] **4.5.2** Create interaction history tracking
- [ ] **4.5.3** Add relationship mapping between nodes
- [ ] **4.5.4** Implement vouching system for trust establishment
- [ ] **4.5.5** Create priority assignment based on relationships
- [ ] **4.5.6** Add trust score calculation and propagation
- [ ] **4.5.7** Implement reputation system updates
- [ ] **4.5.8** Create node relationship dashboard

---

## Phase 5: Persistent Queue System

### 5.1 Queue Implementation
- [ ] **5.1.1** Create disk-backed message queue
- [ ] **5.1.2** Implement FIFO queue for DMs
- [ ] **5.1.3** Add priority field for future use
- [ ] **5.1.4** Create queue persistence across reboots
- [ ] **5.1.5** Implement queue monitoring and statistics

### 5.2 Queue Management
- [ ] **5.2.1** Add queue size monitoring
- [ ] **5.2.2** Implement queue overflow handling
- [ ] **5.2.3** Create queue cleanup and maintenance
- [ ] **5.2.4** Add queue performance metrics
- [ ] **5.2.5** Implement queue error handling

---

## Phase 6: RAG System Development

### 6.1 Markdown Knowledge Base
- [ ] **6.1.1** Create knowledge directory structure
- [ ] **6.1.2** Implement markdown file organization
- [ ] **6.1.3** Add file metadata and tagging system
- [ ] **6.1.4** Create knowledge base validation
- [ ] **6.1.5** Implement file discovery and indexing

### 6.2 Shell-Based File Operations (SECURITY CRITICAL)
- [ ] **6.2.1** Implement grep-based text search (knowledge directory only)
- [ ] **6.2.2** Add cat/head/tail for file content access (read-only, sanitized)
- [ ] **6.2.3** Create sed-based text processing (read-only operations only)
- [ ] **6.2.4** Implement file filtering and sorting (knowledge directory only)
- [ ] **6.2.5** Add file operation error handling and security logging
- [ ] **6.2.6** Implement input sanitization and path validation
- [ ] **6.2.7** Create command whitelist and validation system
- [ ] **6.2.8** Add audit logging for all file operations

### 6.3 Direct File Retrieval
- [ ] **6.3.1** Implement file content retrieval
- [ ] **6.3.2** Add context-aware file selection
- [ ] **6.3.3** Create file relevance scoring
- [ ] **6.3.4** Implement file content summarization
- [ ] **6.3.5** Add file operation performance monitoring

### 6.4 RAG Pipeline
- [ ] **6.4.1** Create prompt assembly with file content
- [ ] **6.4.2** Implement context window management
- [ ] **6.4.3** Add response quality validation
- [ ] **6.4.4** Create RAG performance monitoring
- [ ] **6.4.5** Implement RAG testing framework with random seed control

### 6.5 Security Implementation (CRITICAL)
- [ ] **6.5.1** Implement file operation security constraints
- [ ] **6.5.2** Create input sanitization system
- [ ] **6.5.3** Add path validation and directory traversal prevention
- [ ] **6.5.4** Implement command whitelist and validation
- [ ] **6.5.5** Add security audit logging and monitoring
- [ ] **6.5.6** Create security testing framework
- [ ] **6.5.7** Implement penetration testing for file operations
- [ ] **6.5.8** Add security documentation and guidelines

---

## Phase 7: LLM Integration - Model Specifics

### 7.1 Ollama Integration
- [ ] **7.1.1** Install and configure Ollama on Pi 5
- [ ] **7.1.2** Download and test Qwen3-4B-Instruct-Q8 model
- [ ] **7.1.3** Download and test Qwen3-4B-Thinking-Q8 model
- [ ] **7.1.4** Download and test Qwen3-8B-Instruct-Q8 model
- [ ] **7.1.5** Download and test Qwen3-8B-Thinking-Q8 model
- [ ] **7.1.6** Create Ollama client wrapper with model selection
- [ ] **7.1.7** Implement model configuration management
- [ ] **7.1.8** Add model performance monitoring

### 7.2 Agent Spawner System
- [ ] **7.2.1** Implement agent spawner coordinator
- [ ] **7.2.2** Create coordinator/responder agent logic (default: Qwen3-4B/8B-Instruct)
- [ ] **7.2.3** Create researcher agent logic (default: Qwen3-4B/8B-Thinking)
- [ ] **7.2.4** Implement agent spawning and tracking system
- [ ] **7.2.5** Add task delegation and agent coordination
- [ ] **7.2.6** Create agent lifecycle management
- [ ] **7.2.7** Implement agent performance monitoring
- [ ] **7.2.8** Add agent configuration and model selection

### 7.3 Agent Tool System
- [ ] **7.3.1** Implement agent tool interface and registration system
- [ ] **7.3.2** Create file search tool (grep-based) for knowledge base
- [ ] **7.3.3** Create file reading tool (cat/head/tail) for knowledge base
- [ ] **7.3.4** Implement tool security constraints and validation
- [ ] **7.3.5** Add tool result parsing and formatting
- [ ] **7.3.6** Create tool error handling and fallback mechanisms
- [ ] **7.3.7** Implement tool usage logging and monitoring
- [ ] **7.3.8** Add tool configuration and permissions

### 7.4 Agent Workflow Implementation
- [ ] **7.4.1** Implement coordinator/responder agent workflow
- [ ] **7.4.2** Create researcher agent workflow with tool access
- [ ] **7.4.3** Implement researcher adversarial feedback system
- [ ] **7.4.4** Add response confidence scoring
- [ ] **7.4.5** Implement agent spawning logic based on task type/priority/load
- [ ] **7.4.6** Create agent coordination and handoff protocols
- [ ] **7.4.7** Add response assembly and quality filtering
- [ ] **7.4.8** Implement agent performance metrics and monitoring

### 7.5 Load Monitoring and Priority Processing
- [ ] **7.5.1** Implement system load monitoring (CPU, memory, queue depth)
- [ ] **7.5.2** Create priority-based processing system
- [ ] **7.5.3** Add user priority assignment based on relationships
- [ ] **7.5.4** Implement dynamic resource allocation
- [ ] **7.5.5** Create processing level selection logic
- [ ] **7.5.6** Add load-based agent selection
- [ ] **7.5.7** Implement priority queue management
- [ ] **7.5.8** Create load monitoring dashboard

### 7.6 Adversarial Revision System
- [ ] **7.6.1** Implement adversarial revision for high-priority responses
- [ ] **7.6.2** Create multi-round quality improvement
- [ ] **7.6.3** Add consensus-based quality validation
- [ ] **7.6.4** Implement revision tracking and logging
- [ ] **7.6.5** Create quality improvement metrics
- [ ] **7.6.6** Add revision performance monitoring
- [ ] **7.6.7** Implement revision cost-benefit analysis
- [ ] **7.6.8** Create revision quality reporting

---

## Phase 8: Announcement System

### 8.1 Announcement Scheduler
- [ ] **8.1.1** Create announcement scheduling system
- [ ] **8.1.2** Implement timed message broadcasting
- [ ] **8.1.3** Add announcement queue management
- [ ] **8.1.4** Create announcement templates
- [ ] **8.1.5** Implement announcement logging

### 8.2 Announcement Content
- [ ] **8.2.1** Create announcement content templates
- [ ] **8.2.2** Add announcement personalization
- [ ] **8.2.3** Implement announcement formatting
- [ ] **8.2.4** Create announcement validation
- [ ] **8.2.5** Add announcement testing

---

## Phase 9: System Integration and Deployment

### 9.1 System Integration
- [ ] **9.1.1** Integrate all components into unified system
- [ ] **9.1.2** Create system startup and shutdown procedures
- [ ] **9.1.3** Implement system health monitoring
- [ ] **9.1.4** Add system performance optimization
- [ ] **9.1.5** Create system documentation

### 9.2 Deployment Preparation
- [ ] **9.2.1** Create deployment scripts and procedures
- [ ] **9.2.2** Implement systemd service configuration
- [ ] **9.2.3** Add system monitoring and alerting
- [ ] **9.2.4** Create backup and recovery procedures
- [ ] **9.2.5** Add system maintenance procedures

### 9.3 Production Readiness
- [ ] **9.3.1** Implement production configuration
- [ ] **9.3.2** Add production monitoring and logging
- [ ] **9.3.3** Create production testing procedures
- [ ] **9.3.4** Implement production security measures
- [ ] **9.3.5** Add production documentation

---

## Phase 10: Advanced Features

### 10.1 Advanced RAG Features
- [ ] **10.1.1** Implement advanced document processing
- [ ] **10.1.2** Add document summarization capabilities
- [ ] **10.1.3** Create document relationship mapping
- [ ] **10.1.4** Implement document versioning
- [ ] **10.1.5** Add document search optimization

### 10.2 Advanced LLM Features
- [ ] **10.2.1** Implement advanced prompt engineering
- [ ] **10.2.2** Add context-aware response generation
- [ ] **10.2.3** Create response quality assessment
- [ ] **10.2.4** Implement response personalization
- [ ] **10.2.5** Add response learning and adaptation

---

## Phase 11: Multi-Modal Access Interfaces

### 11.1 Web Interface Development
- [ ] **11.1.1** Create local WiFi web interface
- [ ] **11.1.2** Implement mobile-responsive design
- [ ] **11.1.3** Add real-time chat functionality
- [ ] **11.1.4** Create user authentication system
- [ ] **11.1.5** Implement web interface testing

### 11.2 Mobile Interface Development
- [ ] **11.2.1** Create mobile app framework
- [ ] **11.2.2** Implement mobile chat interface
- [ ] **11.2.3** Add mobile-specific features
- [ ] **11.2.4** Create mobile app testing
- [ ] **11.2.5** Implement mobile app deployment

### 11.3 Voice Interface Development
- [ ] **11.3.1** Implement speech-to-text integration
- [ ] **11.3.2** Add text-to-speech capabilities
- [ ] **11.3.3** Create voice command processing
- [ ] **11.3.4** Implement voice interface testing
- [ ] **11.3.5** Add voice interface optimization

### 11.4 API Gateway Development
- [ ] **11.4.1** Create API gateway for all interfaces
- [ ] **11.4.2** Implement API routing and load balancing
- [ ] **11.4.3** Add API security and authentication
- [ ] **11.4.4** Create API monitoring and analytics
- [ ] **11.4.5** Implement API documentation

---

## Phase 12: Community Features

### 12.1 Community Management
- [ ] **12.1.1** Implement community user management
- [ ] **12.1.2** Add community moderation tools
- [ ] **12.1.3** Create community analytics
- [ ] **12.1.4** Implement community feedback system
- [ ] **12.1.5** Add community documentation

### 12.2 Community Integration
- [ ] **12.2.1** Integrate with existing community tools
- [ ] **12.2.2** Add community event integration
- [ ] **12.2.3** Create community knowledge sharing
- [ ] **12.2.4** Implement community collaboration features
- [ ] **12.2.5** Add community support system

---

## Phase 13: Future Enhancements

### 13.1 Advanced AI Features
- [ ] **13.1.1** Implement advanced AI capabilities
- [ ] **13.1.2** Add AI model fine-tuning
- [ ] **13.1.3** Create AI performance optimization
- [ ] **13.1.4** Implement AI learning and adaptation
- [ ] **13.1.5** Add AI research and development

### 13.2 System Optimization
- [ ] **13.2.1** Implement system performance optimization
- [ ] **13.2.2** Add system scalability improvements
- [ ] **13.2.3** Create system reliability enhancements
- [ ] **13.2.4** Implement system security improvements
- [ ] **13.2.5** Add system maintenance automation

### 13.3 Community Expansion
- [ ] **13.3.1** Implement multi-community support
- [ ] **13.3.2** Add community federation
- [ ] **13.3.3** Create community collaboration tools
- [ ] **13.3.4** Implement community knowledge sharing
- [ ] **13.3.5** Add community support and training

---

## Current Status

**Phase 1**: Foundation and Core Infrastructure - **Not Started**
**Phase 2**: REST API Development (Separate Process) - **Not Started**
**Phase 3**: Comprehensive Test Suite - **Not Started**
**Phase 4**: Meshtastic Integration - **Not Started**
**Phase 5**: Persistent Queue System - **Not Started**
**Phase 6**: Simplified RAG System Development - **Not Started**
**Phase 7**: LLM Integration - **Not Started**
**Phase 8**: Announcement System - **Not Started**
**Phase 9**: System Integration and Deployment - **Not Started**
**Phase 10**: Advanced Features - **Not Started**
**Phase 11**: Multi-Modal Access Interfaces - **Not Started**
**Phase 12**: Community Features - **Not Started**
**Phase 13**: Future Enhancements - **Not Started**

---

## Next Steps

1. **Start Phase 2**: REST API Development
2. **Begin Phase 3**: Comprehensive Test Suite
3. **Plan Phase 4**: Meshtastic Integration
4. **Design Phase 5**: Persistent Queue System
5. **Architect Phase 6**: Simplified RAG System

---

## Notes

- All phases are designed to be implemented incrementally
- Each phase builds upon previous phases
- Testing is integrated throughout all phases
- Security considerations are embedded in all phases
- Documentation is maintained throughout development
- The system is designed for offline-first operation
- Multi-modal access is planned for future phases
- Community features are designed for long-term sustainability
- **Agent-based architecture** with specialized models for different tasks
- **Load monitoring and priority-based processing** for intelligent resource allocation
- **Adversarial revision system** for high-quality responses
- **Meshtastic node tracking and relationship management** for community trust
- **Markdown-based RAG system** with direct file access using shell utilities (grep, cat, sed, head, tail)
- **Separate process architecture** with REST API service running independently from Meshtastic service
