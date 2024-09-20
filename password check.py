
import re

def check_password_strength(password):
    # Initialize strength criteria
    strength_criteria = {
        'length': False,
        'uppercase': False,
        'lowercase': False,
        'digits': False,
        'special': False
    }

    # Check length (minimum 8 characters)
    if len(password) >= 8:
        strength_criteria['length'] = True

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_criteria['uppercase'] = True

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_criteria['lowercase'] = True

    # Check for digits
    if re.search(r'[0-9]', password):
        strength_criteria['digits'] = True

    # Check for special characters (like @, #, $, etc.)
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_criteria['special'] = True

    # Count how many criteria are met
    strength_count = sum(strength_criteria.values())

    # Provide feedback based on the strength count
    if strength_count == 5:
        return 'Password is very strong.'
    elif strength_count == 4:
        return 'Password is strong.'
    elif strength_count == 3:
        return 'Password is moderate.'
    else:
        return 'Password is weak.'

# Main loop to interact with the user
while True:
    print('----- Password Complexity Checker -----')
    password = input('Enter a password to check its strength: ')
    result = check_password_strength(password)
    print(f'Strength: {result}')

    # Ask the user if they want to check another password
    run_again = input('Do you want to check another password? (yes/no): ').lower()
    if run_again != 'yes':
        print('Exiting the Password Checker. Stay safe!')
        break
