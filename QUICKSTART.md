# 🚀 AMRIT AI - Quick Start Guide

This guide will help you get AMRIT AI up and running in minutes.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 5 minutes of your time

## Step 1: Clone the Repository

```bash
git clone https://github.com/amritglobalhub/adaptive-multi-realm-intelligence-technology.git
cd adaptive-multi-realm-intelligence-technology
```

## Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv

# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** The full installation includes ML/AI libraries which may take several minutes. For a quick demo, you can install just the essentials:

```bash
pip install fastapi uvicorn sqlalchemy pydantic-settings cryptography PyJWT passlib pytest
```

## Step 4: Configure Environment (Optional)

```bash
cp .env.example .env
# Edit .env to customize settings
```

Default settings work fine for local development.

## Step 5: Initialize Database

```bash
python init_db.py
```

This creates the SQLite database and sets up the master user (Amrit Gupta).

## Step 6: Try the Demonstrations

### A. Numerology Demonstration

```bash
python demo.py
```

Shows complete numerology analysis and compatibility testing.

### B. Legacy Numerology Core

```bash
python numerology_core.py
```

Backward-compatible version using the enhanced system.

## Step 7: Start the API Server

```bash
python run_server.py
```

The server will start at `http://localhost:8000`

## Step 8: Explore the API

Open your browser and visit:

- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## Quick API Tests

### Test Numerology Calculation

```bash
curl -X POST "http://localhost:8000/api/numerology" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "birth_date=06/11/2000&full_name=Amrit Gupta"
```

### Test Compatibility Check

```bash
curl -X POST "http://localhost:8000/api/numerology/compatibility" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "user1_birth_date=06/11/2000&user1_name=Amrit Gupta&user2_birth_date=15/08/1995&user2_name=John Doe"
```

### Create Dynamic Link

```bash
curl -X POST "http://localhost:8000/api/create-link" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "access_level=guest&expires_in_days=7"
```

### Get Analytics

```bash
curl "http://localhost:8000/api/analytics?days=7"
```

## Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest backend/tests/test_numerology.py
```

## Project Structure

```
adaptive-multi-realm-intelligence-technology/
├── backend/              # Backend application
│   ├── app/
│   │   ├── api/         # API endpoints
│   │   ├── core/        # Configuration & database
│   │   ├── models/      # Database models
│   │   ├── services/    # Business logic
│   │   └── utils/       # Utilities
│   └── tests/           # Test suite
├── demo.py              # Demonstration script
├── init_db.py           # Database initialization
├── run_server.py        # Server startup script
├── numerology_core.py   # Legacy numerology module
└── requirements.txt     # Python dependencies
```

## Master User Credentials

After initialization:
- **Email**: master@amrit-ai.local
- **Password**: change-this-password (⚠️ Change this!)

## Key Features to Explore

1. **Numerology Analysis**: Calculate all 9 numerology numbers
2. **Compatibility Testing**: Check relationship compatibility
3. **User Tracking**: Log and analyze user activities
4. **Dynamic Links**: Generate device onboarding links
5. **Task Scheduling**: Schedule tasks for later execution
6. **Analytics**: View comprehensive user analytics
7. **Daily Reports**: Get daily activity summaries

## What's Implemented

✅ Core Architecture
✅ Enhanced Numerology Engine (9 numbers)
✅ REST API with 10+ endpoints
✅ Database Models (SQLAlchemy)
✅ Security Layer (JWT, Encryption)
✅ Activity Logging
✅ Analytics System
✅ Test Suite

## What's Coming Next

🔄 Voice Recognition System
🔄 Image Generation (AI)
🔄 Web Dashboard (React)
🔄 Mobile App (React Native)
🔄 Real-time WebSocket
🔄 Biometric Authentication
🔄 Environmental Sensors

## Troubleshooting

### Import Errors

If you get import errors, make sure you're in the project root directory and the virtual environment is activated.

### Database Locked

If you get "database is locked" errors, close any other processes accessing the database.

### Port Already in Use

If port 8000 is in use, edit `run_server.py` to use a different port:

```python
uvicorn.run(app, host="0.0.0.0", port=8001)  # Change to 8001 or any available port
```

## Getting Help

- Check the main README.md for detailed documentation
- Open an issue on GitHub
- Review the API documentation at /docs

## Next Steps

1. Explore the API documentation
2. Try different numerology combinations
3. Check the code in `backend/app/services/numerology.py`
4. Review database models in `backend/app/models/database.py`
5. Experiment with the API endpoints

---

**Built with ❤️ for Amrit Gupta's AMRIT AI Ecosystem**
