"""
Test configuration and fixtures
"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.models.database import Base


@pytest.fixture
def test_db():
    """Create test database"""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
