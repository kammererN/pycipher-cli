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
import argparse
import utils


# Parses command-line arguments.
class Parser:

    def __init__(self):

        # Instantiate parser object.
        parser = argparse.ArgumentParser(
            prog="pycipher-cli",
            usage="python3 pyccli.py --cipher [choice]",
            description='Encrypt a file using a cipher. For more information about cryptography and ciphers, '
                        'visit http://practicalcryptography.com/ciphers/.')

        # Parser arguments.
        parser.add_argument('-i', '--input', help='path/to/input/file', default=utils.get_relative_path('io/input.txt'),
                            required=False)
        parser.add_argument('-o', '--output', help='path/to/output/file. optional; default=io/output.txt',
                            required=False, default=utils.get_relative_path('io/output.txt'))
        parser.add_argument('-c', '--cipher', choices=['adfgx', 'adfgvx', 'affine', 'autokey', 'atbash', 'beaufort',
                                                       'bifid', 'caesar', 'col-trans',
                                                       'gronsfeld', 'playfair', 'polybius', 'porta',
                                                       'rail-fence', 'rot13', 'simple-sub', 'vigenere'],
                            help='the cipher option selected', required=True)
        parser.add_argument('-k', '--keys', nargs='*', help='key(s) for the cipher', required=False, default=None)

        # Parse the arguments.
        self.args = parser.parse_args()


# Point user to proper script in case of execution.
if __name__ == "__main__":
    print("Please run 'pyc-cli.py' instead.")
