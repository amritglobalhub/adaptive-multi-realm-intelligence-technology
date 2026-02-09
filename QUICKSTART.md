# 🔮 AMRIT AI - Quick Start Guide

## Table of Contents
1. [Installation](#installation)
2. [First-Time Setup](#first-time-setup)
3. [Basic Usage](#basic-usage)
4. [Advanced Features](#advanced-features)
5. [Security Best Practices](#security-best-practices)

## Installation

### Prerequisites
- Python 3.10+
- pip package manager
- Basic understanding of command line

### Step 1: Clone Repository
```bash
git clone https://github.com/amritglobalhub/adaptive-multi-realm-intelligence-technology.git
cd adaptive-multi-realm-intelligence-technology
```

### Step 2: Install Dependencies
```bash
# Install core dependencies
pip install numpy cryptography

# Optional: Install all dependencies for full functionality
pip install -r requirements.txt
```

### Step 3: Verify Installation
```bash
python3 -c "from amrit_system import AMRITSystem; print('✅ AMRIT AI installed successfully!')"
```

## First-Time Setup

### 1. Initialize System

```python
from amrit_system import AMRITSystem

# Create system with master password
# ⚠️ IMPORTANT: Remember this password! It cannot be recovered.
system = AMRITSystem("your_secure_password_here")
```

### 2. Enroll as Owner

For first-time setup, you need to enroll your biometric data:

```python
import numpy as np
from datetime import datetime

# Prepare voice samples (3-5 samples recommended)
# In production, use real audio recording
audio_samples = [
    # Record yourself saying different phrases
    # For demo: np.random.randn(16000)
]

# Prepare text samples (what you said in audio)
text_samples = [
    "Hello AMRIT",
    "Initialize learning system",
    "I am the owner"
]

# Prepare behavioral data
behavioral_samples = [
    {
        'timestamp': datetime.now().isoformat(),
        'duration': 10,  # seconds
        'typing_speed': 45  # optional
    }
    # Add more samples
]

# Enroll
success = system.enroll_owner(
    audio_samples,
    text_samples,
    behavioral_samples
)

if success:
    print("✅ Enrollment successful!")
```

### 3. First Authentication

```python
# Authenticate with your voice and text
audio = # Your voice sample
text = "Hello AMRIT"

authenticated = system.authenticate_owner(
    audio_data=audio,
    text=text
)

if authenticated:
    print("✅ Welcome, Owner!")
    system.print_status()
```

## Basic Usage

### Recording Interactions

```python
# Record a command interaction
system.record_interaction('command', {
    'command': 'analyze_data',
    'context': {'dataset': 'sales_2024'},
    'success': True
})

# Record a query interaction
system.record_interaction('query', {
    'query': 'What are the trends?',
    'response': 'Sales increased by 15%...',
    'satisfaction': 0.9  # 0-1 scale
})

# Record a conversation
system.record_interaction('conversation', {
    'text': 'I prefer brief responses with examples'
})

# Record a preference
system.record_interaction('preference', {
    'type': 'response_style',
    'value': 'brief_with_examples'
})
```

### Requesting Permissions

```python
from permission_manager import PermissionType

# Request permission for sensitive operation
request_id = system.request_permission(
    PermissionType.DATA_MODIFICATION,
    "Need to update preference database"
)

# Grant permission (in production, this would be voice-confirmed)
system.grant_permission(request_id, duration=3600)  # 1 hour

# Check if permission is active
if system.permissions.check_permission(PermissionType.DATA_MODIFICATION):
    # Perform operation
    pass
```

### Getting Learned Patterns

```python
# Get all learned patterns
patterns = system.get_learned_patterns()

# Get learned preferences
preferences = system.get_preferences()

# Get personalization profile
profile = system.get_personalization_profile()
```

### Running Data Analysis

```python
# Request permission first
req_id = system.request_permission(
    PermissionType.DATA_MODIFICATION,
    "Running data analysis"
)
system.grant_permission(req_id)

# Run analysis
insights = system.run_data_analysis()

print(f"Sample size: {insights['sample_size']}")
print(f"Command preferences: {insights['command_preferences']}")
```

### Generating Personalized UI

```python
# Request permission
req_id = system.request_permission(
    PermissionType.SYSTEM_UPDATE,
    "Generating personalized UI"
)
system.grant_permission(req_id)

# Generate UI
ui_config = system.generate_personalized_ui()

print(f"Theme colors: {ui_config['theme']}")
print(f"Dashboard widgets: {ui_config['dashboard']}")
print(f"Custom commands: {ui_config['custom_commands']}")
```

### Ending Session

```python
# Always end session properly
system.end_session()
```

## Advanced Features

### Custom Learning Patterns

```python
from self_learning import SelfLearningEngine

# Access learning engine directly
learning = system.learning_engine

# Get linguistic style
style = learning.get_linguistic_style()
print(f"Vocabulary size: {style['vocabulary_size']}")
print(f"Common words: {style['most_common_words']}")

# Predict next action
predicted_action = learning.predict_next_action({'context': 'work'})
```

### Multi-Layer Encryption

```python
from encryption import EncryptionManager

manager = EncryptionManager("password")

# Apply multiple encryption layers
data = "sensitive data"
passwords = ["password1", "password2", "password3"]
encrypted, salts = manager.multi_layer_encrypt(data, passwords)

# Decrypt (must use same passwords in same order)
decrypted = manager.multi_layer_decrypt(encrypted, salts, passwords)
```

### Direct Storage Access

```python
# Store custom data
system.storage.store_data(
    'behavior_profiles',
    'my_custom_key',
    {'custom': 'data'}
)

# Retrieve custom data
data = system.storage.retrieve_data(
    'behavior_profiles',
    'my_custom_key'
)

# List all keys in category
keys = system.storage.list_keys('behavior_profiles')
```

### Biometric Profile Updates

```python
# Update owner profile with new samples
system.owner_recognition.update_profile(
    audio_data=new_audio,
    text=new_text,
    behavioral_data=new_behavioral
)

# Get profile statistics
stats = system.owner_recognition.get_profile_stats()
print(f"Sample count: {stats['sample_count']}")
print(f"Last updated: {stats['last_updated']}")
```

## Security Best Practices

### 1. Master Password Management
- Use a strong, unique password (16+ characters)
- Never share your master password
- Store password in secure password manager
- **CANNOT BE RECOVERED** - losing it means losing all data

### 2. Permission Management
- Review all permission requests carefully
- Grant permissions with minimal required duration
- Regularly audit permission history:
  ```python
  history = system.permissions.get_permission_history()
  ```
- Revoke unnecessary permissions:
  ```python
  system.permissions.revoke_all_permissions()
  ```

### 3. Data Security
- Hidden storage is in `amrit_hidden_space/` directory
- Never commit this directory to version control
- Regular backups if needed (encrypted)
- Use secure wipe for complete removal:
  ```python
  system.secure_wipe()  # ⚠️ IRREVERSIBLE!
  ```

### 4. Authentication
- Always use multiple biometric modalities
- Monitor failed authentication attempts
- System auto-locks after 3 failed attempts
- Lockout lasts 5 minutes by default

### 5. Session Management
- Always call `system.end_session()` when done
- Sessions timeout after 30 minutes of inactivity
- Cache is cleared on exit (if configured)
- Never leave system authenticated unattended

## Common Issues & Solutions

### Issue: Import Error
```bash
# Solution: Install dependencies
pip install numpy cryptography
```

### Issue: Authentication Fails
```bash
# Solution 1: Check if system is locked
# Wait 5 minutes or restart system

# Solution 2: Re-enroll if needed
# May be necessary if samples were too different
```

### Issue: Permission Denied
```bash
# Solution: Request and grant permission
req_id = system.request_permission(PermissionType.XXX, "reason")
system.grant_permission(req_id)
```

### Issue: Hidden Directory Not Created
```bash
# Solution: Ensure write permissions
chmod 700 .
python3 -c "from hidden_storage import HiddenStorageManager; h = HiddenStorageManager('pwd'); h.initialize()"
```

## Example Workflow

Complete workflow from start to finish:

```python
from amrit_system import AMRITSystem
from permission_manager import PermissionType
import numpy as np
from datetime import datetime

# 1. Initialize
system = AMRITSystem("secure_password_123")

# 2. Enroll (first time only)
if not system.owner_recognition.owner_profile:
    audio = [np.random.randn(16000) for _ in range(3)]
    text = ["Hello", "AMRIT", "Initialize"]
    behavioral = [{'timestamp': datetime.now().isoformat(), 'duration': 10}] * 3
    system.enroll_owner(audio, text, behavioral)

# 3. Authenticate
audio = np.random.randn(16000)
if system.authenticate_owner(audio_data=audio, text="Hello"):
    
    # 4. Use system
    system.record_interaction('command', {
        'command': 'process_data',
        'success': True
    })
    
    # 5. Request permission for analysis
    req_id = system.request_permission(
        PermissionType.DATA_MODIFICATION,
        "Running analysis"
    )
    system.grant_permission(req_id)
    
    # 6. Analyze
    insights = system.run_data_analysis()
    print(f"Found {insights['sample_size']} interactions")
    
    # 7. Generate UI
    req_id = system.request_permission(
        PermissionType.SYSTEM_UPDATE,
        "Generate UI"
    )
    system.grant_permission(req_id)
    ui = system.generate_personalized_ui()
    
    # 8. Status
    system.print_status()
    
    # 9. End
    system.end_session()
```

## Next Steps

1. Run the example script: `python3 examples.py`
2. Run the test suite: `python3 test_amrit.py`
3. Explore the API documentation in `README.md`
4. Customize `config.py` for your needs
5. Integrate AMRIT into your application

## Support & Documentation

- Full API Reference: See `README.md`
- Example Scripts: See `examples.py`
- Test Suite: See `test_amrit.py`
- Configuration: See `config.py`

---

**🔮 AMRIT AI - Your Personal Intelligence, Securely Yours**
