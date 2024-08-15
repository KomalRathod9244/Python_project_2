# 1. Secure random password generator

import secrets
import string

def generate_password(length=12):
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    lowercase_letters = string.ascii_lowercase 
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        secrets.choice(lowercase_letters),
        secrets.choice(uppercase_letters),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]

    for _ in range(length - 4):
        password.append(secrets.choice(lowercase_letters + uppercase_letters + digits + special_characters))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

print("The generated password is : ",generate_password(12))  # Generate a 12-character password

