#!/usr/bin/env python
"""
AMRIT AI - Startup Script
Run the FastAPI server with proper module path
"""
import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Import and run
from backend.app.main import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
