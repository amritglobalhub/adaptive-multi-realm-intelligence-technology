# 🔮 AMRIT AI - Adaptive Multi-Realm Intelligence Technology

A self-learning personal intelligence system with multi-modal biometric authentication, autonomous learning capabilities, and personalized UI generation.

## 🌟 Features

### 1. **Autonomous Learning System**
- ✅ Self-learning from every interaction without explicit training
- ✅ Adaptive behavior based on user patterns
- ✅ Linguistic pattern capture and analysis
- ✅ Preference analysis and prediction
- ✅ Behavior prediction development

### 2. **Permission-Gated Operations**
- ✅ Voice/explicit permission required for major actions
- ✅ Explicit consent logging for all operations
- ✅ Auto-learning only with user consent
- ✅ Data modification requires approval
- ✅ Policy updates require confirmation

### 3. **Hidden Data Architecture**
- ✅ Encrypted hidden directory structure
- ✅ Multi-layer AES-256 encryption
- ✅ Obfuscated file names
- ✅ SQLCipher encrypted database support
- ✅ Zero traces in system cache

### 4. **Owner Recognition & Identification**
- ✅ Voice print analysis system
- ✅ Speech pattern recognition
- ✅ Behavioral signature matching
- ✅ Multi-modal biometric verification
- ✅ Spoofing detection
- ✅ Real-time confidence scoring

### 5. **Data Mining for Personalization**
- ✅ Command preference extraction
- ✅ Response preference analysis
- ✅ Time pattern detection
- ✅ Context understanding
- ✅ Communication style analysis
- ✅ Decision-making pattern tracking
- ✅ Emotional undertone detection

### 6. **Personalized UI Generation**
- ✅ Auto-design based on preferences
- ✅ Logo/branding concept generation
- ✅ Custom command builder
- ✅ Personalized dashboard generation
- ✅ Adaptive theme colors

## 📁 Project Structure

```
adaptive-multi-realm-intelligence-technology/
├── config.py                    # System configuration
├── encryption.py                # Multi-layer encryption system
├── hidden_storage.py            # Encrypted hidden storage manager
├── permission_manager.py        # Permission and consent system
├── owner_recognition.py         # Multi-modal biometric verification
├── self_learning.py             # Autonomous learning engine
├── data_mining.py              # Data mining and pattern extraction
├── ui_personalization.py       # Personalized UI generator
├── amrit_system.py             # Main system orchestrator
├── requirements.txt            # Python dependencies
└── amrit_hidden_space/         # Hidden encrypted storage (auto-created)
    ├── personal_biometrics/
    ├── behavior_profiles/
    ├── recognition_engine/
    ├── learning_logs/
    └── system_intelligence/
```

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Setup Steps

1. **Clone the repository:**
```bash
git clone https://github.com/amritglobalhub/adaptive-multi-realm-intelligence-technology.git
cd adaptive-multi-realm-intelligence-technology
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables (optional):**
```bash
# Create .env file
echo "AMRIT_API_HOST=127.0.0.1" > .env
echo "AMRIT_API_PORT=8000" >> .env
echo "AMRIT_LOG_LEVEL=INFO" >> .env
```

## 💻 Usage

### Basic Usage

```python
from amrit_system import AMRITSystem
import numpy as np

# Initialize system with master password
system = AMRITSystem("your_secure_password")

# Enroll owner (first-time setup)
audio_samples = [...]  # List of voice samples
text_samples = ["Hello AMRIT", "This is my voice"]
behavioral_samples = [{'timestamp': '...', 'duration': 10}]

system.enroll_owner(audio_samples, text_samples, behavioral_samples)

# Authenticate owner
audio = np.array([...])  # Voice sample
authenticated = system.authenticate_owner(audio_data=audio, text="Hello")

if authenticated:
    # Record interactions for learning
    system.record_interaction('command', {
        'command': 'process_data',
        'context': {'mode': 'active'},
        'success': True
    })
    
    # Request permission for operation
    request_id = system.request_permission(
        PermissionType.DATA_MODIFICATION,
        "Need to update user preferences"
    )
    
    # Grant permission
    system.grant_permission(request_id)
    
    # Run data analysis
    insights = system.run_data_analysis()
    
    # Generate personalized UI
    ui_config = system.generate_personalized_ui()
    
    # Get system status
    system.print_status()
    
    # End session
    system.end_session()
```

### Running the Demo

```bash
python amrit_system.py
```

Follow the prompts to:
1. Set master password
2. Enroll as owner (first-time)
3. Authenticate
4. See system in action

## 🔐 Security Features

### Encryption
- **AES-256** encryption for all stored data
- **PBKDF2** key derivation with 100,000 iterations
- **Multi-layer encryption** support
- **Secure file deletion** with random data overwrite

### Hidden Storage
- Invisible to normal file system operations
- Obfuscated filenames using SHA-256 hashing
- Restrictive file permissions (0600 on Unix)
- Encrypted metadata alongside data

### Authentication
- Multi-modal biometric verification
- Failed attempt tracking and lockout
- Confidence scoring system
- Spoofing detection

### Privacy
- No external telemetry
- Anonymized logs
- Cache clearing on exit
- Secure wipe functionality

## 🧠 Learning Capabilities

### Pattern Recognition
- Command usage patterns
- Query preferences
- Linguistic style analysis
- Temporal usage patterns
- Context understanding

### Preference Learning
- Response style preferences
- Communication preferences
- Decision-making patterns
- Emotional patterns
- Time-of-day preferences

### Adaptive Behavior
- Predictive action suggestions
- Personalized responses
- Custom command generation
- UI adaptation

## 📊 API Reference

### Core Classes

#### `AMRITSystem`
Main system orchestrator.

**Methods:**
- `__init__(master_password: str)` - Initialize system
- `authenticate_owner(...)` - Authenticate user
- `enroll_owner(...)` - Enroll new owner
- `record_interaction(...)` - Record interaction for learning
- `request_permission(...)` - Request operation permission
- `grant_permission(...)` - Grant permission
- `get_system_status()` - Get comprehensive status
- `end_session()` - End current session

#### `HiddenStorageManager`
Manages encrypted hidden storage.

**Methods:**
- `initialize()` - Create hidden directory structure
- `store_data(category, key, data)` - Store encrypted data
- `retrieve_data(category, key)` - Retrieve decrypted data
- `delete_data(category, key)` - Securely delete data
- `secure_wipe()` - Wipe all storage

#### `PermissionManager`
Manages permission system.

**Methods:**
- `request_permission(type, reason)` - Request permission
- `grant_permission(request_id)` - Grant permission
- `deny_permission(request_id)` - Deny permission
- `check_permission(type)` - Check if permission exists
- `get_permission_history()` - Get audit log

#### `OwnerRecognitionEngine`
Multi-modal biometric verification.

**Methods:**
- `enroll_owner(audio, text, behavioral)` - Enroll owner
- `verify_owner(audio, text, behavioral)` - Verify owner
- `detect_spoofing(audio)` - Detect spoofing attempts
- `update_profile(...)` - Update biometric profile

#### `SelfLearningEngine`
Autonomous learning system.

**Methods:**
- `record_interaction(type, data)` - Record interaction
- `get_learned_patterns()` - Get learned patterns
- `get_preferences()` - Get learned preferences
- `predict_preference(...)` - Predict preference
- `get_linguistic_style()` - Get linguistic analysis

## 🎨 Personalization

The system automatically generates personalized UI elements based on learned preferences:

- **Color Themes** - Based on emotional profile
- **Typography** - Based on communication complexity
- **Layout** - Based on content preferences
- **Dashboard** - Based on usage patterns
- **Custom Commands** - Based on frequent actions

## 📝 Configuration

Edit `config.py` to customize:

```python
# Encryption settings
ENCRYPTION_KEY_SIZE = 256
ENCRYPTION_ITERATIONS = 100000

# Biometric thresholds
VOICE_CONFIDENCE_THRESHOLD = 0.85
OVERALL_CONFIDENCE_THRESHOLD = 0.80

# Learning settings
MIN_INTERACTIONS_FOR_LEARNING = 10
ENABLE_AUTO_LEARNING = True

# Security settings
MAX_FAILED_AUTH_ATTEMPTS = 3
AUTH_LOCKOUT_TIME = 300
```

## 🛡️ Security Warnings

1. **Master Password**: Never share your master password. Loss means permanent data loss.
2. **Backup**: Regularly backup encrypted hidden storage if needed.
3. **Permissions**: Review permission requests carefully.
4. **Secure Wipe**: The secure wipe operation is IRREVERSIBLE.

## 🐛 Troubleshooting

### Common Issues

**Issue: Import errors**
```bash
# Solution: Install all dependencies
pip install -r requirements.txt
```

**Issue: Permission denied on hidden directory**
```bash
# Solution: Check directory permissions
chmod 700 amrit_hidden_space/
```

**Issue: Authentication fails**
```bash
# Solution: Re-enroll owner or check if system is locked
# Wait for lockout period to expire
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

This is a prototype system for educational purposes. For production use:
- Implement proper audio processing with librosa/pyannote
- Use production-grade ML models for biometric verification
- Add comprehensive error handling
- Implement secure key management
- Add comprehensive testing
- Follow security best practices

## 👤 Author

Amrit Gupta

## 🙏 Acknowledgments

Built with:
- Python cryptography libraries
- NumPy for numerical operations
- Multi-modal biometric concepts
- Machine learning principles

---

**🔮 AMRIT AI - Your Personal Intelligence, Securely Yours**
