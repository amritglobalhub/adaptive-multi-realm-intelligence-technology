"""
AMRIT AI - Encryption Module

Multi-layer encryption system for securing sensitive data.
Uses AES-256 encryption with PBKDF2 key derivation.
"""

import os
import hashlib
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from typing import Optional, Union
import config


class EncryptionManager:
    """Handles all encryption and decryption operations"""
    
    def __init__(self, master_password: Optional[str] = None):
        """
        Initialize encryption manager
        
        Args:
            master_password: Master password for encryption (optional)
        """
        self.master_password = master_password
        self._cipher_cache = {}
    
    def _derive_key(self, password: str, salt: bytes) -> bytes:
        """
        Derive encryption key from password using PBKDF2
        
        Args:
            password: Password string
            salt: Salt bytes
            
        Returns:
            Derived key bytes
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=config.ENCRYPTION_ITERATIONS,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
    
    def generate_salt(self) -> bytes:
        """Generate random salt"""
        return os.urandom(config.SALT_SIZE)
    
    def encrypt(self, data: Union[str, bytes], password: Optional[str] = None) -> tuple:
        """
        Encrypt data with AES-256
        
        Args:
            data: Data to encrypt (string or bytes)
            password: Optional password (uses master password if not provided)
            
        Returns:
            Tuple of (encrypted_data, salt)
        """
        if password is None:
            password = self.master_password
        
        if password is None:
            raise ValueError("No password provided for encryption")
        
        # Convert string to bytes if necessary
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Generate salt and derive key
        salt = self.generate_salt()
        key = self._derive_key(password, salt)
        
        # Encrypt data
        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(data)
        
        return encrypted_data, salt
    
    def decrypt(self, encrypted_data: bytes, salt: bytes, 
                password: Optional[str] = None) -> bytes:
        """
        Decrypt data with AES-256
        
        Args:
            encrypted_data: Encrypted data bytes
            salt: Salt used for encryption
            password: Optional password (uses master password if not provided)
            
        Returns:
            Decrypted data bytes
        """
        if password is None:
            password = self.master_password
        
        if password is None:
            raise ValueError("No password provided for decryption")
        
        # Derive key
        key = self._derive_key(password, salt)
        
        # Decrypt data
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data)
        
        return decrypted_data
    
    def encrypt_file(self, file_path: str, output_path: str, 
                     password: Optional[str] = None):
        """
        Encrypt a file
        
        Args:
            file_path: Path to input file
            output_path: Path to output encrypted file
            password: Optional password
        """
        with open(file_path, 'rb') as f:
            data = f.read()
        
        encrypted_data, salt = self.encrypt(data, password)
        
        # Write salt + encrypted data
        with open(output_path, 'wb') as f:
            f.write(salt)
            f.write(encrypted_data)
    
    def decrypt_file(self, encrypted_file_path: str, output_path: str,
                     password: Optional[str] = None):
        """
        Decrypt a file
        
        Args:
            encrypted_file_path: Path to encrypted file
            output_path: Path to output decrypted file
            password: Optional password
        """
        with open(encrypted_file_path, 'rb') as f:
            # Read salt (first SALT_SIZE bytes)
            salt = f.read(config.SALT_SIZE)
            # Read encrypted data (rest of file)
            encrypted_data = f.read()
        
        decrypted_data = self.decrypt(encrypted_data, salt, password)
        
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
    
    def hash_data(self, data: Union[str, bytes]) -> str:
        """
        Create SHA-256 hash of data
        
        Args:
            data: Data to hash
            
        Returns:
            Hexadecimal hash string
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        return hashlib.sha256(data).hexdigest()
    
    def verify_hash(self, data: Union[str, bytes], hash_value: str) -> bool:
        """
        Verify data against hash
        
        Args:
            data: Data to verify
            hash_value: Expected hash value
            
        Returns:
            True if hash matches, False otherwise
        """
        return self.hash_data(data) == hash_value
    
    def generate_encryption_key(self) -> bytes:
        """Generate random encryption key"""
        return Fernet.generate_key()
    
    def multi_layer_encrypt(self, data: Union[str, bytes], 
                           passwords: list) -> tuple:
        """
        Apply multiple layers of encryption
        
        Args:
            data: Data to encrypt
            passwords: List of passwords for each layer
            
        Returns:
            Tuple of (encrypted_data, salts_list)
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        encrypted = data
        salts = []
        
        for password in passwords:
            encrypted, salt = self.encrypt(encrypted, password)
            salts.append(salt)
        
        return encrypted, salts
    
    def multi_layer_decrypt(self, encrypted_data: bytes, 
                           salts: list, passwords: list) -> bytes:
        """
        Decrypt multiple layers of encryption
        
        Args:
            encrypted_data: Encrypted data
            salts: List of salts (in encryption order)
            passwords: List of passwords (in encryption order)
            
        Returns:
            Decrypted data bytes
        """
        decrypted = encrypted_data
        
        # Decrypt in reverse order
        for salt, password in zip(reversed(salts), reversed(passwords)):
            decrypted = self.decrypt(decrypted, salt, password)
        
        return decrypted


# Convenience functions
def encrypt_data(data: Union[str, bytes], password: str) -> tuple:
    """Quick encrypt function"""
    manager = EncryptionManager(password)
    return manager.encrypt(data)


def decrypt_data(encrypted_data: bytes, salt: bytes, password: str) -> bytes:
    """Quick decrypt function"""
    manager = EncryptionManager(password)
    return manager.decrypt(encrypted_data, salt)
