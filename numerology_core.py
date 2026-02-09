# Numerology Core System for Amrit Gupta

# Constants
BIRTH_DATE = '06/11/2000'
BIRTH_TIME = '18:00'
BIRTH_PLACE = 'New Delhi'

# Function to calculate Life Path Number

def life_path_number(birth_date):
    date_components = birth_date.split('/')
    month = int(date_components[1])
    day = int(date_components[0])
    year = int(date_components[2])

    total = month + day + year
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    return total

# Function to interpret the Life Path Number

def interpret_life_path_number(number):
    interpretations = {
        1: 'Leadership and independence',
        2: 'Cooperation and diplomacy',
        3: 'Creativity and self-expression',
        4: 'Stability and order',
        5: 'Freedom and adventure',
        6: 'Nurturing and responsibility',
        7: 'Spirituality and introspection',
        8: 'Power and material success',
        9: 'Compassion and humanitarianism'
    }
    return interpretations.get(number, 'Unknown')

# Calculate and display results
life_path_number_result = life_path_number(BIRTH_DATE)
interpretation = interpret_life_path_number(life_path_number_result)

print(f'Life Path Number for Amrit Gupta: {life_path_number_result}')
print(f'Interpretation: {interpretation}')