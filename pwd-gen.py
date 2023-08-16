import os
import random
from dotenv import load_dotenv
from string import punctuation

# Load .env file
load_dotenv()

# Read parameters from .env
MIN_LENGTH = int(os.getenv('MIN_LENGTH', 10))
MAX_LENGTH = int(os.getenv('MAX_LENGTH', 64))
SPECIAL_CHARACTERS = os.getenv('SPECIAL_CHARACTERS', punctuation)

def generate_password() -> str:
    length = max(MIN_LENGTH, MAX_LENGTH)
    password = [
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), # At least one uppercase letter
        random.choice('abcdefghijklmnopqrstuvwxyz'), # At least one lowercase letter
        random.choice('0123456789'),                 # At least one number
        random.choice(SPECIAL_CHARACTERS)            # At least one special character
    ]
    num_required = len(password)
    all_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' + SPECIAL_CHARACTERS
    password += [random.choice(all_characters) for _ in range(length - num_required)] # Fill remaining characters
    random.shuffle(password)
    return ''.join(password)

password = generate_password()
print(f"Generated password: {password}")