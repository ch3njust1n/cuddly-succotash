'''
Author: Justin Chen
Date:   5.1.2020
'''

import string
import random
import argparse

def generate_pwd(length, charset):
  if length < 64: raise Exception('Password must be a minimum length of 64')
  return ''.join(random.choice(charset) for _ in range(length))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', type=int, default=64, help='password length (default: 64)')

    charset = list(set(string.printable) - set(string.whitespace))
    args = parser.parse_args()
    pwd = generate_pwd(args.length, charset=charset)
    print(f'{args.length}-length pwd:\n\n{pwd}\n')

if __name__ == '__main__':
  main()
