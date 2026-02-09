"""
Tests for AMRIT AI Numerology Service
"""
import pytest
from backend.app.services.numerology import numerology_service


class TestNumerologyService:
    """Test numerology calculations"""
    
    def test_life_path_calculation(self):
        """Test life path number calculation"""
        # Test case for Amrit Gupta: 06/11/2000
        result = numerology_service.life_path_number("06/11/2000")
        assert isinstance(result, int)
        assert 1 <= result <= 9 or result in [11, 22, 33]
    
    def test_destiny_number(self):
        """Test destiny number calculation"""
        result = numerology_service.destiny_number("Amrit Gupta")
        assert isinstance(result, int)
        assert 1 <= result <= 9 or result in [11, 22, 33]
    
    def test_soul_urge_number(self):
        """Test soul urge number calculation"""
        result = numerology_service.soul_urge_number("Amrit Gupta")
        assert isinstance(result, int)
        assert 1 <= result <= 9 or result in [11, 22, 33]
    
    def test_personality_number(self):
        """Test personality number calculation"""
        result = numerology_service.personality_number("Amrit Gupta")
        assert isinstance(result, int)
        assert 1 <= result <= 9 or result in [11, 22, 33]
    
    def test_calculate_all_numbers(self):
        """Test calculating all numbers at once"""
        result = numerology_service.calculate_all_numbers(
            birth_date="06/11/2000",
            full_name="Amrit Gupta"
        )
        
        # Check all required fields are present
        assert "life_path" in result
        assert "destiny" in result
        assert "soul_urge" in result
        assert "personality" in result
        assert "maturity" in result
        assert "personal_year" in result
        assert "personal_month" in result
        assert "personal_day" in result
        
        # Verify all are valid numbers
        for key in ["life_path", "destiny", "soul_urge", "personality", 
                    "maturity", "personal_year", "personal_month", "personal_day"]:
            value = result[key]
            assert isinstance(value, int)
            assert 1 <= value <= 9 or value in [11, 22, 33]
    
    def test_compatibility_calculation(self):
        """Test compatibility score calculation"""
        person1 = numerology_service.calculate_all_numbers("06/11/2000", "Amrit Gupta")
        person2 = numerology_service.calculate_all_numbers("15/08/1995", "John Doe")
        
        compatibility = numerology_service.calculate_compatibility(person1, person2)
        
        assert isinstance(compatibility, float)
        assert 0 <= compatibility <= 100
    
    def test_risk_assessment(self):
        """Test risk level assessment"""
        master = numerology_service.calculate_all_numbers("06/11/2000", "Amrit Gupta")
        user = numerology_service.calculate_all_numbers("15/08/1995", "John Doe")
        
        risk = numerology_service.assess_risk_level(user, master)
        
        assert risk in ["very_low", "low", "medium", "high", "very_high"]
    
    def test_daily_guidance(self):
        """Test daily guidance generation"""
        numbers = numerology_service.calculate_all_numbers("06/11/2000", "Amrit Gupta")
        guidance = numerology_service.generate_daily_guidance(numbers)
        
        assert isinstance(guidance, str)
        assert len(guidance) > 0
    
    def test_lucky_times(self):
        """Test lucky times calculation"""
        numbers = numerology_service.calculate_all_numbers("06/11/2000", "Amrit Gupta")
        lucky = numerology_service.get_lucky_times(numbers)
        
        assert "lucky_hours" in lucky
        assert "lucky_days" in lucky
        assert "power_number" in lucky
        assert isinstance(lucky["lucky_hours"], list)
        assert isinstance(lucky["lucky_days"], list)
    
    def test_reduce_to_single_digit(self):
        """Test number reduction"""
        assert numerology_service.reduce_to_single_digit(25) == 7  # 2+5=7
        assert numerology_service.reduce_to_single_digit(123) == 6  # 1+2+3=6
        assert numerology_service.reduce_to_single_digit(11, allow_master=True) == 11
        assert numerology_service.reduce_to_single_digit(11, allow_master=False) == 2
    
    def test_invalid_date_format(self):
        """Test handling of invalid date format"""
        with pytest.raises(ValueError):
            numerology_service.calculate_from_date("invalid")
    
    def test_vowels_consonants_separation(self):
        """Test vowel and consonant separation"""
        vowels, consonants = numerology_service.get_vowels_consonants("Amrit Gupta")
        
        assert isinstance(vowels, str)
        assert isinstance(consonants, str)
        assert len(vowels) > 0
        assert len(consonants) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
