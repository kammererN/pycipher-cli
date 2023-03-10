
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

import argparse


# Parses
class Parser:

    def __init__(self):
        # Instantiate argparse.
        parser = argparse.ArgumentParser(
            prog="pycipher-cli",
            usage="python pyc.py [-i] PATH/TO/FILE [-c] CIPHER [-k] KEY",
            description='Encrypt a file using a cipher.')

        # Add arguments to the parser.
        parser.add_argument('-i', '--input', help='path/to/input/file', default='input.txt')
        parser.add_argument('-o', '--output', help='optional/path/to/output/file', required=False,
                            default='output.txt')
        parser.add_argument('-c', '--cipher', choices=['adfgx', 'adfgvx', 'affine', 'autokey', 'atbash', 'beaufort',
                                                       'bifid', 'caesar', 'columnar_trans', 'enigma_m3', 'four_square',
                                                       'gronsfeld', 'm209', 'playfair', 'poly_square', 'porta',
                                                       'rail_fence', 'rot13', 'simple_sub', 'vigenere'],
                            help='the cipher option selected', required=True)
        parser.add_argument('-k', '--key', help='key for the cipher', required=False, default=None)
        parser.add_argument('-w', '--word', help='keyword for the cipher', required=False, default=None)

        # Parse the arguments.
        self.args = parser.parse_args()

    # Accessor for the cipher argument.
    def get_cipher(self):
        return self.args.cipher

    # Accessor for the input file argument.
    def get_input(self):
        return self.args.input

    # Accessor for the output file argument.
    def get_output(self):
        return self.args.output

    # Accessor for the decrypt argument.
    def get_key(self):
        return self.args.key

    # Accessor for the keyword argument.
    def get_keyword(self):
        return self.args.word


# Point user to proper script in case of execution.
if __name__ == "__main__":
    print("Please run 'pyc-cli.py' instead.")
