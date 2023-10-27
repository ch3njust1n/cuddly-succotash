'''
Author: Justin Chen
Date:   10.11.2022
'''

import random
import argparse
import configparser
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

CHARACTER_SET = []
CHARACTER_SET.extend(ascii_lowercase)
CHARACTER_SET.extend(ascii_uppercase)
CHARACTER_SET.extend(digits)

try:
    MIN_LENGTH = int(os.getenv('MIN_LENGTH', 10))
    MAX_LENGTH = int(os.getenv('MAX_LENGTH', 64))
except ValueError:
    print("Error: MIN_LENGTH and MAX_LENGTH must be integers.")
    exit(1)


'''
inputs:
min_length    (int)  Minimum number of characters
num_numeric   (int)  Number of digits
num_upper     (int)  Number of uppercase characters
num_lower     (int)  Number of lowercase characters
num_special	  (int)  Number of special characters
special_chars (list) List of user specified special characters

output:
requirements (list) Randomly selected required characters
'''
def set_requirements(min_length, num_numeric, num_upper, num_lower, num_special, special_chars):
	password = []

	special = special_chars if special_chars else punctuation
	CHARACTER_SET.extend(special)
 
	if min_length < 8:
		raise Exception('Invalid length: password must be greater than 8 characters')
	
	password.extend(random.choices(digits, k=num_numeric))
	password.extend(random.choices(ascii_uppercase, k=num_upper))
	password.extend(random.choices(ascii_lowercase, k=num_lower))
	password.extend(random.choices(special, k=num_special))

	return password


'''
inputs:
password   (list) List of characters to be extended
min_length (int)  Minimum length of the password

output:
password (list) List of all characters in the password
'''
def random_pad(password, min_length):
	if len(password) < min_length:
		remaining = min_length - len(password)
		password.extend(random.choices(CHARACTER_SET, k=remaining))
	
	return password


def main():
	format_filename = lambda file: f'{file}.ini' if not file.endswith('.ini') else file
	
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', '--config', type=format_filename, required=True, help='Configuration file')
	args = parser.parse_args()

	config = configparser.ConfigParser(allow_no_value=True)
	config.read(args.config)
	cfg = config['DEFAULT']
 
	toInt = lambda x: 0 if not x else int(x)
 
	min_length = toInt(cfg['min'])
	num_numeric = toInt(cfg['numeric'])
	num_upper = toInt(cfg['upper'])
	num_lower = toInt(cfg['lower'])
	num_special = toInt(cfg['special'])
	special_chars = cfg['special_chars'].split()
  
	password = set_requirements(min_length, num_numeric, num_upper, num_lower, num_special, special_chars)
	password = random_pad(password, min_length)
	random.shuffle(password)
	password = ''.join(password)

	print(f"\n{len(password)}-length pwd:\n\n{password}\n")


if __name__ == '__main__':
  main()
