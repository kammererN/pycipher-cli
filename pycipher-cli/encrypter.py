
"""
GNU General Public License v3+

PyCipher-CLI: tool for encryption of text (.txt) files.
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

    # Encrypts a file using the Atbash cipher.
    def atbash(self):
        with open(self.input_file, 'r') as file:
            plaintext = file.read()
            ciphertext = pycipher.Atbash().encipher(plaintext, True)
            with open(self.output_file, 'w') as output:
                output.write(ciphertext)

    # Encrypts a file using the Caesar cipher.
    def caesar(self, key):
        with open(self.input_file, 'r') as file:
            plaintext = file.read()
            ciphertext = pycipher.Caesar(key).encipher(plaintext, True)
            with open(self.output_file, 'w') as output:
                output.write(ciphertext)


# Point user to proper script in case of execution.
if __name__ == "__main__":
    print("Please run 'pycipher-cli.py' instead.")