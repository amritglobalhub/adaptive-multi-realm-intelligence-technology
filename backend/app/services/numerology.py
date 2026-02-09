"""
AMRIT AI - Enhanced Numerology Service
Complete numerology calculation engine with all 9 number types
"""
from datetime import datetime
from typing import Dict, Tuple
import re


class NumerologyService:
    """Enhanced numerology service for comprehensive analysis"""
    
    # Numerology interpretations
    INTERPRETATIONS = {
        1: {"trait": "Leadership and independence", "element": "Fire", "color": "Red"},
        2: {"trait": "Cooperation and diplomacy", "element": "Water", "color": "Orange"},
        3: {"trait": "Creativity and self-expression", "element": "Fire", "color": "Yellow"},
        4: {"trait": "Stability and order", "element": "Earth", "color": "Green"},
        5: {"trait": "Freedom and adventure", "element": "Air", "color": "Blue"},
        6: {"trait": "Nurturing and responsibility", "element": "Earth", "color": "Indigo"},
        7: {"trait": "Spirituality and introspection", "element": "Water", "color": "Violet"},
        8: {"trait": "Power and material success", "element": "Earth", "color": "Pink"},
        9: {"trait": "Compassion and humanitarianism", "element": "Fire", "color": "Gold"}
    }
    
    # Master numbers (not reduced)
    MASTER_NUMBERS = [11, 22, 33]
    
    @staticmethod
    def reduce_to_single_digit(number: int, allow_master: bool = True) -> int:
        """Reduce a number to single digit (or master number)"""
        while number > 9:
            if allow_master and number in NumerologyService.MASTER_NUMBERS:
                return number
            number = sum(int(digit) for digit in str(number))
        return number
    
    @staticmethod
    def calculate_from_date(date_str: str) -> int:
        """Calculate number from date string (DD/MM/YYYY or MM/DD/YYYY)"""
        # Remove any non-numeric characters except /
        date_str = re.sub(r'[^\d/]', '', date_str)
        parts = date_str.split('/')
        
        if len(parts) != 3:
            raise ValueError("Invalid date format. Use DD/MM/YYYY or MM/DD/YYYY")
        
        # Convert to integers and sum
        total = sum(int(part) for part in parts)
        return NumerologyService.reduce_to_single_digit(total)
    
    @staticmethod
    def calculate_from_name(name: str) -> int:
        """Calculate number from name using Pythagorean system"""
        # Pythagorean numerology chart
        chart = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
            'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
            'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
        }
        
        # Remove non-alphabetic characters and convert to uppercase
        clean_name = re.sub(r'[^A-Za-z]', '', name.upper())
        
        # Calculate sum
        total = sum(chart.get(char, 0) for char in clean_name)
        return NumerologyService.reduce_to_single_digit(total)
    
    @staticmethod
    def get_vowels_consonants(name: str) -> Tuple[str, str]:
        """Separate vowels and consonants from name"""
        vowels = "AEIOU"
        clean_name = re.sub(r'[^A-Za-z]', '', name.upper())
        
        vowel_chars = ''.join([c for c in clean_name if c in vowels])
        consonant_chars = ''.join([c for c in clean_name if c not in vowels])
        
        return vowel_chars, consonant_chars
    
    def life_path_number(self, birth_date: str) -> int:
        """
        Life Path Number - Most important number
        Calculated from birth date
        """
        return self.calculate_from_date(birth_date)
    
    def destiny_number(self, full_name: str) -> int:
        """
        Destiny Number (Expression Number)
        Calculated from full birth name
        """
        return self.calculate_from_name(full_name)
    
    def soul_urge_number(self, full_name: str) -> int:
        """
        Soul Urge Number (Heart's Desire)
        Calculated from vowels in full name
        """
        vowels, _ = self.get_vowels_consonants(full_name)
        return self.calculate_from_name(vowels)
    
    def personality_number(self, full_name: str) -> int:
        """
        Personality Number
        Calculated from consonants in full name
        """
        _, consonants = self.get_vowels_consonants(full_name)
        return self.calculate_from_name(consonants)
    
    def maturity_number(self, birth_date: str, full_name: str) -> int:
        """
        Maturity Number
        Sum of Life Path and Destiny numbers
        """
        life_path = self.life_path_number(birth_date)
        destiny = self.destiny_number(full_name)
        return self.reduce_to_single_digit(life_path + destiny)
    
    def personal_year_number(self, birth_date: str, target_year: int = None) -> int:
        """
        Personal Year Number
        Changes each year
        """
        if target_year is None:
            target_year = datetime.now().year
        
        # Extract month and day from birth date
        parts = birth_date.split('/')
        month = int(parts[1]) if len(parts) == 3 else int(parts[0])
        day = int(parts[0]) if len(parts) == 3 else int(parts[1])
        
        total = month + day + target_year
        return self.reduce_to_single_digit(total)
    
    def personal_month_number(self, birth_date: str, target_month: int = None, target_year: int = None) -> int:
        """
        Personal Month Number
        Changes each month
        """
        if target_month is None:
            target_month = datetime.now().month
        if target_year is None:
            target_year = datetime.now().year
        
        personal_year = self.personal_year_number(birth_date, target_year)
        return self.reduce_to_single_digit(personal_year + target_month)
    
    def personal_day_number(self, birth_date: str, target_date: datetime = None) -> int:
        """
        Personal Day Number
        Changes each day
        """
        if target_date is None:
            target_date = datetime.now()
        
        personal_month = self.personal_month_number(
            birth_date, 
            target_date.month, 
            target_date.year
        )
        return self.reduce_to_single_digit(personal_month + target_date.day)
    
    def calculate_all_numbers(self, birth_date: str, full_name: str) -> Dict:
        """
        Calculate all numerology numbers for a person
        """
        now = datetime.now()
        
        return {
            "life_path": self.life_path_number(birth_date),
            "destiny": self.destiny_number(full_name),
            "soul_urge": self.soul_urge_number(full_name),
            "personality": self.personality_number(full_name),
            "maturity": self.maturity_number(birth_date, full_name),
            "personal_year": self.personal_year_number(birth_date, now.year),
            "personal_month": self.personal_month_number(birth_date, now.month, now.year),
            "personal_day": self.personal_day_number(birth_date, now),
            "interpretations": {
                "life_path": self.INTERPRETATIONS.get(self.life_path_number(birth_date), {}),
                "destiny": self.INTERPRETATIONS.get(self.destiny_number(full_name), {}),
            }
        }
    
    def calculate_compatibility(self, person1_numbers: Dict, person2_numbers: Dict) -> float:
        """
        Calculate compatibility score between two people (0-100)
        Based on life path, destiny, and soul urge numbers
        """
        # Key numbers for compatibility
        key_numbers = ["life_path", "destiny", "soul_urge"]
        
        matches = 0
        total_comparisons = 0
        
        for key in key_numbers:
            if key in person1_numbers and key in person2_numbers:
                num1 = person1_numbers[key]
                num2 = person2_numbers[key]
                
                # Perfect match
                if num1 == num2:
                    matches += 3
                # Compatible numbers (differ by 2 or complementary)
                elif abs(num1 - num2) in [2, 5]:
                    matches += 2
                # Neutral
                elif abs(num1 - num2) in [1, 3, 4]:
                    matches += 1
                
                total_comparisons += 3
        
        # Calculate percentage
        if total_comparisons == 0:
            return 50.0
        
        return (matches / total_comparisons) * 100
    
    def assess_risk_level(self, user_numbers: Dict, master_numbers: Dict) -> str:
        """
        Assess risk level based on compatibility with master
        """
        compatibility = self.calculate_compatibility(user_numbers, master_numbers)
        
        if compatibility >= 80:
            return "very_low"
        elif compatibility >= 60:
            return "low"
        elif compatibility >= 40:
            return "medium"
        elif compatibility >= 20:
            return "high"
        else:
            return "very_high"
    
    def generate_daily_guidance(self, numbers: Dict) -> str:
        """
        Generate daily guidance based on personal day number
        """
        personal_day = numbers.get("personal_day", 1)
        
        guidance = {
            1: "Today is perfect for new beginnings. Take initiative and lead with confidence.",
            2: "Focus on partnerships and cooperation. Listen to others and find balance.",
            3: "Express yourself creatively. Communication and social activities are favored.",
            4: "Build solid foundations. Focus on practical matters and organization.",
            5: "Embrace change and adventure. Be flexible and open to new experiences.",
            6: "Nurture relationships and take responsibility. Help others and create harmony.",
            7: "Seek knowledge and inner wisdom. Reflect, meditate, and trust your intuition.",
            8: "Focus on achievement and material success. Make important business decisions.",
            9: "Complete projects and let go of what no longer serves you. Be compassionate."
        }
        
        return guidance.get(personal_day, "Trust your inner guidance today.")
    
    def get_lucky_times(self, numbers: Dict) -> Dict:
        """
        Calculate lucky times based on numerology
        """
        life_path = numbers.get("life_path", 1)
        personal_day = numbers.get("personal_day", 1)
        
        # Lucky hours (simplified - based on numbers)
        lucky_hours = [(life_path + i) % 24 for i in range(3)]
        lucky_days = [1, 9, 10, 18, 19, 27, 28]  # Days aligned with certain numbers
        
        return {
            "lucky_hours": lucky_hours,
            "lucky_days": lucky_days,
            "power_number": life_path
        }


# Global instance
numerology_service = NumerologyService()
