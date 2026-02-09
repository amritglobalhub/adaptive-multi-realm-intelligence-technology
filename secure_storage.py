"""
AMRIT AI Secure Storage Manager
Manages the hidden encrypted vault for all user data
Only accessible by user and AMRIT AI
"""

import os
import json
from datetime import datetime
from typing import Any, Dict, List, Optional
import amrit_config as config
from encryption_manager import encryption_manager


class SecureStorage:
    """
    Secure storage manager for AMRIT AI
    All data is encrypted and stored in hidden vault
    """
    
    def __init__(self):
        self._initialize_vault()
    
    def _initialize_vault(self):
        """Initialize the secure vault structure"""
        # Create all necessary directories
        directories = [
            config.DATA_DIR,
            config.VOICE_DATA_DIR,
            config.PREFERENCES_DIR,
            config.PROJECTS_DIR,
            config.DESIGNS_DIR,
            config.PATTERNS_DIR
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            # Set restrictive permissions (owner only)
            os.chmod(directory, 0o700)
        
        # Hide the vault directory on Unix-like systems
        if not config.DATA_DIR.split('/')[-1].startswith('.'):
            # Already hidden by naming convention
            pass
    
    def save_voice_biometric(self, voice_data: Dict[str, Any]) -> str:
        """
        Save voice biometric data
        
        Args:
            voice_data: Dictionary containing voice pattern data
        
        Returns:
            ID of saved biometric
        """
        timestamp = datetime.now().isoformat()
        biometric_id = encryption_manager.hash_data(timestamp)
        
        voice_data['timestamp'] = timestamp
        voice_data['biometric_id'] = biometric_id
        
        file_path = os.path.join(config.VOICE_DATA_DIR, f'{biometric_id}.dat')
        
        # Encrypt and save
        encrypted_data = encryption_manager.encrypt_data(voice_data)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        
        os.chmod(file_path, 0o600)
        
        return biometric_id
    
    def load_voice_biometric(self, biometric_id: str) -> Optional[Dict[str, Any]]:
        """Load voice biometric data"""
        file_path = os.path.join(config.VOICE_DATA_DIR, f'{biometric_id}.dat')
        
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        return encryption_manager.decrypt_data(encrypted_data)
    
    def save_preference(self, category: str, preference_data: Dict[str, Any]):
        """
        Save user preference data
        
        Args:
            category: Category of preference (coding_style, design_style, etc.)
            preference_data: Preference data to save
        """
        file_path = os.path.join(config.PREFERENCES_DIR, f'{category}.dat')
        
        # Load existing preferences if any
        existing_prefs = {}
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                existing_prefs = encryption_manager.decrypt_data(f.read())
        
        # Update with new preferences
        existing_prefs.update(preference_data)
        existing_prefs['last_updated'] = datetime.now().isoformat()
        
        # Encrypt and save
        encrypted_data = encryption_manager.encrypt_data(existing_prefs)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        
        os.chmod(file_path, 0o600)
    
    def load_preference(self, category: str) -> Optional[Dict[str, Any]]:
        """Load user preference data"""
        file_path = os.path.join(config.PREFERENCES_DIR, f'{category}.dat')
        
        if not os.path.exists(file_path):
            return {}
        
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        return encryption_manager.decrypt_data(encrypted_data)
    
    def save_project(self, project_name: str, project_data: Dict[str, Any]) -> str:
        """
        Save generated project
        
        Args:
            project_name: Name of the project
            project_data: Project data including code, metadata, etc.
        
        Returns:
            Project ID
        """
        timestamp = datetime.now().isoformat()
        project_id = encryption_manager.hash_data(f"{project_name}_{timestamp}")
        
        project_data['project_id'] = project_id
        project_data['project_name'] = project_name
        project_data['created_at'] = timestamp
        
        # Create project directory
        project_dir = os.path.join(config.PROJECTS_DIR, project_id)
        os.makedirs(project_dir, exist_ok=True)
        os.chmod(project_dir, 0o700)
        
        # Save project metadata
        metadata_path = os.path.join(project_dir, 'metadata.dat')
        encrypted_data = encryption_manager.encrypt_data(project_data)
        with open(metadata_path, 'wb') as f:
            f.write(encrypted_data)
        
        os.chmod(metadata_path, 0o600)
        
        return project_id
    
    def load_project(self, project_id: str) -> Optional[Dict[str, Any]]:
        """Load project data"""
        project_dir = os.path.join(config.PROJECTS_DIR, project_id)
        metadata_path = os.path.join(project_dir, 'metadata.dat')
        
        if not os.path.exists(metadata_path):
            return None
        
        with open(metadata_path, 'rb') as f:
            encrypted_data = f.read()
        
        return encryption_manager.decrypt_data(encrypted_data)
    
    def save_design(self, design_name: str, design_data: Dict[str, Any]) -> str:
        """
        Save generated design
        
        Args:
            design_name: Name of the design
            design_data: Design data including styles, assets, etc.
        
        Returns:
            Design ID
        """
        timestamp = datetime.now().isoformat()
        design_id = encryption_manager.hash_data(f"{design_name}_{timestamp}")
        
        design_data['design_id'] = design_id
        design_data['design_name'] = design_name
        design_data['created_at'] = timestamp
        
        file_path = os.path.join(config.DESIGNS_DIR, f'{design_id}.dat')
        
        # Encrypt and save
        encrypted_data = encryption_manager.encrypt_data(design_data)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        
        os.chmod(file_path, 0o600)
        
        return design_id
    
    def load_design(self, design_id: str) -> Optional[Dict[str, Any]]:
        """Load design data"""
        file_path = os.path.join(config.DESIGNS_DIR, f'{design_id}.dat')
        
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        return encryption_manager.decrypt_data(encrypted_data)
    
    def save_learned_pattern(self, pattern_type: str, pattern_data: Dict[str, Any]):
        """
        Save learned behavioral patterns
        
        Args:
            pattern_type: Type of pattern (communication, coding, design, etc.)
            pattern_data: Pattern data
        """
        file_path = os.path.join(config.PATTERNS_DIR, f'{pattern_type}.dat')
        
        # Load existing patterns if any
        existing_patterns = []
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                existing_patterns = encryption_manager.decrypt_data(f.read())
        
        # Add new pattern with timestamp
        pattern_data['timestamp'] = datetime.now().isoformat()
        existing_patterns.append(pattern_data)
        
        # Encrypt and save
        encrypted_data = encryption_manager.encrypt_data(existing_patterns)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        
        os.chmod(file_path, 0o600)
    
    def load_learned_patterns(self, pattern_type: str) -> List[Dict[str, Any]]:
        """Load learned patterns"""
        file_path = os.path.join(config.PATTERNS_DIR, f'{pattern_type}.dat')
        
        if not os.path.exists(file_path):
            return []
        
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        return encryption_manager.decrypt_data(encrypted_data)
    
    def get_vault_status(self) -> Dict[str, Any]:
        """Get status of the secure vault"""
        status = {
            'initialized': os.path.exists(config.DATA_DIR),
            'encrypted': config.DATA_ENCRYPTION_ENABLED,
            'security_level': config.SECURITY_LEVEL,
            'voice_biometrics_count': len(os.listdir(config.VOICE_DATA_DIR)) if os.path.exists(config.VOICE_DATA_DIR) else 0,
            'projects_count': len(os.listdir(config.PROJECTS_DIR)) if os.path.exists(config.PROJECTS_DIR) else 0,
            'designs_count': len(os.listdir(config.DESIGNS_DIR)) if os.path.exists(config.DESIGNS_DIR) else 0
        }
        
        return status


# Global secure storage instance
secure_storage = SecureStorage()
