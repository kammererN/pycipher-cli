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
# Helper functions used in the rest of the project.


# Reads a keysquare from a file and returns it as a string. Necessary for keysquare ciphers.
def read_keysquare(filename):
    keysquare = []
    with open(filename, 'r') as f:
        for line in f:
            # Strip newline character and append to list
            row = line.strip()
            keysquare.append(row)
    # Join the lines with newline characters
    keysquare_string = ''.join(keysquare)
    return keysquare_string


# Converts any 'j' within the plaintext to 'i'. Necessary for ADFGX encryption.
def j_to_i(plaintext):
    plaintext = plaintext.replace('j', 'i')
    plaintext = plaintext.replace('J', 'I')
    return plaintext
