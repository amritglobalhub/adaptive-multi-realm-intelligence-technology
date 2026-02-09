#!/usr/bin/env python
"""
AMRIT AI - Database Initialization Script
Creates the database and initializes with master user
"""
import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from backend.app.core.database import init_db, SessionLocal
from backend.app.core.config import settings
from backend.app.models.database import User, NumerologyAnalysis
from backend.app.services.numerology import numerology_service
from backend.app.services.security import security_service
from datetime import datetime


def initialize_database():
    """Initialize database and create master user"""
    print("🌟 AMRIT AI - Database Initialization")
    print("=" * 80)
    
    # Create tables
    print("\n1. Creating database tables...")
    init_db()
    print("   ✓ Tables created successfully")
    
    # Create session
    db = SessionLocal()
    
    try:
        # Check if master user already exists
        existing_master = db.query(User).filter(User.is_master == True).first()
        
        if existing_master:
            print(f"\n⚠️  Master user already exists: {existing_master.name}")
            print(f"   Email: {existing_master.email}")
            return
        
        # Calculate master numerology
        print("\n2. Calculating master numerology...")
        master_numbers = numerology_service.calculate_all_numbers(
            settings.master_birth_date,
            settings.master_name
        )
        print(f"   ✓ Numerology calculated for {settings.master_name}")
        print(f"   Life Path: {master_numbers['life_path']}")
        print(f"   Destiny: {master_numbers['destiny']}")
        
        # Create master user
        print("\n3. Creating master user...")
        master_user = User(
            name=settings.master_name,
            email="master@amrit-ai.local",  # Default email
            is_master=True,
            birth_date=settings.master_birth_date,
            birth_time=settings.master_birth_time,
            birth_place=settings.master_birth_place,
            numerology_numbers=master_numbers,
            hashed_password=security_service.hash_password("change-this-password"),  # Default password
            is_active=True,
            created_at=datetime.utcnow()
        )
        
        db.add(master_user)
        db.commit()
        db.refresh(master_user)
        
        print(f"   ✓ Master user created with ID: {master_user.id}")
        
        # Create initial numerology analysis
        print("\n4. Creating initial numerology analysis...")
        guidance = numerology_service.generate_daily_guidance(master_numbers)
        lucky_times = numerology_service.get_lucky_times(master_numbers)
        
        analysis = NumerologyAnalysis(
            user_id=master_user.id,
            life_path=master_numbers['life_path'],
            destiny=master_numbers['destiny'],
            soul_urge=master_numbers['soul_urge'],
            personality=master_numbers['personality'],
            maturity=master_numbers['maturity'],
            personal_year=master_numbers['personal_year'],
            personal_month=master_numbers['personal_month'],
            personal_day=master_numbers['personal_day'],
            compatibility_score=100.0,  # Master is 100% compatible with self
            risk_level="very_low",
            daily_guidance=guidance,
            lucky_times=lucky_times
        )
        
        db.add(analysis)
        db.commit()
        
        print(f"   ✓ Initial analysis created")
        
        print("\n" + "=" * 80)
        print("✅ Database initialization complete!")
        print()
        print("Master User Details:")
        print(f"  Name: {master_user.name}")
        print(f"  Email: {master_user.email}")
        print(f"  Birth Date: {master_user.birth_date}")
        print(f"  Default Password: change-this-password")
        print()
        print("⚠️  IMPORTANT: Change the default password before deploying!")
        print()
        
    except Exception as e:
        print(f"\n❌ Error during initialization: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    initialize_database()
