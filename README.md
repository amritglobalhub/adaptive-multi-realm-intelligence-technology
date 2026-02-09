# 🌟 AMRIT AI - Complete Intelligent Ecosystem

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

AMRIT AI is a comprehensive AI-powered intelligent ecosystem that combines cutting-edge technology with mystical numerology for personalized user experiences. The system operates on local networks and the internet, offering voice control, biometric authentication, and advanced analytics.

## 🎯 Key Features

### Core Capabilities
- **Voice Control System**: Natural language voice commands with biometric verification
- **Numerology Integration**: Complete 9-number numerology analysis and compatibility matching
- **Multi-Device Support**: Seamless synchronization across desktop, mobile, and web
- **Advanced Analytics**: Comprehensive user tracking with location mapping
- **Dynamic Link Generation**: Easy device onboarding with self-installing links
- **Biometric Security**: Face and voice authentication
- **AI Content Generation**: Images and text based on numerology
- **Task Scheduling**: Voice and API-based task automation
- **Environmental Monitoring**: Temperature, humidity, and location tracking

### Security Features
- AES-256 encryption for all sensitive data
- JWT token-based authentication
- Biometric verification (Face ID, Voice)
- IP tracking and access control
- Activity logging and audit trail
- Automatic session management

## 🏗️ Architecture

### Project Structure
```
adaptive-multi-realm-intelligence-technology/
├── backend/
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   ├── core/         # Core configuration and database
│   │   ├── models/       # Database models
│   │   ├── services/     # Business logic services
│   │   └── utils/        # Utility functions
│   └── tests/            # Test suite
├── frontend/             # React web application
├── mobile/               # React Native mobile app
├── shared/               # Shared utilities
├── docs/                 # Documentation
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
└── numerology_core.py    # Legacy numerology module
```

### Technology Stack

**Backend:**
- FastAPI (Web framework)
- SQLAlchemy (ORM)
- Redis (Caching)
- Celery (Task scheduling)
- PyTorch (ML models)
- OpenAI API (Text generation)
- Stable Diffusion (Image generation)

**Security:**
- Cryptography (AES-256)
- JWT tokens
- Passlib (Password hashing)
- OAuth2

**AI/ML:**
- Voice recognition (Librosa, WebRTC)
- Biometric processing
- Custom numerology algorithms

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip
- Redis (optional, for caching)
- PostgreSQL (optional, SQLite used by default)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/amritglobalhub/adaptive-multi-realm-intelligence-technology.git
cd adaptive-multi-realm-intelligence-technology
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Initialize database**
```bash
python -c "from backend.app.core.database import init_db; init_db()"
```

6. **Run the server**
```bash
python backend/app/main.py
```

The API will be available at `http://localhost:8000`

### API Documentation
Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📡 API Endpoints

### Numerology
- `POST /api/numerology` - Calculate complete numerology analysis
- `POST /api/numerology/compatibility` - Check compatibility between two people

### User Management
- `POST /api/user-entry` - Log user entry with tracking

### Voice System
- `POST /api/voice-command` - Process voice commands
- `POST /api/verify-biometric` - Verify voice/face biometrics

### Content Generation
- `POST /api/generate-image` - Generate AI images (numerology-based)

### Analytics
- `GET /api/analytics` - Get user analytics
- `GET /api/daily-report` - Get daily activity report
- `GET /api/map-location` - Get user location map

### Task Management
- `POST /api/schedule-task` - Schedule task for execution

### Link Generation
- `POST /api/create-link` - Generate dynamic onboarding link

## 🔢 Numerology System

The AMRIT AI numerology engine calculates 9 essential numbers:

1. **Life Path Number** - Core personality and life direction
2. **Destiny Number** - Life purpose and goals
3. **Soul Urge Number** - Inner desires and motivations
4. **Personality Number** - External persona
5. **Maturity Number** - Later life development
6. **Personal Year** - Current year's theme
7. **Personal Month** - Current month's focus
8. **Personal Day** - Daily guidance
9. **Expression Number** - Natural talents

### Example Usage

```python
from backend.app.services.numerology import numerology_service

# Calculate all numbers
numbers = numerology_service.calculate_all_numbers(
    birth_date="06/11/2000",
    full_name="Amrit Gupta"
)

# Check compatibility
compatibility = numerology_service.calculate_compatibility(
    person1_numbers,
    person2_numbers
)

# Get daily guidance
guidance = numerology_service.generate_daily_guidance(numbers)
```

## 🔐 Security Configuration

### Master/Owner Setup
Configure the master user in `.env`:
```env
MASTER_NAME=Amrit Gupta
MASTER_BIRTH_DATE=06/11/2000
MASTER_BIRTH_TIME=18:00
MASTER_BIRTH_PLACE=New Delhi
```

### Encryption Keys
Generate secure keys:
```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

## 📊 Database Schema

### Main Tables
- **users** - User accounts and profiles
- **voice_samples** - Voice biometric data
- **projects** - Project management
- **activity_logs** - Comprehensive activity tracking
- **numerology_analyses** - Numerology calculations
- **environmental_data** - Environmental sensors
- **generated_content** - AI-generated images/text
- **dynamic_links** - Device onboarding links
- **scheduled_tasks** - Task scheduling

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=backend

# Run specific test file
pytest backend/tests/test_numerology.py
```

## 📈 Development Roadmap

### Phase 1: Foundation ✅
- [x] Project structure
- [x] Core numerology engine
- [x] Database models
- [x] Basic API endpoints
- [x] Security layer

### Phase 2: Voice System (In Progress)
- [ ] Voice recognition integration
- [ ] Noise filtering
- [ ] Biometric voice analysis
- [ ] Command execution engine

### Phase 3: Web Platform
- [ ] React dashboard
- [ ] User analytics UI
- [ ] Voice control interface
- [ ] Settings management

### Phase 4: Mobile App
- [ ] React Native implementation
- [ ] Camera integration
- [ ] Mobile keyboard
- [ ] Biometric access

### Phase 5: Advanced Features
- [ ] Image generation (Stable Diffusion)
- [ ] Real-time WebSocket
- [ ] Multi-device sync
- [ ] Environmental sensors

### Phase 6: Production
- [ ] Performance optimization
- [ ] Security audit
- [ ] Documentation completion
- [ ] Deployment setup

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines before submitting PRs.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Amrit Gupta**
- Birth Date: 06/11/2000
- Location: New Delhi

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- PyTorch for ML capabilities
- OpenAI for text generation APIs
- Stable Diffusion for image generation

## 📞 Support

For support, please open an issue on GitHub or contact the development team.

---

**Built with ❤️ using AI, Numerology, and cutting-edge technology**
