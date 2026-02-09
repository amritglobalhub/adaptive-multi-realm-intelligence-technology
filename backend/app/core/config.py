"""
AMRIT AI - Core Configuration Module
Handles all configuration settings for the system
"""
import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings"""
    
    # Server Configuration
    host: str = Field(default="0.0.0.0", env="HOST")
    port: int = Field(default=8000, env="PORT")
    debug: bool = Field(default=True, env="DEBUG")
    
    # Database
    database_url: str = Field(default="sqlite:///./amrit.db", env="DATABASE_URL")
    
    # Redis
    redis_url: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    
    # Security
    secret_key: str = Field(default="change-this-secret-key", env="SECRET_KEY")
    algorithm: str = Field(default="HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    encryption_key: str = Field(default="change-this-encryption-key", env="ENCRYPTION_KEY")
    
    # Master/Owner Configuration
    master_name: str = Field(default="Amrit Gupta", env="MASTER_NAME")
    master_birth_date: str = Field(default="06/11/2000", env="MASTER_BIRTH_DATE")
    master_birth_time: str = Field(default="18:00", env="MASTER_BIRTH_TIME")
    master_birth_place: str = Field(default="New Delhi", env="MASTER_BIRTH_PLACE")
    
    # OpenAI
    openai_api_key: Optional[str] = Field(default=None, env="OPENAI_API_KEY")
    
    # Voice Settings
    voice_sample_rate: int = Field(default=16000, env="VOICE_SAMPLE_RATE")
    voice_min_duration: float = Field(default=1.0, env="VOICE_MIN_DURATION")
    voice_max_duration: float = Field(default=300.0, env="VOICE_MAX_DURATION")
    
    # Image Generation
    stable_diffusion_model: str = Field(
        default="stabilityai/stable-diffusion-2-1", 
        env="STABLE_DIFFUSION_MODEL"
    )
    
    # Security
    max_login_attempts: int = Field(default=5, env="MAX_LOGIN_ATTEMPTS")
    session_timeout: int = Field(default=3600, env="SESSION_TIMEOUT")
    ip_whitelist_enabled: bool = Field(default=False, env="IP_WHITELIST_ENABLED")
    
    # Analytics
    enable_tracking: bool = Field(default=True, env="ENABLE_TRACKING")
    enable_environmental_data: bool = Field(default=True, env="ENABLE_ENVIRONMENTAL_DATA")
    
    # Link Generation
    link_expiry_days: int = Field(default=7, env="LINK_EXPIRY_DAYS")
    base_url: str = Field(default="http://localhost:8000", env="BASE_URL")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()
