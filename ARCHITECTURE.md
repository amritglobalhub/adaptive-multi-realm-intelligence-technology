# 🏗️ AMRIT AI - System Architecture

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        AMRIT AI ECOSYSTEM                           │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Client    │    │  Mobile Client  │    │   IoT Devices   │
│   (React)       │    │ (React Native)  │    │   (Sensors)     │
└────────┬────────┘    └────────┬────────┘    └────────┬────────┘
         │                      │                       │
         └──────────────────────┼───────────────────────┘
                                │
                        ┌───────▼───────┐
                        │   REST API    │
                        │   (FastAPI)   │
                        └───────┬───────┘
                                │
                ┌───────────────┼───────────────┐
                │               │               │
        ┌───────▼──────┐ ┌─────▼─────┐ ┌──────▼──────┐
        │  Numerology  │ │  Security │ │  Analytics  │
        │   Service    │ │  Service  │ │   Service   │
        └──────────────┘ └───────────┘ └─────────────┘
                                │
                        ┌───────▼───────┐
                        │   Database    │
                        │  (SQLite/     │
                        │  PostgreSQL)  │
                        └───────────────┘
```

## Backend Architecture (Implemented)

```
backend/
│
├── app/
│   ├── main.py                 # FastAPI Application
│   │   ├── 11 REST Endpoints
│   │   ├── CORS Middleware
│   │   ├── Activity Logging
│   │   └── Error Handling
│   │
│   ├── core/
│   │   ├── config.py           # Configuration Management
│   │   │   ├── Environment Variables
│   │   │   ├── Settings Class
│   │   │   └── Validation
│   │   │
│   │   └── database.py         # Database Connection
│   │       ├── Engine Creation
│   │       ├── Session Factory
│   │       └── DB Initialization
│   │
│   ├── models/
│   │   └── database.py         # SQLAlchemy Models
│   │       ├── User
│   │       ├── VoiceSample
│   │       ├── Project
│   │       ├── ActivityLog
│   │       ├── NumerologyAnalysis
│   │       ├── EnvironmentalData
│   │       ├── GeneratedContent
│   │       ├── DynamicLink
│   │       └── ScheduledTask
│   │
│   └── services/
│       ├── numerology.py       # Numerology Engine
│       │   ├── Calculate 9 Numbers
│       │   ├── Compatibility Scoring
│       │   ├── Risk Assessment
│       │   ├── Daily Guidance
│       │   └── Lucky Times
│       │
│       └── security.py         # Security Services
│           ├── Password Hashing
│           ├── JWT Tokens
│           ├── Data Encryption
│           └── Token Validation
│
└── tests/
    ├── conftest.py             # Test Configuration
    └── test_numerology.py      # Test Suite (12 tests)
```

## API Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    REST API ENDPOINTS                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  NUMEROLOGY                    USER MANAGEMENT              │
│  ├─ POST /api/numerology       ├─ POST /api/user-entry     │
│  └─ POST /api/numerology/      │                            │
│     compatibility              │                            │
│                                                              │
│  VOICE & BIOMETRIC            CONTENT GENERATION            │
│  ├─ POST /api/voice-command   ├─ POST /api/generate-image  │
│  └─ POST /api/verify-         │                             │
│     biometric                 │                             │
│                                                              │
│  ANALYTICS                    TASK MANAGEMENT               │
│  ├─ GET  /api/analytics       ├─ POST /api/schedule-task   │
│  ├─ GET  /api/daily-report    └─ POST /api/create-link     │
│  └─ GET  /api/map-location                                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Database Schema Architecture

```
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│    Users     │◄────────┤ VoiceSamples │         │   Projects   │
├──────────────┤         ├──────────────┤         ├──────────────┤
│ id (PK)      │         │ id (PK)      │         │ id (PK)      │
│ name         │         │ user_id (FK) │         │ owner_id (FK)│
│ email        │         │ audio_data   │         │ name         │
│ is_master    │         │ frequency    │         │ description  │
│ birth_date   │         │ tone         │         │ status       │
│ numerology   │         │ language     │         │ files        │
│ hashed_pwd   │         └──────────────┘         └──────────────┘
│ ip_address   │                │                        │
│ device_info  │                │                        │
└──────┬───────┘                │                        │
       │                        │                        │
       │         ┌──────────────┴──────────┐            │
       │         │                         │            │
       ├─────────▼──────────┐   ┌─────────▼────────────▼───┐
       │   ActivityLog      │   │  NumerologyAnalysis      │
       ├────────────────────┤   ├──────────────────────────┤
       │ id (PK)            │   │ id (PK)                  │
       │ user_id (FK)       │   │ user_id (FK)             │
       │ action             │   │ life_path                │
       │ action_type        │   │ destiny                  │
       │ ip_address         │   │ soul_urge                │
       │ location           │   │ personality              │
       │ timestamp          │   │ compatibility_score      │
       └────────────────────┘   │ risk_level               │
                               │ daily_guidance            │
                               └──────────────────────────┘

┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ GeneratedContent │    │  DynamicLink     │    │ ScheduledTask    │
├──────────────────┤    ├──────────────────┤    ├──────────────────┤
│ id (PK)          │    │ id (PK)          │    │ id (PK)          │
│ owner_id (FK)    │    │ link_code        │    │ user_id (FK)     │
│ content_type     │    │ full_url         │    │ task_name        │
│ content_data     │    │ access_level     │    │ scheduled_time   │
│ prompt           │    │ expires_at       │    │ is_recurring     │
│ numerology_based │    │ max_uses         │    │ status           │
└──────────────────┘    └──────────────────┘    └──────────────────┘

┌──────────────────┐
│ EnvironmentalData│
├──────────────────┤
│ id (PK)          │
│ location         │
│ temperature      │
│ humidity         │
│ air_quality      │
│ wind_speed       │
│ timestamp        │
└──────────────────┘
```

## Security Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    SECURITY LAYERS                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Layer 1: Transport Security                            │
│  └─ HTTPS/TLS (Production)                              │
│                                                          │
│  Layer 2: Authentication                                │
│  ├─ JWT Token Generation                                │
│  ├─ Token Validation                                    │
│  └─ Expiry Management                                   │
│                                                          │
│  Layer 3: Authorization                                 │
│  ├─ Role-Based Access Control                           │
│  ├─ Master User Privileges                              │
│  └─ Access Level Management                             │
│                                                          │
│  Layer 4: Data Protection                               │
│  ├─ Password Hashing (bcrypt)                           │
│  ├─ Data Encryption (AES-256)                           │
│  ├─ Voice Sample Encryption                             │
│  └─ Biometric Data Encryption                           │
│                                                          │
│  Layer 5: Activity Monitoring                           │
│  ├─ IP Tracking                                         │
│  ├─ Device Fingerprinting                               │
│  ├─ Activity Logging                                    │
│  └─ Audit Trail                                         │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## Numerology Service Architecture

```
┌────────────────────────────────────────────────────────┐
│           NUMEROLOGY SERVICE PIPELINE                   │
└────────────────────────────────────────────────────────┘

Input: Birth Date + Full Name
        │
        ▼
┌─────────────────────────────────┐
│   1. Basic Number Calculation   │
│   ├─ Life Path (from date)      │
│   ├─ Destiny (from name)        │
│   ├─ Soul Urge (from vowels)    │
│   └─ Personality (consonants)   │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│   2. Derived Calculations       │
│   ├─ Maturity Number            │
│   ├─ Personal Year              │
│   ├─ Personal Month             │
│   └─ Personal Day               │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│   3. Analysis Generation        │
│   ├─ Interpretations            │
│   ├─ Element & Color            │
│   ├─ Daily Guidance             │
│   └─ Lucky Times                │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│   4. Compatibility (Optional)   │
│   ├─ Score Calculation          │
│   ├─ Risk Assessment            │
│   └─ Recommendations            │
└────────────┬────────────────────┘
             │
             ▼
        Output: Complete Analysis
```

## Data Flow Architecture

```
┌───────────┐
│  Client   │
│  Request  │
└─────┬─────┘
      │
      │ HTTP Request
      ▼
┌─────────────────┐
│   FastAPI       │
│   Main App      │
└────────┬────────┘
         │
         ├──────────────┐
         │              │
         ▼              ▼
┌─────────────┐  ┌─────────────┐
│  Validate   │  │    Log      │
│  Request    │  │  Activity   │
└──────┬──────┘  └─────────────┘
       │
       ▼
┌─────────────┐
│  Service    │
│  Layer      │
└──────┬──────┘
       │
       ├──────────────┬──────────────┐
       │              │              │
       ▼              ▼              ▼
┌───────────┐  ┌───────────┐  ┌───────────┐
│Numerology │  │ Security  │  │ Database  │
│ Service   │  │ Service   │  │  Access   │
└─────┬─────┘  └─────┬─────┘  └─────┬─────┘
      │              │              │
      └──────────────┴──────────────┘
                     │
                     ▼
            ┌────────────────┐
            │  Build Response│
            └────────┬───────┘
                     │
                     ▼
            ┌────────────────┐
            │  HTTP Response │
            │  (JSON)        │
            └────────┬───────┘
                     │
                     ▼
            ┌────────────────┐
            │     Client     │
            └────────────────┘
```

## Deployment Architecture (Future)

```
┌─────────────────────────────────────────────────────────┐
│                    PRODUCTION DEPLOYMENT                 │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────┐        ┌────────────┐                  │
│  │   Nginx    │───────▶│  FastAPI   │                  │
│  │ (Reverse   │        │   Apps     │                  │
│  │  Proxy)    │        │ (Uvicorn)  │                  │
│  └────────────┘        └─────┬──────┘                  │
│                              │                          │
│                              ▼                          │
│                        ┌───────────┐                    │
│                        │PostgreSQL │                    │
│                        │ (Primary) │                    │
│                        └───────────┘                    │
│                              │                          │
│                              ▼                          │
│                        ┌───────────┐                    │
│                        │   Redis   │                    │
│                        │  (Cache)  │                    │
│                        └───────────┘                    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## Integration Points

```
┌─────────────────────────────────────────────────────────┐
│              THIRD-PARTY INTEGRATIONS                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Voice Recognition                                       │
│  └─ OpenAI Whisper / Google Speech-to-Text              │
│                                                          │
│  Image Generation                                        │
│  └─ Stable Diffusion / DALL-E                           │
│                                                          │
│  Text Generation                                         │
│  └─ OpenAI GPT / Anthropic Claude                       │
│                                                          │
│  Location Services                                       │
│  └─ MaxMind GeoIP / IP-API                              │
│                                                          │
│  Environmental Data                                      │
│  └─ IoT Sensors / Weather APIs                          │
│                                                          │
│  Biometric Recognition                                   │
│  └─ Face++ / AWS Rekognition                            │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## Scalability Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  HORIZONTAL SCALING                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│              ┌──────────────────┐                       │
│              │  Load Balancer   │                       │
│              └────────┬─────────┘                       │
│                       │                                  │
│        ┌──────────────┼──────────────┐                  │
│        │              │              │                  │
│   ┌────▼────┐    ┌────▼────┐   ┌────▼────┐            │
│   │ API     │    │ API     │   │ API     │            │
│   │ Server 1│    │ Server 2│   │ Server 3│            │
│   └────┬────┘    └────┬────┘   └────┬────┘            │
│        │              │              │                  │
│        └──────────────┼──────────────┘                  │
│                       │                                  │
│              ┌────────▼─────────┐                       │
│              │   Database       │                       │
│              │   Cluster        │                       │
│              └──────────────────┘                       │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

**Architecture Status**: ✅ Core Backend Implemented
**Next Phase**: Frontend & Integration Development
