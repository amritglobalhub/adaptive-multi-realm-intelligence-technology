"""
AMRIT AI - Adaptive Multi-Realm Intelligence Technology
Configuration Module

This module contains all configuration settings for the AMRIT AI system.
"""

import os
from pathlib import Path

# Base Directories
BASE_DIR = Path(__file__).parent.absolute()
HIDDEN_SPACE_DIR = BASE_DIR / "amrit_hidden_space"

# Hidden Directory Structure
HIDDEN_DIRS = {
    "personal_biometrics": HIDDEN_SPACE_DIR / "personal_biometrics",
    "behavior_profiles": HIDDEN_SPACE_DIR / "behavior_profiles",
    "recognition_engine": HIDDEN_SPACE_DIR / "recognition_engine",
    "learning_logs": HIDDEN_SPACE_DIR / "learning_logs",
    "system_intelligence": HIDDEN_SPACE_DIR / "system_intelligence",
}

# Encryption Settings
ENCRYPTION_KEY_SIZE = 256  # AES-256
ENCRYPTION_ITERATIONS = 100000  # PBKDF2 iterations
SALT_SIZE = 32  # bytes

# Voice Recognition Settings
VOICE_SAMPLE_RATE = 16000  # Hz
VOICE_CHANNELS = 1  # Mono
VOICE_CHUNK_SIZE = 1024
VOICE_FORMAT = "WAV"

# Biometric Thresholds
VOICE_CONFIDENCE_THRESHOLD = 0.70
BEHAVIOR_CONFIDENCE_THRESHOLD = 0.70
OVERALL_CONFIDENCE_THRESHOLD = 0.70

# Learning Settings
MIN_INTERACTIONS_FOR_LEARNING = 10
LEARNING_BATCH_SIZE = 100
MODEL_UPDATE_FREQUENCY = 1000  # interactions

# Permission Settings
PERMISSION_EXPIRY_TIME = 3600  # seconds (1 hour)
REQUIRE_PERMISSION_FOR = [
    "data_modification",
    "system_update",
    "policy_change",
    "model_training",
    "external_access",
]

# Database Settings
DB_NAME = "amrit_intelligence.db"
DB_ENCRYPTED = True

# Logging Settings
LOG_LEVEL = "INFO"
LOG_RETENTION_DAYS = 30
LOG_ENCRYPTION = True

# Security Settings
MAX_FAILED_AUTH_ATTEMPTS = 3
AUTH_LOCKOUT_TIME = 300  # seconds (5 minutes)
SESSION_TIMEOUT = 1800  # seconds (30 minutes)

# Model Paths (within hidden space)
MODELS = {
    "voice_recognition": "recognition_engine/owner_identification_model.pkl.enc",
    "face_recognition": "recognition_engine/face_recognition_data.enc",
    "behavior_fingerprint": "recognition_engine/behavior_fingerprint.enc",
    "predictive_models": "system_intelligence/predictive_models.enc",
    "personalization": "system_intelligence/personalization_engine.enc",
}

# Feature Flags
ENABLE_VOICE_RECOGNITION = True
ENABLE_FACE_RECOGNITION = False  # Requires camera
ENABLE_GAIT_ANALYSIS = False  # Requires motion sensors
ENABLE_AUTO_LEARNING = True
ENABLE_PERSONALIZATION = True

# System Information
SYSTEM_NAME = "AMRIT"
SYSTEM_VERSION = "1.0.0"
SYSTEM_DESCRIPTION = "Adaptive Multi-Realm Intelligence Technology"

# Privacy Settings
ANONYMIZE_LOGS = True
CLEAR_CACHE_ON_EXIT = True
NO_EXTERNAL_TELEMETRY = True

# UI Generation Settings
UI_THEME_COLORS = 5  # Number of colors to extract for theme
UI_UPDATE_FREQUENCY = 50  # interactions
GENERATE_LOGO = True
GENERATE_DASHBOARD = True

# Data Mining Settings
PATTERN_DETECTION_WINDOW = 100  # interactions
PREFERENCE_WEIGHT_DECAY = 0.95  # Recent preferences weighted higher
MIN_PATTERN_OCCURRENCES = 3

# Anomaly Detection
ANOMALY_DETECTION_SENSITIVITY = 0.1
SPOOFING_DETECTION_ENABLED = True

# API Settings
API_HOST = "127.0.0.1"
API_PORT = 8000
API_RELOAD = False  # Set to False in production

# Environment Variables (Override config)
def load_from_env():
    """Load configuration from environment variables if present"""
    global API_HOST, API_PORT, LOG_LEVEL
    
    API_HOST = os.getenv("AMRIT_API_HOST", API_HOST)
    API_PORT = int(os.getenv("AMRIT_API_PORT", API_PORT))
    LOG_LEVEL = os.getenv("AMRIT_LOG_LEVEL", LOG_LEVEL)

load_from_env()
