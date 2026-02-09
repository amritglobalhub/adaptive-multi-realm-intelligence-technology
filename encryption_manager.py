"""
AMRIT AI Encryption Manager
Provides military-grade encryption for all user data
Ensures complete privacy and security
"""

import os
import json
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import hashlib
from typing import Any, Dict, Optional
import amrit_config as config


class EncryptionManager:
    """
    Military-grade encryption manager for AMRIT AI
    Handles all encryption/decryption operations
    """
    
    def __init__(self):
        self.encryption_key = None
        self.cipher_suite = None
        self._initialize_encryption()
    
    def _initialize_encryption(self):
        """Initialize encryption system with key generation or loading"""
        os.makedirs(config.DATA_DIR, exist_ok=True)
        
        if os.path.exists(config.ENCRYPTION_KEY_PATH):
            # Load existing key
            self.encryption_key = self._load_key()
        else:
            # Generate new key
            self.encryption_key = self._generate_key()
            self._save_key(self.encryption_key)
        
        self.cipher_suite = Fernet(self.encryption_key)
    
    def _generate_key(self) -> bytes:
        """Generate a new encryption key using secure random"""
        return Fernet.generate_key()
    
    def _save_key(self, key: bytes):
        """Save encryption key to secure location"""
        # Add extra layer of obfuscation
        obfuscated_key = base64.b85encode(key)
        
        with open(config.ENCRYPTION_KEY_PATH, 'wb') as key_file:
            key_file.write(obfuscated_key)
        
        # Set restrictive permissions (owner only)
        os.chmod(config.ENCRYPTION_KEY_PATH, 0o600)
    
    def _load_key(self) -> bytes:
        """Load encryption key from secure location"""
        with open(config.ENCRYPTION_KEY_PATH, 'rb') as key_file:
            obfuscated_key = key_file.read()
        
        return base64.b85decode(obfuscated_key)
    
    def encrypt_data(self, data: Any) -> bytes:
        """
        Encrypt any data type (converts to JSON first)
        
        Args:
            data: Any data to encrypt (dict, list, str, etc.)
        
        Returns:
            Encrypted bytes
        """
        if not config.DATA_ENCRYPTION_ENABLED:
            return json.dumps(data).encode()
        
        # Convert to JSON string
        json_data = json.dumps(data)
        
        # Encrypt
        encrypted_data = self.cipher_suite.encrypt(json_data.encode())
        
        return encrypted_data
    
    def decrypt_data(self, encrypted_data: bytes) -> Any:
        """
        Decrypt data and return original format
        
        Args:
            encrypted_data: Encrypted bytes
        
        Returns:
            Original data (dict, list, str, etc.)
        """
        if not config.DATA_ENCRYPTION_ENABLED:
            return json.loads(encrypted_data.decode())
        
        # Decrypt
        decrypted_bytes = self.cipher_suite.decrypt(encrypted_data)
        
        # Parse JSON
        data = json.loads(decrypted_bytes.decode())
        
        return data
    
    def encrypt_file(self, file_path: str, output_path: Optional[str] = None):
        """
        Encrypt an entire file
        
        Args:
            file_path: Path to file to encrypt
            output_path: Path for encrypted file (default: original + .encrypted)
        """
        if not output_path:
            output_path = file_path + '.encrypted'
        
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        encrypted_data = self.cipher_suite.encrypt(file_data)
        
        with open(output_path, 'wb') as f:
            f.write(encrypted_data)
        
        # Set restrictive permissions
        os.chmod(output_path, 0o600)
    
    def decrypt_file(self, encrypted_file_path: str, output_path: str):
        """
        Decrypt an encrypted file
        
        Args:
            encrypted_file_path: Path to encrypted file
            output_path: Path for decrypted file
        """
        with open(encrypted_file_path, 'rb') as f:
            encrypted_data = f.read()
        
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
    
    def hash_data(self, data: str) -> str:
        """
        Create secure hash of data (for identification, not encryption)
        
        Args:
            data: String data to hash
        
        Returns:
            Hex string of hash
        """
        return hashlib.sha256(data.encode()).hexdigest()
    
    def verify_hash(self, data: str, hash_value: str) -> bool:
        """
        Verify data against hash
        
        Args:
            data: Original data
            hash_value: Hash to verify against
        
        Returns:
            True if matches, False otherwise
        """
        return self.hash_data(data) == hash_value


# Global encryption manager instance
encryption_manager = EncryptionManager()
