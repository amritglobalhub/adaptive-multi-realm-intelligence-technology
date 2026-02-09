# 🔮 AMRIT AI - API Documentation

## Table of Contents
1. [Core Classes](#core-classes)
2. [Module Reference](#module-reference)
3. [Configuration](#configuration)
4. [Error Handling](#error-handling)

## Core Classes

### AMRITSystem

Main system orchestrator that integrates all components.

#### Constructor

```python
AMRITSystem(master_password: str)
```

**Parameters:**
- `master_password` (str): Master password for encryption. **Cannot be recovered if lost.**

**Example:**
```python
system = AMRITSystem("my_secure_password")
```

#### Methods

##### `enroll_owner(audio_samples, text_samples, behavioral_samples) -> bool`

Enroll owner for first-time setup with biometric samples.

**Parameters:**
- `audio_samples` (list): List of numpy arrays with voice samples
- `text_samples` (list): List of transcribed text strings
- `behavioral_samples` (list): List of behavioral data dictionaries

**Returns:**
- `bool`: True if enrollment successful

**Example:**
```python
audio = [np.random.randn(16000) for _ in range(3)]
text = ["Hello", "AMRIT", "Initialize"]
behavioral = [{'timestamp': '...', 'duration': 10}] * 3
success = system.enroll_owner(audio, text, behavioral)
```

##### `authenticate_owner(audio_data=None, text=None, behavioral_data=None) -> bool`

Authenticate owner using multi-modal biometrics.

**Parameters:**
- `audio_data` (np.ndarray, optional): Voice sample
- `text` (str, optional): Transcribed text
- `behavioral_data` (dict, optional): Behavioral data

**Returns:**
- `bool`: True if authenticated

**Example:**
```python
audio = np.random.randn(16000)
authenticated = system.authenticate_owner(audio_data=audio, text="Hello")
```

##### `record_interaction(interaction_type, data) -> str`

Record an interaction for learning.

**Parameters:**
- `interaction_type` (str): Type of interaction ('command', 'query', 'conversation', 'preference')
- `data` (dict): Interaction data

**Returns:**
- `str`: Interaction ID

**Example:**
```python
interaction_id = system.record_interaction('command', {
    'command': 'process_data',
    'context': {'dataset': 'sales'},
    'success': True
})
```

##### `request_permission(permission_type, reason) -> str`

Request permission for an operation.

**Parameters:**
- `permission_type` (PermissionType): Type of permission
- `reason` (str): Human-readable reason

**Returns:**
- `str`: Permission request ID

**Example:**
```python
from permission_manager import PermissionType
request_id = system.request_permission(
    PermissionType.DATA_MODIFICATION,
    "Need to update database"
)
```

##### `grant_permission(request_id, duration=None) -> bool`

Grant a permission request.

**Parameters:**
- `request_id` (str): Permission request ID
- `duration` (int, optional): Duration in seconds

**Returns:**
- `bool`: True if granted

**Example:**
```python
system.grant_permission(request_id, duration=3600)
```

##### `get_learned_patterns() -> dict`

Get all learned patterns.

**Returns:**
- `dict`: Dictionary of learned patterns

##### `get_preferences() -> dict`

Get learned preferences.

**Returns:**
- `dict`: Dictionary of preferences

##### `get_personalization_profile() -> dict`

Get personalization profile.

**Returns:**
- `dict`: Personalization profile

##### `run_data_analysis() -> dict`

Run complete data mining analysis.

**Returns:**
- `dict`: Analysis insights

**Requires:** Permission for DATA_MODIFICATION

##### `generate_personalized_ui() -> dict`

Generate personalized UI based on learned preferences.

**Returns:**
- `dict`: UI configuration

**Requires:** Permission for SYSTEM_UPDATE

##### `get_system_status() -> dict`

Get comprehensive system status.

**Returns:**
- `dict`: System status

##### `print_status()`

Print system status in readable format.

##### `end_session()`

End current session and cleanup.

##### `secure_wipe() -> bool`

Securely wipe all data. **IRREVERSIBLE!**

**Returns:**
- `bool`: True if wiped successfully

---

### EncryptionManager

Handles all encryption and decryption operations.

#### Constructor

```python
EncryptionManager(master_password: str = None)
```

#### Methods

##### `encrypt(data, password=None) -> tuple`

Encrypt data with AES-256.

**Parameters:**
- `data` (str or bytes): Data to encrypt
- `password` (str, optional): Password (uses master if not provided)

**Returns:**
- `tuple`: (encrypted_data, salt)

##### `decrypt(encrypted_data, salt, password=None) -> bytes`

Decrypt data.

**Parameters:**
- `encrypted_data` (bytes): Encrypted data
- `salt` (bytes): Salt used for encryption
- `password` (str, optional): Password

**Returns:**
- `bytes`: Decrypted data

##### `hash_data(data) -> str`

Create SHA-256 hash of data.

**Parameters:**
- `data` (str or bytes): Data to hash

**Returns:**
- `str`: Hexadecimal hash string

##### `encrypt_file(file_path, output_path, password=None)`

Encrypt a file.

##### `decrypt_file(encrypted_file_path, output_path, password=None)`

Decrypt a file.

##### `multi_layer_encrypt(data, passwords) -> tuple`

Apply multiple layers of encryption.

**Parameters:**
- `data` (str or bytes): Data to encrypt
- `passwords` (list): List of passwords for each layer

**Returns:**
- `tuple`: (encrypted_data, salts_list)

##### `multi_layer_decrypt(encrypted_data, salts, passwords) -> bytes`

Decrypt multiple layers.

---

### HiddenStorageManager

Manages encrypted hidden storage.

#### Constructor

```python
HiddenStorageManager(master_password: str)
```

#### Methods

##### `initialize() -> bool`

Initialize hidden storage structure.

**Returns:**
- `bool`: True if successful

##### `store_data(category, key, data, use_pickle=False) -> bool`

Store encrypted data.

**Parameters:**
- `category` (str): Storage category
- `key` (str): Data identifier
- `data` (Any): Data to store
- `use_pickle` (bool): Whether to pickle data first

**Returns:**
- `bool`: True if successful

**Categories:**
- `personal_biometrics`
- `behavior_profiles`
- `recognition_engine`
- `learning_logs`
- `system_intelligence`

##### `retrieve_data(category, key) -> Any`

Retrieve and decrypt data.

**Parameters:**
- `category` (str): Storage category
- `key` (str): Data identifier

**Returns:**
- Data or None if not found

##### `delete_data(category, key) -> bool`

Securely delete data.

##### `list_keys(category) -> list`

List all keys in category.

##### `store_model(category, model_name, model_obj) -> bool`

Store a machine learning model.

##### `retrieve_model(category, model_name) -> Any`

Retrieve a machine learning model.

##### `secure_wipe() -> bool`

Securely wipe all hidden storage.

---

### PermissionManager

Manages permission system.

#### Constructor

```python
PermissionManager(storage_manager: HiddenStorageManager)
```

#### Methods

##### `request_permission(permission_type, reason, metadata=None) -> str`

Request permission for an operation.

**Parameters:**
- `permission_type` (PermissionType): Type of permission
- `reason` (str): Human-readable reason
- `metadata` (dict, optional): Additional context

**Returns:**
- `str`: Permission request ID

##### `grant_permission(request_id, duration=None) -> bool`

Grant a permission request.

##### `deny_permission(request_id, reason="") -> bool`

Deny a permission request.

##### `check_permission(permission_type) -> bool`

Check if there's an active permission.

##### `revoke_permission(request_id) -> bool`

Revoke an active permission.

##### `revoke_all_permissions(permission_type=None)`

Revoke all active permissions.

##### `get_permission_history(limit=100) -> list`

Get permission history log.

##### `get_active_permissions() -> list`

Get all currently active permissions.

##### `get_statistics() -> dict`

Get permission statistics.

#### PermissionType Enum

```python
class PermissionType(Enum):
    DATA_MODIFICATION = "data_modification"
    SYSTEM_UPDATE = "system_update"
    POLICY_CHANGE = "policy_change"
    MODEL_TRAINING = "model_training"
    EXTERNAL_ACCESS = "external_access"
    AUTO_LEARNING = "auto_learning"
    FILE_ACCESS = "file_access"
    NETWORK_ACCESS = "network_access"
```

---

### OwnerRecognitionEngine

Multi-modal biometric verification system.

#### Constructor

```python
OwnerRecognitionEngine(storage_manager: HiddenStorageManager)
```

#### Methods

##### `enroll_owner(audio_samples, text_samples, behavioral_data) -> bool`

Enroll owner with biometric samples.

##### `verify_owner(audio_data=None, text=None, behavioral_data=None) -> tuple`

Verify if current user is the owner.

**Returns:**
- `tuple`: (is_owner, confidence_score)

##### `detect_spoofing(audio_data) -> tuple`

Detect if audio sample is potentially spoofed.

**Returns:**
- `tuple`: (is_spoofed, confidence)

##### `update_profile(audio_data=None, text=None, behavioral_data=None)`

Update owner profile with new verified samples.

##### `get_profile_stats() -> dict`

Get statistics about owner profile.

---

### SelfLearningEngine

Autonomous learning system.

#### Constructor

```python
SelfLearningEngine(storage_manager, permission_manager)
```

#### Methods

##### `record_interaction(interaction_type, data) -> str`

Record an interaction for learning.

##### `get_learned_patterns(pattern_type=None) -> dict`

Get learned patterns.

##### `get_preferences(preference_type=None) -> dict`

Get learned preferences.

##### `predict_preference(preference_type, options) -> str`

Predict preferred option from list.

##### `predict_next_action(context) -> str`

Predict next likely action.

##### `get_linguistic_style() -> dict`

Get analyzed linguistic style.

##### `get_interaction_statistics() -> dict`

Get statistics about interactions.

##### `export_learned_knowledge() -> dict`

Export all learned knowledge.

---

### DataMiningPipeline

Mines user data for personalization.

#### Constructor

```python
DataMiningPipeline(storage_manager: HiddenStorageManager)
```

#### Methods

##### `mine_command_preferences(interaction_history) -> dict`

Mine command preferences.

##### `mine_response_preferences(interaction_history) -> dict`

Mine response style preferences.

##### `mine_time_patterns(interaction_history) -> dict`

Mine temporal usage patterns.

##### `mine_communication_style(linguistic_patterns) -> dict`

Mine communication style.

##### `run_full_analysis(interaction_history, linguistic_patterns) -> dict`

Run complete data mining analysis.

##### `get_personalization_profile() -> dict`

Get comprehensive personalization profile.

---

### UIPersonalizationEngine

Generates customized UI/UX.

#### Constructor

```python
UIPersonalizationEngine(storage_manager: HiddenStorageManager)
```

#### Methods

##### `generate_color_theme(preferences) -> dict`

Generate color theme based on preferences.

##### `generate_logo_concept(preferences) -> dict`

Generate logo concept.

##### `generate_custom_commands(learned_patterns) -> dict`

Generate custom commands.

##### `generate_dashboard_layout(preferences) -> dict`

Generate personalized dashboard layout.

##### `create_personalized_ui(personalization_profile, learned_patterns) -> dict`

Create complete personalized UI configuration.

##### `get_current_theme() -> dict`

Get current UI theme.

##### `update_theme_color(color_key, color_value)`

Update a specific theme color.

---

## Configuration

Configuration is managed in `config.py`. Key settings:

### Encryption Settings
```python
ENCRYPTION_KEY_SIZE = 256  # AES-256
ENCRYPTION_ITERATIONS = 100000  # PBKDF2 iterations
SALT_SIZE = 32  # bytes
```

### Biometric Thresholds
```python
VOICE_CONFIDENCE_THRESHOLD = 0.70
BEHAVIOR_CONFIDENCE_THRESHOLD = 0.70
OVERALL_CONFIDENCE_THRESHOLD = 0.70
```

### Learning Settings
```python
MIN_INTERACTIONS_FOR_LEARNING = 10
LEARNING_BATCH_SIZE = 100
MODEL_UPDATE_FREQUENCY = 1000
ENABLE_AUTO_LEARNING = True
```

### Security Settings
```python
MAX_FAILED_AUTH_ATTEMPTS = 3
AUTH_LOCKOUT_TIME = 300  # seconds
SESSION_TIMEOUT = 1800  # seconds
```

### Permission Settings
```python
PERMISSION_EXPIRY_TIME = 3600  # seconds
REQUIRE_PERMISSION_FOR = [
    "data_modification",
    "system_update",
    "policy_change",
    "model_training",
    "external_access",
]
```

---

## Error Handling

### Common Exceptions

```python
try:
    system = AMRITSystem("password")
except Exception as e:
    print(f"Initialization failed: {e}")
```

### Authentication Errors

```python
authenticated = system.authenticate_owner(audio_data=audio)
if not authenticated:
    # Check if locked
    if system.owner_recognition.is_locked():
        print("System is locked. Wait for lockout period.")
    else:
        print("Authentication failed. Try again.")
```

### Permission Errors

```python
if not system.permissions.check_permission(PermissionType.DATA_MODIFICATION):
    req_id = system.request_permission(
        PermissionType.DATA_MODIFICATION,
        "Need permission"
    )
    system.grant_permission(req_id)
```

### Storage Errors

```python
success = system.storage.store_data(category, key, data)
if not success:
    print("Failed to store data")
```

---

## Best Practices

1. **Always authenticate before operations**
2. **Request permissions explicitly**
3. **End sessions properly**
4. **Handle authentication failures gracefully**
5. **Regular permission audits**
6. **Secure master password**
7. **Never commit hidden storage**

---

**🔮 AMRIT AI - Complete API Reference**
