"""
AMRIT AI Configuration Module
Contains all system configuration, constants, and settings
"""

import os

# System Information
SYSTEM_NAME = "AMRIT AI"
SYSTEM_VERSION = "1.0.0"
SYSTEM_DESCRIPTION = "Adaptive Multi-Realm Intelligence Technology"

# User Information (from numerology_core.py)
USER_BIRTH_DATE = '06/11/2000'
USER_BIRTH_TIME = '18:00'
USER_BIRTH_PLACE = 'New Delhi'
USER_NAME = 'Amrit Gupta'

# Storage Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '.amrit_vault')
VOICE_DATA_DIR = os.path.join(DATA_DIR, 'voice_biometrics')
PREFERENCES_DIR = os.path.join(DATA_DIR, 'preferences')
PROJECTS_DIR = os.path.join(DATA_DIR, 'generated_projects')
DESIGNS_DIR = os.path.join(DATA_DIR, 'generated_designs')
PATTERNS_DIR = os.path.join(DATA_DIR, 'learned_patterns')
ENCRYPTION_KEY_PATH = os.path.join(DATA_DIR, '.encryption_key')

# Security Settings
ENCRYPTION_ALGORITHM = 'AES-256-GCM'
ENCRYPTION_KEY_SIZE = 32  # 256 bits
SECURITY_LEVEL = 'MILITARY_GRADE'

# Voice Learning Settings
VOICE_SAMPLE_RATE = 16000
VOICE_CHANNELS = 1
VOICE_LEARNING_PHASES = {
    'RECOGNITION': {'duration_days': 7, 'samples_required': 100},
    'LEARNING': {'duration_days': 28, 'samples_required': 500},
    'ADAPTATION': {'duration_days': 90, 'samples_required': 2000},
    'MASTERY': {'duration_days': 180, 'samples_required': 5000}
}

# Code Generation Settings
SUPPORTED_LANGUAGES = [
    'Python',
    'JavaScript',
    'Java',
    'C++',
    'TypeScript',
    'Go',
    'Rust',
    'Ruby',
    'PHP',
    'C#'
]

PROJECT_TYPES = [
    'Website',
    'Mobile App',
    'Desktop App',
    'API Server',
    'E-commerce',
    'Dashboard',
    'Database',
    'CLI Tool',
    'Library',
    'Framework'
]

# Design Generation Settings
DESIGN_CATEGORIES = [
    'Logo',
    'Brand Identity',
    'UI/UX',
    'Color Scheme',
    'Typography',
    'Layout',
    'Icons',
    'Illustrations'
]

# Learning System Settings
LEARNING_RATE = 0.01
ADAPTATION_THRESHOLD = 0.85
CONFIDENCE_THRESHOLD = 0.90

# Offline Capabilities
OFFLINE_MODE = True
LOCAL_DATABASE = 'sqlite'
LOCAL_WEB_SERVER_PORT = 8000

# Privacy & Security Settings
DATA_ENCRYPTION_ENABLED = True
THIRD_PARTY_ACCESS = False
CLOUD_SYNC_ENABLED = False  # Only when internet available and user permits
AUTO_BACKUP_ENABLED = True
BACKUP_FREQUENCY_HOURS = 24

# System Permissions
PERMISSIONS = {
    'VOICE_RECORDING': True,
    'PREFERENCE_STORAGE': True,
    'AUTO_CODE_GENERATION': True,
    'ENCRYPTED_VAULT': True,
    'SELF_LEARNING': True,
    'DESIGN_GENERATION': True,
    'OFFLINE_CAPABILITIES': True,
    'CLOUD_FEATURES': False  # Requires internet and user permission
}

# Feature Flags
FEATURES = {
    'VOICE_LEARNING': True,
    'CODE_GENERATION': True,
    'DESIGN_GENERATION': True,
    'AUTO_OPTIMIZATION': True,
    'PATTERN_RECOGNITION': True,
    'PREFERENCE_LEARNING': True,
    'ANTICIPATORY_SUGGESTIONS': True,
    'AUTONOMOUS_UPDATES': True
}
