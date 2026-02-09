"""
AMRIT AI - Hidden Storage System

Manages encrypted hidden directories and files.
Implements steganographic storage and obfuscation.
"""

import os
import json
import pickle
import shutil
from pathlib import Path
from typing import Any, Optional, Dict
from datetime import datetime
import config
from encryption import EncryptionManager


class HiddenStorageManager:
    """Manages hidden encrypted storage for AMRIT AI"""
    
    def __init__(self, master_password: str):
        """
        Initialize hidden storage manager
        
        Args:
            master_password: Master password for encryption
        """
        self.master_password = master_password
        self.encryption_manager = EncryptionManager(master_password)
        self.base_dir = config.HIDDEN_SPACE_DIR
        self.initialized = False
    
    def initialize(self):
        """Initialize hidden storage structure"""
        try:
            # Create base hidden directory
            self.base_dir.mkdir(parents=True, exist_ok=True)
            
            # Create all subdirectories
            for dir_name, dir_path in config.HIDDEN_DIRS.items():
                dir_path.mkdir(parents=True, exist_ok=True)
            
            # Hide directories (Unix systems)
            if os.name == 'posix':
                # Set hidden attribute on Unix
                os.system(f'chmod 700 "{self.base_dir}"')
            
            self.initialized = True
            return True
        except Exception as e:
            print(f"Error initializing hidden storage: {e}")
            return False
    
    def _get_full_path(self, category: str, filename: str) -> Path:
        """
        Get full path for a file in hidden storage
        
        Args:
            category: Storage category (e.g., 'personal_biometrics')
            filename: Filename
            
        Returns:
            Full path to file
        """
        if category not in config.HIDDEN_DIRS:
            raise ValueError(f"Invalid storage category: {category}")
        
        return config.HIDDEN_DIRS[category] / filename
    
    def _obfuscate_filename(self, original_name: str) -> str:
        """
        Obfuscate filename using hash
        
        Args:
            original_name: Original filename
            
        Returns:
            Obfuscated filename
        """
        hash_value = self.encryption_manager.hash_data(original_name)
        return hash_value[:16] + '.enc'
    
    def store_data(self, category: str, key: str, data: Any,
                   use_pickle: bool = False) -> bool:
        """
        Store encrypted data in hidden storage
        
        Args:
            category: Storage category
            key: Data identifier
            data: Data to store
            use_pickle: Whether to pickle the data first
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if not self.initialized:
                self.initialize()
            
            # Prepare data
            if use_pickle:
                data_bytes = pickle.dumps(data)
            elif isinstance(data, dict):
                data_bytes = json.dumps(data).encode('utf-8')
            elif isinstance(data, (list, tuple)):
                data_bytes = json.dumps(data).encode('utf-8')
            elif isinstance(data, str):
                data_bytes = data.encode('utf-8')
            elif isinstance(data, bytes):
                data_bytes = data
            elif isinstance(data, (int, float, bool)):
                data_bytes = json.dumps(data).encode('utf-8')
            else:
                # For any other type, use pickle
                data_bytes = pickle.dumps(data)
            
            # Encrypt data
            encrypted_data, salt = self.encryption_manager.encrypt(data_bytes)
            
            # Get file path
            filename = self._obfuscate_filename(key)
            file_path = self._get_full_path(category, filename)
            
            # Store salt + encrypted data + metadata
            metadata = {
                'key': key,
                'timestamp': datetime.now().isoformat(),
                'pickled': use_pickle,
                'is_json': isinstance(data, dict)
            }
            
            with open(file_path, 'wb') as f:
                # Write salt
                f.write(salt)
                # Write metadata length (4 bytes)
                metadata_bytes = json.dumps(metadata).encode('utf-8')
                metadata_len = len(metadata_bytes)
                f.write(metadata_len.to_bytes(4, byteorder='big'))
                # Write metadata
                f.write(metadata_bytes)
                # Write encrypted data
                f.write(encrypted_data)
            
            # Set restrictive permissions
            if os.name == 'posix':
                os.chmod(file_path, 0o600)
            
            return True
        
        except Exception as e:
            print(f"Error storing data: {e}")
            return False
    
    def retrieve_data(self, category: str, key: str) -> Optional[Any]:
        """
        Retrieve and decrypt data from hidden storage
        
        Args:
            category: Storage category
            key: Data identifier
            
        Returns:
            Decrypted data or None if not found
        """
        try:
            # Get file path
            filename = self._obfuscate_filename(key)
            file_path = self._get_full_path(category, filename)
            
            if not file_path.exists():
                return None
            
            with open(file_path, 'rb') as f:
                # Read salt
                salt = f.read(config.SALT_SIZE)
                # Read metadata length
                metadata_len = int.from_bytes(f.read(4), byteorder='big')
                # Read metadata
                metadata_bytes = f.read(metadata_len)
                metadata = json.loads(metadata_bytes.decode('utf-8'))
                # Read encrypted data
                encrypted_data = f.read()
            
            # Decrypt data
            decrypted_data = self.encryption_manager.decrypt(
                encrypted_data, salt
            )
            
            # Parse data based on metadata
            if metadata.get('pickled'):
                return pickle.loads(decrypted_data)
            elif metadata.get('is_json'):
                return json.loads(decrypted_data.decode('utf-8'))
            else:
                return decrypted_data.decode('utf-8')
        
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return None
    
    def delete_data(self, category: str, key: str) -> bool:
        """
        Delete data from hidden storage
        
        Args:
            category: Storage category
            key: Data identifier
            
        Returns:
            True if successful, False otherwise
        """
        try:
            filename = self._obfuscate_filename(key)
            file_path = self._get_full_path(category, filename)
            
            if file_path.exists():
                # Securely delete file (overwrite with random data)
                file_size = file_path.stat().st_size
                with open(file_path, 'wb') as f:
                    f.write(os.urandom(file_size))
                
                # Delete file
                file_path.unlink()
                return True
            
            return False
        
        except Exception as e:
            print(f"Error deleting data: {e}")
            return False
    
    def list_keys(self, category: str) -> list:
        """
        List all keys in a category
        
        Args:
            category: Storage category
            
        Returns:
            List of keys
        """
        try:
            dir_path = config.HIDDEN_DIRS[category]
            keys = []
            
            for file_path in dir_path.glob('*.enc'):
                try:
                    with open(file_path, 'rb') as f:
                        # Skip salt
                        f.read(config.SALT_SIZE)
                        # Read metadata length
                        metadata_len = int.from_bytes(f.read(4), byteorder='big')
                        # Read metadata
                        metadata_bytes = f.read(metadata_len)
                        metadata = json.loads(metadata_bytes.decode('utf-8'))
                        keys.append(metadata['key'])
                except:
                    continue
            
            return keys
        
        except Exception as e:
            print(f"Error listing keys: {e}")
            return []
    
    def store_model(self, category: str, model_name: str, model_obj: Any) -> bool:
        """
        Store a machine learning model
        
        Args:
            category: Storage category
            model_name: Model identifier
            model_obj: Model object to store
            
        Returns:
            True if successful, False otherwise
        """
        return self.store_data(category, model_name, model_obj, use_pickle=True)
    
    def retrieve_model(self, category: str, model_name: str) -> Optional[Any]:
        """
        Retrieve a machine learning model
        
        Args:
            category: Storage category
            model_name: Model identifier
            
        Returns:
            Model object or None if not found
        """
        return self.retrieve_data(category, model_name)
    
    def clear_cache(self):
        """Clear any cached data (for security)"""
        self.encryption_manager._cipher_cache.clear()
    
    def secure_wipe(self):
        """
        Securely wipe all hidden storage
        WARNING: This will delete all stored data!
        """
        try:
            if self.base_dir.exists():
                # Overwrite all files before deletion
                for file_path in self.base_dir.rglob('*'):
                    if file_path.is_file():
                        file_size = file_path.stat().st_size
                        with open(file_path, 'wb') as f:
                            f.write(os.urandom(file_size))
                
                # Delete directory tree
                shutil.rmtree(self.base_dir)
            
            return True
        
        except Exception as e:
            print(f"Error during secure wipe: {e}")
            return False
