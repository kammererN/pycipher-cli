
"""
GNU General Public License v3+

PyCipher-CLI: encryption tool for text (.txt) files.
Copyright (C) 2023 Nicholas Kammerer (nkammerer@albany.edu)

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


# Class that handles the execution of file encryption.
class Encrypter:

    # Constructor.
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    # Encrypts a file using the ADFGX cipher.
    def adfgx(self, key, keyword):
        with open(self.input_file, 'r') as file:
            plaintext = file.read()
            ciphertext = pycipher.ADFGX(key, keyword).encipher(plaintext)
            with open(self.output_file, 'w') as output:
                output.write(ciphertext)

    # Encrypts a file using the ADFGX cipher.
    def adfgvx(self):
        pass

    # Encrypts a file using the Autokey cipher.
    def autokey(self):
        pass

    # Encrypts a file using the Atbash cipher.
    def atbash(self):
        with open(self.input_file, 'r') as file:
            plaintext = file.read()
            ciphertext = pycipher.Atbash().encipher(plaintext, True)
            with open(self.output_file, 'w') as output:
                output.write(ciphertext)

    # Encrypts a file using the Beaufort cipher.
    def beaufort(self):
        pass
    # Encrypts a file using the Bifid cipher.

    def bifid(self):
        pass

    # Encrypts a file using the Caesar cipher.
    def caesar(self, key):
        with open(self.input_file, 'r') as file:
            plaintext = file.read()
            ciphertext = pycipher.Caesar(int(key)).encipher(plaintext, True)
            with open(self.output_file, 'w') as output:
                output.write(ciphertext)

    # Encrypts a file using the Columnar Transposition cipher.
    def columnar_transposition(self):
        pass

    # Encrypts a file using the Enigma M3 cipher.
    def enigma_m3(self):
        pass

    # Encrypts a file using the Four-Square cipher.
    def four_square(self):
        pass

    # Encrypts a file using the Gronsfeld cipher.
    def gronsfeld(self):
        pass

    # Encrypts a file using the M-209 cipher.
    def m209(self):
        pass

    # Encrypts a file using the Playfair cipher.
    def playfair(self):
        pass

    # Encrypts a file using the Polybius Square cipher.
    def polybius_square(self):
        pass

    # Encrypts a file using the Porta cipher.
    def porta(self):
        pass

    # Encrypts a file using the Rail-fence cipher.
    def rail_fence(self, key):
        with open(self.input_file, 'r') as file:
            plaintext = file.read()
            ciphertext = pycipher.Railfence(int(key)).encipher(plaintext, True)
            with open(self.output_file, 'w') as output:
                output.write(ciphertext)

    # Encrypts a file using the Rot13 cipher.
    def rot13(self):
        with open(self.input_file, 'r') as file:
            plaintext = file.read()
            ciphertext = pycipher.Rot13().encipher(plaintext, True)
            with open(self.output_file, 'w') as output:
                output.write(ciphertext)

    # Encrypts a file using the Simple Substitution cipher.
    def simple_substitution(self):
        pass

    # Encrypts a file using the Vigenere cipher.
    def vigenere(self):
        pass


# Point user to proper script in case of execution.
if __name__ == "__main__":
    print("Please run 'pyc-cli.py' instead.")