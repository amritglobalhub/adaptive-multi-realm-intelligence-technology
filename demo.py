#!/usr/bin/env python
"""
AMRIT AI - Demonstration Script
Shows the numerology system and API capabilities
"""
import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from backend.app.services.numerology import numerology_service


def print_separator():
    print("\n" + "=" * 80 + "\n")


def demonstrate_numerology():
    """Demonstrate the numerology system"""
    print("🌟 AMRIT AI - Numerology System Demonstration")
    print_separator()
    
    # Master (Amrit Gupta) Analysis
    print("📊 MASTER ANALYSIS - Amrit Gupta")
    print("-" * 80)
    
    master_birth = "06/11/2000"
    master_name = "Amrit Gupta"
    
    master_numbers = numerology_service.calculate_all_numbers(master_birth, master_name)
    
    print(f"Birth Date: {master_birth}")
    print(f"Full Name: {master_name}")
    print()
    print("Numerology Numbers:")
    print(f"  • Life Path Number: {master_numbers['life_path']}")
    print(f"  • Destiny Number: {master_numbers['destiny']}")
    print(f"  • Soul Urge Number: {master_numbers['soul_urge']}")
    print(f"  • Personality Number: {master_numbers['personality']}")
    print(f"  • Maturity Number: {master_numbers['maturity']}")
    print(f"  • Personal Year: {master_numbers['personal_year']}")
    print(f"  • Personal Month: {master_numbers['personal_month']}")
    print(f"  • Personal Day: {master_numbers['personal_day']}")
    
    # Interpretations
    print()
    print("Interpretations:")
    life_path_interp = master_numbers['interpretations']['life_path']
    destiny_interp = master_numbers['interpretations']['destiny']
    print(f"  • Life Path: {life_path_interp.get('trait', 'N/A')}")
    print(f"    Element: {life_path_interp.get('element', 'N/A')}, Color: {life_path_interp.get('color', 'N/A')}")
    print(f"  • Destiny: {destiny_interp.get('trait', 'N/A')}")
    
    # Daily Guidance
    print()
    guidance = numerology_service.generate_daily_guidance(master_numbers)
    print(f"Daily Guidance: {guidance}")
    
    # Lucky Times
    lucky = numerology_service.get_lucky_times(master_numbers)
    print()
    print(f"Power Number: {lucky['power_number']}")
    print(f"Lucky Hours: {', '.join(map(str, lucky['lucky_hours']))}")
    
    print_separator()
    
    # Visitor Analysis
    print("👤 VISITOR ANALYSIS - John Doe")
    print("-" * 80)
    
    visitor_birth = "15/08/1995"
    visitor_name = "John Doe"
    
    visitor_numbers = numerology_service.calculate_all_numbers(visitor_birth, visitor_name)
    
    print(f"Birth Date: {visitor_birth}")
    print(f"Full Name: {visitor_name}")
    print()
    print("Numerology Numbers:")
    print(f"  • Life Path Number: {visitor_numbers['life_path']}")
    print(f"  • Destiny Number: {visitor_numbers['destiny']}")
    print(f"  • Soul Urge Number: {visitor_numbers['soul_urge']}")
    print(f"  • Personality Number: {visitor_numbers['personality']}")
    
    print_separator()
    
    # Compatibility Analysis
    print("🤝 COMPATIBILITY ANALYSIS")
    print("-" * 80)
    
    compatibility = numerology_service.calculate_compatibility(master_numbers, visitor_numbers)
    risk_level = numerology_service.assess_risk_level(visitor_numbers, master_numbers)
    
    print(f"Master: {master_name}")
    print(f"Visitor: {visitor_name}")
    print()
    print(f"Compatibility Score: {compatibility:.1f}%")
    print(f"Risk Level: {risk_level.upper().replace('_', ' ')}")
    print()
    
    # Interpretation
    if compatibility >= 80:
        print("✅ Excellent compatibility! Very harmonious relationship.")
    elif compatibility >= 60:
        print("👍 Good compatibility. Generally positive interactions.")
    elif compatibility >= 40:
        print("⚖️ Moderate compatibility. Some effort needed for harmony.")
    elif compatibility >= 20:
        print("⚠️ Low compatibility. Potential challenges in relationship.")
    else:
        print("❌ Poor compatibility. Significant differences to navigate.")
    
    print_separator()
    
    # API Information
    print("🚀 API ENDPOINTS AVAILABLE")
    print("-" * 80)
    print()
    print("Start the server with: python run_server.py")
    print()
    print("Then access:")
    print("  • API Documentation: http://localhost:8000/docs")
    print("  • Health Check: http://localhost:8000/health")
    print()
    print("Key Endpoints:")
    print("  POST /api/numerology - Calculate numerology analysis")
    print("  POST /api/numerology/compatibility - Check compatibility")
    print("  POST /api/user-entry - Log user entry")
    print("  POST /api/voice-command - Process voice commands")
    print("  GET  /api/analytics - Get analytics")
    print("  POST /api/create-link - Generate dynamic link")
    print("  POST /api/schedule-task - Schedule task")
    print("  GET  /api/daily-report - Get daily report")
    
    print_separator()
    
    print("✨ AMRIT AI - Your Complete Intelligent Ecosystem")
    print("   Voice • Biometrics • Numerology • Analytics • AI Generation")
    print()


if __name__ == "__main__":
    demonstrate_numerology()
