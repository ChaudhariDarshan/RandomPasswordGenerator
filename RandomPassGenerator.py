import random
import string

def generate_password(length=12):
    # Define character sets for lowercase letters, uppercase letters, digits, and special characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one uppercase letter
    password = random.choice(uppercase_letters)

    # Add lowercase letters, digits, and special characters to the password
    all_characters = lowercase_letters + digits + special_characters
    password += ''.join(random.choice(all_characters) for _ in range(length - 1))

    # Shuffle the password characters to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Generate a strong password with a default length of 12 characters
strong_password = generate_password()
print("\n\n Your Strong Password is := ",strong_password)
#print(strong_password)
