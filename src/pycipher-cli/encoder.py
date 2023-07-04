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
import utils
import random as rand

# Key length generation constants.
KEYLEN_MIN = 5
KEYLEN_MAX = 25


# Class that handles the execution of file encryption.
class Encoder:

    def __init__(self, input_file, output_file, cipher, keys):
        # Parser data
        self.input = input_file
        self.output = output_file
        self.cipher = cipher
        if isinstance(keys, list):
            self.keys = keys
        else:
            self.keys = []

        # Read input.txt to self.plaintext
        with open(self.input, 'r') as file:
            self.plaintext = file.read()

    # Writes ciphertext to output file.
    def write_output(self, ciphertext):
        with open(self.output, 'w') as output:
            output.write(ciphertext)

    # Print result of encoder activity.
    def print_result(self, success=False):
        if success:
            print(f"Successfully encrypted file to {self.output} using {self.cipher} cipher.")

    # Generate key if not provided in args.
    def generate_key(self, _min=KEYLEN_MIN, _max=KEYLEN_MAX, bifid=False, gronsfeld=False, simple_sub=False):
        # Generates period key for Bifid cipher.
        if bifid:
            print("No period detected. Auto-generating period...")
            self.keys.append(utils.generate_period(_min, _max))
            print("Saved period to key.txt for future decryption.")

        # Generates key for Gronsfeld cipher.
        elif gronsfeld:
            print("No key detected. Auto-generating key...")
            self.keys.append(utils.generate_num_key(length=rand.randint(_min, _max)))
            print("Saved period to key.txt for future decryption.")

        # Generates alpha-unique key for simple-substitution.
        elif simple_sub:
            print("No key detected. Auto-generating key...")
            self.keys.append(utils.generate_alpha_key(length=rand.randint(_min, _max), simple_sub=True))
            print("Saved key to key.txt for future decryption.")

        # If no key exists, generate it.
        if not self.keys:
            print("No key detected. Auto-generating key...")
            self.keys.append(utils.generate_alpha_key(length=rand.randint(_min, _max)))
            print("Saved key to key.txt for future decryption.")

    # Generate keysquare if not provided in args.
    def generate_ksq(self, adfgvx=False, playfair=False):
        if adfgvx:
            if not self.keys:
                print("No keys detected. Auto-generating keysquare...")
                self.keys.append(utils.generate_keysquare())
                print("Saved keysquare to ksq.txt for future decryption.")
        elif playfair:
            print("No keys detected. Auto-generating keysquare...")
            self.keys.append(utils.generate_keysquare(playfair=True))
            print("Saved keysquare to ksq.txt for future decryption.")
        else:
            if not self.keys:
                print("No keys detected. Auto-generating keysquare...")
                self.keys.append(utils.generate_keysquare())
                print("Saved keysquare to ksq.txt for future decryption.")

    # Prepares plaintext for Playfair cipher.
    def prepare_plaintext(self):
        # Replace double letters with 'x'
        modified_text = ''
        for i in range(len(self.plaintext) - 1):
            if self.plaintext[i] == self.plaintext[i + 1]:
                modified_text += self.plaintext[i] + 'x'
            else:
                modified_text += self.plaintext[i]

        # Add the last character
        modified_text += self.plaintext[-1]

        # If the text length is odd, add an 'x'
        if len(modified_text) % 2 != 0:
            self.modified_text += 'x'

        # Break into pairs of letters
        pairs = ' '.join(modified_text[i:i + 2] for i in range(0, len(modified_text), 2))

        self.plaintext = pairs

    # Encrypts a file using the ADFGX cipher.
    def adfgx(self):
        # If no key or keysquare exists, generate and save them.
        self.generate_ksq()
        self.generate_key()

        # Ensure that the plaintext drops Js in text.
        self.plaintext = utils.j_to_i(self.plaintext)

        try:
            # Encrypt the plaintext using the ADFGX cipher, and write the ciphertext to output.txt.
            self.write_output(pycipher.ADFGX(key=self.keys[0],
                                             keyword=self.keys[1]).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the ADFGVX cipher.
    def adfgvx(self):
        # If no key or keysquare exists, generate and save them.
        self.generate_ksq(adfgvx=True)
        self.generate_key()
        try:
            # Encrypt the plaintext using the ADFGVX cipher, and write the ciphertext to output.txt.
            self.write_output(pycipher.ADFGVX(key=self.keys[0],
                                              keyword=self.keys[1]).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Affine cipher.
    def affine(self):
        # If no key or keysquare exists, generate and save them.
        if not self.keys:
            # Key 'a' should be chosen such that a and 26 are coprime.
            self.keys.append(rand.choice([i for i in range(1, 26) if utils.is_coprime(i)]))
            # Key 'b' can be any integer from 0 to 25.
            self.keys.append(rand.randint(0, 25))

            # Write affine keys to key.txt
            with open(utils.get_relative_path('io/key.txt'), 'w') as file:
                for key in self.keys:
                    file.write(str(key))
                    file.write('\n')
        try:
            # Encrypt the plaintext using the Affine cipher, and write the ciphertext to output.txt.
            self.write_output(pycipher.Affine(int(self.keys[0]), int(self.keys[1])).encipher(self.plaintext, True))

            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Autokey cipher.
    def autokey(self):
        # If no key exists, generate it.
        self.generate_key()

        try:
            # Encrypt the plaintext using the Autokey cipher, and write the ciphertext to output.txt.
            self.write_output(pycipher.Autokey(self.keys[0]).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Atbash cipher.
    def atbash(self):
        try:
            self.write_output(pycipher.Atbash().encipher(self.plaintext, True))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Beaufort cipher.
    def beaufort(self):
        # If no key exists, generate it.
        self.generate_key()

        try:
            # Encrypt the plaintext using the Affine cipher, and write the ciphertext to output.txt.
            self.write_output(pycipher.Beaufort(self.keys[0]).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Bifid cipher.
    def bifid(self):
        # Generate keysquare as bifid key
        self.generate_ksq()

        # Generate Bifid period
        self.generate_key(bifid=True)
        try:
            self.write_output(pycipher.Bifid(self.keys[0], self.keys[1]).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Caesar cipher.
    def caesar(self):
        if not self.keys:
            print("No keys detected. Auto-generating key...")
            self.keys.append(rand.randint(0, 26))
            print("Saved key to key.txt for future decryption.")

            # Write affine keys to key.txt
            with open(utils.get_relative_path('io/key.txt'), 'w') as file:
                file.write(str(self.keys[0]))
        try:
            self.write_output(pycipher.Caesar(self.keys[0]).encipher(self.plaintext, True))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Columnar Transposition cipher.
    def columnar_transposition(self):
        # If no key exists, generate it.
        self.generate_key()
        try:
            # Encrypt the plaintext using the Columnar-Transposition cipher, and write the ciphertext to output.txt.
            self.write_output(pycipher.ColTrans(self.keys[0]).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Gronsfeld cipher.
    def gronsfeld(self):
        # If no key exists, generate it.
        self.generate_key(gronsfeld=True)

        try:
            # Encrypt the plaintext using the Columnar-Transposition cipher, and write the ciphertext to output.txt.
            self.write_output(pycipher.Gronsfeld(self.keys[0]).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Playfair cipher.
    def playfair(self):
        # Generate keysquare
        self.generate_ksq(playfair=True)

        # Prepare plaintext for Playfair cipher.
        self.prepare_plaintext()

        try:
            self.write_output(pycipher.Playfair(self.keys[0]).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Polybius Square cipher.
    def polybius_square(self):
        # Generate keysquare as polybius key
        self.generate_ksq()

        try:
            self.write_output(pycipher.PolybiusSquare(self.keys[0]).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Porta cipher.
    def porta(self):
        # If no key exists, generate it.
        self.generate_key()
        try:
            self.write_output(pycipher.Porta(self.keys[0]).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Rail-fence cipher.
    def rail_fence(self):
        if not self.keys:
            print("No key detected. Auto-generating key...")
            self.keys.append(rand.randint(0, 15))
            print("Saved key to key.txt for future decryption.")

            # Write affine keys to key.txt
            with open(utils.get_relative_path('io/key.txt'), 'w') as file:
                file.write(str(self.keys[0]))
        try:
            self.write_output(pycipher.Railfence(int(self.keys[0])).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Rot13 cipher.
    def rot13(self):
        try:
            self.write_output(pycipher.Rot13().encipher(self.plaintext, True))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Simple Substitution cipher.
    def simple_substitution(self):
        # Key generation if not user-submitted.
        self.generate_key(simple_sub=True)

        try:
            self.write_output(pycipher.SimpleSubstitution(self.keys[0]).encipher(self.plaintext, True))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return

    # Encrypts a file using the Vigenere cipher.
    def vigenere(self):
        # If no key exists, generate it.
        self.generate_key()

        try:
            # Encrypt the plaintext using the Columnar-Transposition cipher, and write the ciphertext to output.txt.
            self.write_output(pycipher.Vigenere(self.keys[0]).encipher(self.plaintext))
            self.print_result(success=True)
        except Exception as e:
            utils.print_error_msg(e)
            return


# Point user to proper script in case of execution.
if __name__ == "__main__":
    print("Please run 'pyccli.py' instead.")
