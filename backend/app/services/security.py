"""
AMRIT AI - Security Service
Encryption, authentication, and security utilities
"""
import jwt
from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from cryptography.fernet import Fernet
from backend.app.core.config import settings

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class SecurityService:
    """Security service for encryption and authentication"""
    
    def __init__(self):
        # Initialize encryption (use settings key or generate)
        try:
            self.cipher = Fernet(settings.encryption_key.encode())
        except:
            # Generate a key if not valid
            self.cipher = Fernet(Fernet.generate_key())
    
    def hash_password(self, password: str) -> str:
        """Hash a password"""
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against a hash"""
        return pwd_context.verify(plain_password, hashed_password)
    
    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """Create JWT access token"""
        to_encode = data.copy()
        
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
        
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
        return encoded_jwt
    
    def decode_token(self, token: str) -> dict:
        """Decode JWT token"""
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.JWTError:
            raise ValueError("Invalid token")
    
    def encrypt_data(self, data: bytes) -> bytes:
        """Encrypt data using Fernet"""
        return self.cipher.encrypt(data)
    
    def decrypt_data(self, encrypted_data: bytes) -> bytes:
        """Decrypt data using Fernet"""
        return self.cipher.decrypt(encrypted_data)
    
    def encrypt_text(self, text: str) -> str:
        """Encrypt text string"""
        return self.cipher.encrypt(text.encode()).decode()
    
    def decrypt_text(self, encrypted_text: str) -> str:
        """Decrypt text string"""
        return self.cipher.decrypt(encrypted_text.encode()).decode()


# Global instance
security_service = SecurityService()
