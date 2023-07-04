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

import pycipher
import utils as u


# Class that handles the execution of file encryption.
class Encoder:

    def __init__(self, input_file, output_file, cipher, keys):
        # Parser data
        self.input = input_file
        self.output = output_file
        self.cipher = cipher
        self.keys = keys if isinstance(keys, list) else [keys]

        # Read input.txt to self.plaintext
        with open(self.input, 'r') as file:
            self.plaintext = file.read()

    # Writes ciphertext to output file.
    def write_output(self, ciphertext):
        with open(self.output, 'w') as output:
            output.write(ciphertext)

    # Encrypts a file using the ADFGX cipher.
    def adfgx(self):  # FIXME
        # If the cipher is ADFGX, read the keysquare to self.keys[0] (primary key location) for encryption.
        # Ensures that J is dropped from the keysquare.
        self.keys[0] = u.j_to_i(u.read_keysquare(self.keys[0]))

        # Ensure that the plaintext drops Js in text.
        self.plaintext = u.j_to_i(self.plaintext)

        try:
            # Encrypt the plaintext using the ADFGX cipher, and write the ciphertext to output.txt.
            self.write_output(pycipher.ADFGX(key=self.keys[len(self.keys) - 2],
                                             keyword=self.keys[len(self.keys) - 1]).encipher(self.plaintext))
        except Exception as e:
            print(f"Yikes! An error has occurred. Please create a new issue on this project's repository at "
                  f"https://github.com/nxrada/pycipher-cli/issues/new\n\tError code:\n\t{e}")

    # Encrypts a file using the ADFGVX cipher.
    def adfgvx(self, key, keyword):  # FIXME
        self.write_output(pycipher.ADFGVX(key, keyword).encipher(self.plaintext))

    # Encrypts a file using the Affine cipher.
    def affine(self, key1, key2):  # FIXME
        self.write_output(pycipher.Affine(int(key1), int(key2)).encipher(self.plaintext, True))

    # Encrypts a file using the Autokey cipher.
    def autokey(self, key):  # FIXME
        self.write_output(pycipher.Autokey(key).encipher(self.plaintext))

    # Encrypts a file using the Atbash cipher.
    def atbash(self):  # FIXME
        self.write_output(pycipher.Atbash().encipher(self.plaintext, True))

    # Encrypts a file using the Beaufort cipher.
    def beaufort(self, key):  # FIXME
        self.write_output(pycipher.Beaufort(key).encipher(self.plaintext))

    # Encrypts a file using the Bifid cipher.
    def bifid(self, key, period):  # FIXME
        self.write_output(pycipher.Bifid(key, period).encipher(self.plaintext))

    # Encrypts a file using the Caesar cipher.
    def caesar(self, key):  # FIXME
        self.write_output(pycipher.Caesar(int(key)).encipher(self.plaintext, True))

    # Encrypts a file using the Columnar Transposition cipher.
    def columnar_transposition(self, key):  # FIXME
        self.write_output(pycipher.ColTrans(key).encipher(self.plaintext))

    # Encrypts a file using the Four-Square cipher.
    def four_square(self, key1, key2):  # FIXME
        self.write_output(pycipher.Foursquare(key1, key2).encipher(self.plaintext))

    # Encrypts a file using the Gronsfeld cipher.
    def gronsfeld(self, key):  # FIXME
        self.write_output(pycipher.Gronsfeld(key).encipher(self.plaintext))

    # Encrypts a file using the Playfair cipher.
    def playfair(self, key):  # FIXME
        self.write_output(pycipher.Playfair(key).encipher(self.plaintext))

    # Encrypts a file using the Polybius Square cipher.
    def polybius_square(self):  # FIXME
        pass

    # Encrypts a file using the Porta cipher.
    def porta(self, key):  # FIXME
        self.write_output(pycipher.Porta(key).encipher(self.plaintext))

    # Encrypts a file using the Rail-fence cipher.
    def rail_fence(self, key):  # FIXME
        self.write_output(pycipher.Railfence(int(key)).encipher(self.plaintext, True))

    # Encrypts a file using the Rot13 cipher.
    def rot13(self):  # FIXME
        self.write_output(pycipher.Rot13().encipher(self.plaintext, True))

    # Encrypts a file using the Simple Substitution cipher.
    def simple_substitution(self, key):  # FIXME
        self.write_output(pycipher.SimpleSubstitution(key).encipher(self.plaintext, True))

    # Encrypts a file using the Vigenere cipher.
    def vigenere(self, key):  # FIXME
        self.write_output(pycipher.Vigenere(key).encipher(self.plaintext))


# Point user to proper script in case of execution.
if __name__ == "__main__":
    print("Please run 'pyccli.py' instead.")
