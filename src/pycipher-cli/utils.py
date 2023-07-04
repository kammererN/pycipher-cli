"""
GNU General Public License v3+

PyCipher-CLI: encryption tool for text (.txt) files.
Copyright (C) 2023 nxrada

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

"""
import random
import string
import os
from math import gcd

# Helper functions used in the rest of the project.


# Generates a random valid keysquare of 5x5, with J --> I. If ADFGVX, 6x6.
def generate_keysquare(adfgvx=False, store_file=True):
    if adfgvx:  # Generate a keysquare of 6x6 A-Z and 0-9
        keysquare = list(string.ascii_uppercase + string.digits)
        random.shuffle(keysquare)
        keysquare_string = ''.join(keysquare)
    else:  # Generate a keysquare of 5x5 A-Z, no J
        keysquare = list(string.ascii_uppercase)
        keysquare.remove('J')
        random.shuffle(keysquare)
        keysquare_string = ''.join(keysquare)

    if store_file:
        with open(get_relative_path('io/ksq.txt'), 'w') as file:
            file.write(keysquare_string)

    return keysquare_string


# Generates an alphabetic key of length. Used for most ciphers.
def generate_alpha_key(length, store_file=True, simple_sub=False):
    if simple_sub:
        alphabet = list(string.ascii_uppercase)
        random.shuffle(alphabet)
        key = ''.join(alphabet)

    else:
        # Generate a random key of length 'length' from the alphabet.
        alphabet = string.ascii_uppercase
        key = ''.join(random.choice(alphabet) for _ in range(len()))

    if store_file:
        with open(get_relative_path('io/key.txt'), 'w') as file:
            file.write(str(key))
    return key


# Generates a numeric key of length.
def generate_num_key(length, store_file=True):
    # Generate a random key of length 'length' from the alphabet.
    digits = string.digits
    key = [random.choice(digits) for _ in range(length)]
    # Convert each string digit to integer
    key = list(map(int, key))

    if store_file:
        with open(get_relative_path('io/key.txt'), 'w') as file:
            file.write(str(key))
    return key


# Generates a numeric period of boundaries. Used in Bifid
def generate_period(low, high, store_file=True):
    # Generate a random key of length 'length' from the alphabet.
    period = random.randint(low, high)

    if store_file:
        with open(get_relative_path('io/key.txt'), 'w') as file:
            file.write(str(period))
    return period


# Check if a number is coprime with 26. Used in Affine.
def is_coprime(n):
    return gcd(n, 26) == 1


# Reads a keysquare from a file and returns it as a string.
def read_keysquare(filename):
    keysquare = []
    with open(get_relative_path(filename), 'r') as f:
        for line in f:
            # Strip newline character and append to list
            row = line.strip()
            keysquare.append(row)
    # Join the lines with newline characters
    keysquare_string = ''.join(keysquare)
    return keysquare_string


# Converts any 'j' within the plaintext to 'i'. Used in keysquare generation.
def j_to_i(plaintext):
    plaintext = plaintext.replace('j', 'i')
    plaintext = plaintext.replace('J', 'I')
    return plaintext


# Gets relative path.
def get_relative_path(loc):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(script_directory, loc)
    return relative_path


# Print error message and encourage user to open GH issue.
def print_error_msg(e):
    print(f"Yikes! An error has occurred. Please create a new issue on this project's repository at "
          f"https://github.com/nxrada/pycipher-cli/issues/new\nError:\n\t{e}")
