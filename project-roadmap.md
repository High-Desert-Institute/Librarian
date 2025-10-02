# Librarian Project Roadmap - Simplified Architecture

## Roadmap Status Legend

- **[ ]** - Not started
- **[?]** - In progress / Testing / Development  
- **[x]** - Completed and tested

**Important**: This roadmap reflects the radically simplified two-script architecture. Update checkbox status whenever tasks are started, completed, or when project details change.

---

## Phase 1: Core Two-Script Implementation

### 1.1 Message Monitor Script (`message_monitor.py`)
- [ ] **1.1.1** Create message monitoring script with Meshtastic integration
- [ ] **1.1.2** Implement CSV file creation for each chat (DM/group) with hardware ID directories
- [ ] **1.1.3** Add message logging with full metadata (sender, timestamp, content, etc.)
- [ ] **1.1.4** Add simulation mode for testing without radio
- [ ] **1.1.5** Create structured logging system

### 1.2 Response Generator Script (`response_generator.py`)
- [ ] **1.2.1** Create response generation script with CSV monitoring
- [ ] **1.2.2** Implement detection of DMs and "librarian" mentions in group chats
- [ ] **1.2.3** Add conversation context building from previous messages
- [ ] **1.2.4** Add simulation mode for testing without Ollama

### 1.3 CSV Message Storage System
- [ ] **1.3.1** Design CSV structure with required columns
- [ ] **1.3.2** Implement separate CSV files for each chat (subset of 1.1.2)
- [ ] **1.3.3** Create CSV file management and organization
- [ ] **1.3.4** Add CSV file validation and error handling

### 1.4 Integration and Testing
- [ ] **1.4.1** Test both scripts running simultaneously
- [ ] **1.4.2** Verify CSV file creation and message logging
- [ ] **1.4.3** Test message detection and context building
- [ ] **1.4.4** Add error handling and recovery mechanisms
- [ ] **1.4.5** Create comprehensive logging for debugging

---

## Phase 2: Chatbot Integration and Message Sending

### 2.1 Chatbot Integration
- [ ] **2.1.1** Integrate Ollama chatbot for response generation
- [ ] **2.1.2** Implement response queuing system
- [ ] **2.1.3** Add message state management (incoming, queued, outgoing, sent)
- [ ] **2.1.4** Create chatbot configuration and model selection
- [ ] **2.1.5** Add chatbot error handling and fallback responses

### 2.2 Message Sending Implementation
- [ ] **2.2.1** Add message sending capability to message monitor script
- [ ] **2.2.2** Implement queued message processing and sending
- [ ] **2.2.3** Add state transitions (queued → outgoing → sent)
- [ ] **2.2.4** Implement retry logic for failed message sends
- [ ] **2.2.5** Add message sending error handling and logging


---

## Phase 3: Testing and Validation

### 3.1 System Integration Testing
- [ ] **3.1.1** Test complete message flow (incoming → response → sending)
- [ ] **3.1.2** Verify state transitions work correctly
- [ ] **3.1.3** Add system health monitoring and status reporting
- [ ] **3.1.4** Implement graceful shutdown and restart procedures
- [ ] **3.1.5** Create system monitoring and alerting

### 3.2 Simulation Testing
- [ ] **3.2.1** Test message monitor simulation mode
- [ ] **3.2.2** Test response generator simulation mode
- [ ] **3.2.3** Create comprehensive test scenarios with mock data
- [ ] **3.2.4** Test CSV file creation and message logging
- [ ] **3.2.5** Test response generation and queuing

### 3.3 Hardware Testing
- [ ] **3.3.1** Test with actual Meshtastic radio
- [ ] **3.3.2** Test Ollama integration and response generation
- [ ] **3.3.3** Test message sending through radio
- [ ] **3.3.4** Test system performance under load
- [ ] **3.3.5** Test battery operation and power management

### 3.4 Validation and Quality Assurance
- [ ] **3.4.1** Create test data sets for response quality validation
- [ ] **3.4.2** Test response accuracy and helpfulness
- [ ] **3.4.3** Validate CSV file integrity and data consistency
- [ ] **3.4.4** Test logging completeness and accuracy
- [ ] **3.4.5** Create performance benchmarks and metrics

---

## Phase 4: Deployment and Operations

### 4.1 Production Deployment
- [ ] **4.1.1** Create deployment scripts for Raspberry Pi 5
- [ ] **4.1.2** Implement systemd service files for both scripts
- [ ] **4.1.3** Add automatic startup and restart configuration
- [ ] **4.1.4** Create installation and setup documentation
- [ ] **4.1.5** Test deployment on fresh Pi 5 system

### 4.2 Monitoring and Maintenance
- [ ] **4.2.1** Implement system health monitoring
- [ ] **4.2.2** Add log rotation and cleanup procedures
- [ ] **4.2.3** Create performance monitoring and alerting
- [ ] **4.2.4** Add backup and recovery procedures
- [ ] **4.2.5** Create maintenance and troubleshooting guides

### 4.3 Event Operations
- [ ] **4.3.1** Test system at Burning Man Decompression 2025
- [ ] **4.3.2** Monitor performance under real-world conditions
- [ ] **4.3.3** Collect feedback and usage data
- [ ] **4.3.4** Document lessons learned and improvements
- [ ] **4.3.5** Plan future enhancements based on experience

---

## Phase 5: Future Enhancements (Optional)

### 5.1 Markdown-Based RAG System
- [ ] **5.1.1** Create knowledge base directory structure for markdown files
- [ ] **5.1.2** Implement markdown file organization and indexing
- [ ] **5.1.3** Add shell-based file search (grep, cat, head, tail) for knowledge retrieval
- [ ] **5.1.4** Implement context-aware file selection and relevance scoring
- [ ] **5.1.5** Create RAG pipeline integration with response generator
- [ ] **5.1.6** Add knowledge base validation and maintenance tools
- [ ] **5.1.7** Implement security constraints for file operations (no databases)

### 5.2 Advanced Features
- [ ] **5.2.1** Implement message scheduling and announcements
- [ ] **5.2.2** Add web interface for monitoring and management
- [ ] **5.2.3** Create mobile app for remote monitoring
- [ ] **5.2.4** Add voice interface capabilities

### 5.3 System Optimization
- [ ] **5.3.1** Implement performance optimization
- [ ] **5.3.2** Add advanced error handling and recovery
- [ ] **5.3.3** Create system monitoring and alerting
- [ ] **5.3.4** Add backup and synchronization features
- [ ] **5.3.5** Implement security enhancements

### 5.4 Community Features
- [ ] **5.4.1** Add multi-node synchronization
- [ ] **5.4.2** Implement community knowledge sharing
- [ ] **5.4.3** Create user management and permissions
- [ ] **5.4.4** Add community analytics and reporting
- [ ] **5.4.5** Implement community collaboration tools

---

## Current Status

**Phase 1**: Core Two-Script Implementation - **Not Started**
**Phase 2**: Message Sending and State Management - **Not Started**
**Phase 3**: Testing and Validation - **Not Started**
**Phase 4**: Deployment and Operations - **Not Started**
**Phase 5**: Future Enhancements (Optional) - **Not Started**

---

## Next Steps

1. **Start Phase 1**: Core Two-Script Implementation
   - Create `message_monitor.py` script
   - Create `response_generator.py` script
   - Implement CSV message storage system
   - Test both scripts in simulation mode

2. **Begin Phase 2**: Message Sending and State Management
   - Add message sending capability
   - Implement complete state lifecycle
   - Test end-to-end message flow

3. **Plan Phase 3**: Testing and Validation
   - Test with actual hardware
   - Validate response quality
   - Performance testing

---

## Notes

- **Simplified Architecture**: Just two Python scripts working through CSV files
- **Maximum Transparency**: All messages logged to CSV files for easy inspection
- **Easy Debugging**: CSV files provide complete audit trail
- **Simulation Modes**: Both scripts can run without hardware for testing
- **Offline-First**: Designed for off-grid operation
- **Extensible**: Easy to add new features or modify behavior
- **Community-Focused**: Built for Burning Man Decompression 2025 deployment
