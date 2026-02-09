"""
Numerology Core System for Amrit Gupta
LEGACY MODULE - Now using enhanced AMRIT AI numerology system

This module is kept for backward compatibility.
New code should use: backend.app.services.numerology
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.app.services.numerology import numerology_service

# Constants
BIRTH_DATE = '06/11/2000'
BIRTH_TIME = '18:00'
BIRTH_PLACE = 'New Delhi'
FULL_NAME = 'Amrit Gupta'

# Calculate using enhanced numerology service
if __name__ == "__main__":
    print("=" * 80)
    print("AMRIT AI - Enhanced Numerology System")
    print("=" * 80)
    print()
    
    # Calculate all numbers
    numbers = numerology_service.calculate_all_numbers(BIRTH_DATE, FULL_NAME)
    
    # Display all numbers
    print(f"Master: {FULL_NAME}")
    print(f"Birth Date: {BIRTH_DATE}")
    print(f"Birth Time: {BIRTH_TIME}")
    print(f"Birth Place: {BIRTH_PLACE}")
    print()
    
    print("Complete Numerology Analysis:")
    print(f"  • Life Path Number: {numbers['life_path']}")
    print(f"    {numbers['interpretations']['life_path'].get('trait', 'N/A')}")
    
    print(f"  • Destiny Number: {numbers['destiny']}")
    print(f"    {numbers['interpretations']['destiny'].get('trait', 'N/A')}")
    
    print(f"  • Soul Urge Number: {numbers['soul_urge']}")
    print(f"  • Personality Number: {numbers['personality']}")
    print(f"  • Maturity Number: {numbers['maturity']}")
    print(f"  • Personal Year: {numbers['personal_year']}")
    print(f"  • Personal Month: {numbers['personal_month']}")
    print(f"  • Personal Day: {numbers['personal_day']}")
    
    print()
    print("Daily Guidance:")
    guidance = numerology_service.generate_daily_guidance(numbers)
    print(f"  {guidance}")
    
    print()
    print("Lucky Times:")
    lucky = numerology_service.get_lucky_times(numbers)
    print(f"  • Power Number: {lucky['power_number']}")
    print(f"  • Lucky Hours: {', '.join(map(str, lucky['lucky_hours']))}")
    
    print()
    print("=" * 80)
    print("✨ For complete API access, run: python run_server.py")
    print("=" * 80)
