"""
AMRIT AI - Main FastAPI Application
Core API server with all endpoints
"""
from fastapi import FastAPI, Depends, HTTPException, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime, timedelta
import secrets

from backend.app.core.config import settings
from backend.app.core.database import get_db, init_db
from backend.app.models.database import (
    User, ActivityLog, NumerologyAnalysis, 
    GeneratedContent, DynamicLink, ScheduledTask
)
from backend.app.services.numerology import numerology_service
from backend.app.services.security import security_service

# Initialize FastAPI app
app = FastAPI(
    title="AMRIT AI - Complete Intelligent Ecosystem",
    description="AI system with voice, biometrics, numerology, and analytics",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Utility function to log activity
async def log_activity(
    db: Session,
    user_id: Optional[int],
    action: str,
    action_type: str,
    request: Request,
    details: dict = None
):
    """Log user activity"""
    activity = ActivityLog(
        user_id=user_id,
        action=action,
        action_type=action_type,
        details=details or {},
        ip_address=request.client.host,
        timestamp=datetime.utcnow()
    )
    db.add(activity)
    db.commit()


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_db()
    print(f"AMRIT AI Server started on {settings.host}:{settings.port}")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "AMRIT AI",
        "version": "1.0.0",
        "description": "Complete Intelligent Ecosystem",
        "status": "online"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}


# ============================================================================
# NUMEROLOGY ENDPOINTS
# ============================================================================

@app.post("/api/numerology")
async def calculate_numerology(
    birth_date: str,
    full_name: str,
    db: Session = Depends(get_db)
):
    """
    Calculate comprehensive numerology analysis
    
    Args:
        birth_date: Birth date in DD/MM/YYYY format
        full_name: Full birth name
    """
    try:
        # Calculate all numbers
        numbers = numerology_service.calculate_all_numbers(birth_date, full_name)
        
        # Get daily guidance
        guidance = numerology_service.generate_daily_guidance(numbers)
        
        # Get lucky times
        lucky_times = numerology_service.get_lucky_times(numbers)
        
        return {
            "success": True,
            "numbers": numbers,
            "daily_guidance": guidance,
            "lucky_times": lucky_times
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/numerology/compatibility")
async def check_compatibility(
    user1_birth_date: str,
    user1_name: str,
    user2_birth_date: str,
    user2_name: str
):
    """
    Check compatibility between two people
    """
    try:
        # Calculate numbers for both users
        user1_numbers = numerology_service.calculate_all_numbers(user1_birth_date, user1_name)
        user2_numbers = numerology_service.calculate_all_numbers(user2_birth_date, user2_name)
        
        # Calculate compatibility
        compatibility = numerology_service.calculate_compatibility(user1_numbers, user2_numbers)
        
        # Assess risk level
        risk_level = numerology_service.assess_risk_level(user2_numbers, user1_numbers)
        
        return {
            "success": True,
            "compatibility_score": compatibility,
            "risk_level": risk_level,
            "user1_numbers": user1_numbers,
            "user2_numbers": user2_numbers
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================================
# USER MANAGEMENT ENDPOINTS
# ============================================================================

@app.post("/api/user-entry")
async def log_user_entry(
    request: Request,
    name: Optional[str] = None,
    birth_date: Optional[str] = None,
    full_name: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Log user entry with comprehensive tracking
    
    Tracks: IP, location, device info, timestamp, numerology
    """
    try:
        # Get client info
        ip_address = request.client.host
        user_agent = request.headers.get("user-agent", "Unknown")
        
        # Calculate numerology if data provided
        numerology_data = None
        if birth_date and full_name:
            numerology_data = numerology_service.calculate_all_numbers(birth_date, full_name)
        
        # Log activity
        await log_activity(
            db=db,
            user_id=None,
            action="user_entry",
            action_type="entry",
            request=request,
            details={
                "name": name,
                "birth_date": birth_date,
                "user_agent": user_agent,
                "numerology": numerology_data
            }
        )
        
        return {
            "success": True,
            "message": "User entry logged",
            "ip_address": ip_address,
            "timestamp": datetime.utcnow().isoformat(),
            "numerology": numerology_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# VOICE COMMAND ENDPOINT
# ============================================================================

@app.post("/api/voice-command")
async def process_voice_command(
    request: Request,
    audio_file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Process voice command
    
    Future: Will integrate voice recognition and command execution
    """
    try:
        # Read audio file
        audio_data = await audio_file.read()
        
        # Log activity
        await log_activity(
            db=db,
            user_id=None,
            action="voice_command",
            action_type="voice",
            request=request,
            details={
                "filename": audio_file.filename,
                "content_type": audio_file.content_type,
                "size": len(audio_data)
            }
        )
        
        # TODO: Integrate voice recognition here
        # For now, return placeholder
        
        return {
            "success": True,
            "message": "Voice command received",
            "audio_size": len(audio_data),
            "note": "Voice recognition integration pending"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# DYNAMIC LINK GENERATION
# ============================================================================

@app.post("/api/create-link")
async def create_dynamic_link(
    access_level: str = "guest",
    expires_in_days: int = 7,
    max_uses: int = 1,
    db: Session = Depends(get_db)
):
    """
    Generate dynamic link for device onboarding
    """
    try:
        # Generate unique code
        link_code = secrets.token_urlsafe(16)
        full_url = f"{settings.base_url}/onboard/{link_code}"
        
        # Calculate expiry
        expires_at = datetime.utcnow() + timedelta(days=expires_in_days)
        
        # Create link record
        link = DynamicLink(
            link_code=link_code,
            full_url=full_url,
            access_level=access_level,
            expires_at=expires_at,
            max_uses=max_uses
        )
        
        db.add(link)
        db.commit()
        
        return {
            "success": True,
            "link_code": link_code,
            "full_url": full_url,
            "expires_at": expires_at.isoformat(),
            "max_uses": max_uses,
            "access_level": access_level
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# ANALYTICS ENDPOINT
# ============================================================================

@app.get("/api/analytics")
async def get_analytics(
    days: int = 7,
    db: Session = Depends(get_db)
):
    """
    Get user analytics for the specified time period
    """
    try:
        # Calculate date range
        start_date = datetime.utcnow() - timedelta(days=days)
        
        # Query activity logs
        activities = db.query(ActivityLog).filter(
            ActivityLog.timestamp >= start_date
        ).all()
        
        # Aggregate data
        total_activities = len(activities)
        unique_ips = len(set([a.ip_address for a in activities if a.ip_address]))
        action_types = {}
        
        for activity in activities:
            action_type = activity.action_type or "unknown"
            action_types[action_type] = action_types.get(action_type, 0) + 1
        
        return {
            "success": True,
            "period_days": days,
            "total_activities": total_activities,
            "unique_ips": unique_ips,
            "action_types": action_types,
            "start_date": start_date.isoformat(),
            "end_date": datetime.utcnow().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# SCHEDULE TASK ENDPOINT
# ============================================================================

@app.post("/api/schedule-task")
async def schedule_task(
    task_name: str,
    task_type: str,
    scheduled_time: str,  # ISO format datetime string
    task_data: dict = None,
    is_recurring: bool = False,
    recurrence_pattern: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Schedule a task for later execution
    """
    try:
        # Parse scheduled time
        scheduled_dt = datetime.fromisoformat(scheduled_time)
        
        # Create scheduled task
        task = ScheduledTask(
            task_name=task_name,
            task_type=task_type,
            task_data=task_data or {},
            scheduled_time=scheduled_dt,
            is_recurring=is_recurring,
            recurrence_pattern=recurrence_pattern
        )
        
        db.add(task)
        db.commit()
        
        return {
            "success": True,
            "task_id": task.id,
            "task_name": task_name,
            "scheduled_time": scheduled_dt.isoformat(),
            "status": "scheduled"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================================
# DAILY REPORT ENDPOINT
# ============================================================================

@app.get("/api/daily-report")
async def get_daily_report(
    date: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Get daily report for specified date (or today)
    """
    try:
        # Parse date or use today
        if date:
            report_date = datetime.fromisoformat(date).date()
        else:
            report_date = datetime.utcnow().date()
        
        # Query activities for the day
        start_time = datetime.combine(report_date, datetime.min.time())
        end_time = datetime.combine(report_date, datetime.max.time())
        
        activities = db.query(ActivityLog).filter(
            ActivityLog.timestamp >= start_time,
            ActivityLog.timestamp <= end_time
        ).all()
        
        # Aggregate data
        report = {
            "date": report_date.isoformat(),
            "total_activities": len(activities),
            "unique_users": len(set([a.user_id for a in activities if a.user_id])),
            "activities_by_type": {},
            "activities_by_hour": [0] * 24
        }
        
        for activity in activities:
            # Count by type
            action_type = activity.action_type or "unknown"
            report["activities_by_type"][action_type] = \
                report["activities_by_type"].get(action_type, 0) + 1
            
            # Count by hour
            hour = activity.timestamp.hour
            report["activities_by_hour"][hour] += 1
        
        return {
            "success": True,
            "report": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# IMAGE GENERATION ENDPOINT (Placeholder)
# ============================================================================

@app.post("/api/generate-image")
async def generate_image(
    prompt: str,
    numerology_based: bool = False,
    birth_date: Optional[str] = None,
    full_name: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Generate AI image (Placeholder - requires Stable Diffusion integration)
    """
    try:
        # If numerology-based, enhance prompt with numerology colors
        enhanced_prompt = prompt
        
        if numerology_based and birth_date and full_name:
            numbers = numerology_service.calculate_all_numbers(birth_date, full_name)
            life_path = numbers.get("life_path", 1)
            interpretation = numerology_service.INTERPRETATIONS.get(life_path, {})
            color = interpretation.get("color", "blue")
            enhanced_prompt = f"{prompt}, with {color} color theme"
        
        # TODO: Integrate Stable Diffusion here
        # For now, return placeholder
        
        return {
            "success": True,
            "message": "Image generation requested",
            "prompt": enhanced_prompt,
            "note": "Stable Diffusion integration pending"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# MAP LOCATION ENDPOINT (Placeholder)
# ============================================================================

@app.get("/api/map-location")
async def get_map_location(
    db: Session = Depends(get_db)
):
    """
    Get world map with user locations (Placeholder)
    """
    try:
        # Query all activity logs with location data
        activities = db.query(ActivityLog).filter(
            ActivityLog.location.isnot(None)
        ).limit(100).all()
        
        # Extract locations
        locations = []
        for activity in activities:
            if activity.location:
                locations.append({
                    "ip": activity.ip_address,
                    "location": activity.location,
                    "timestamp": activity.timestamp.isoformat()
                })
        
        return {
            "success": True,
            "total_locations": len(locations),
            "locations": locations,
            "note": "Location mapping requires GeoIP integration"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# BIOMETRIC VERIFICATION ENDPOINT (Placeholder)
# ============================================================================

@app.post("/api/verify-biometric")
async def verify_biometric(
    biometric_type: str,  # face, voice
    biometric_data: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Verify biometric data (Placeholder)
    """
    try:
        data = await biometric_data.read()
        
        # TODO: Implement biometric verification
        
        return {
            "success": True,
            "biometric_type": biometric_type,
            "verified": False,
            "note": "Biometric verification integration pending"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)
