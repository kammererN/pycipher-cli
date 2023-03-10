
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

# Import modules
import cliParser
import encrypter
import keyCheck

# Execute file
if __name__ == "__main__":

    # Instantiate Parser object.
    parser = cliParser.Parser()
    # Instantiate Encrypter object.
    enc = encrypter.Encrypter(parser.get_input(), parser.get_output())
    # Instantiate KeyCheck object.
    check = keyCheck.KeyCheck(parser.get_key(), parser.get_keyword())

    # Check the cipher selection, and execute the appropriate encryption algorithm.
    match parser.get_cipher().lower():
        case 'adfgx':
            pass
        case 'adfgvx':
            pass
        case 'affine':
            pass
        case 'autokey':
            pass
        case 'atbash':
            enc.atbash()
        case 'beaufort':
            pass
        case 'bifid':
            pass
        case 'caesar':
            if not check.is_between_0_25():
                print("Invalid key. Key must be an integer between 0 and 25.")
                exit(1)
            enc.caesar(parser.get_key())
        case 'columnar_trans':
            pass
        case 'enigma_m3':
            pass
        case 'four_square':
            pass
        case 'gronsfeld':
            pass
        case 'm209':
            pass
        case 'playfair':
            pass
        case 'poly_square':
            pass
        case 'porta':
            pass
        case 'rail_fence':
            if not check.is_positive_int():
                print("Invalid key. Key must be a positive integer.")
                exit(1)
            enc.rail_fence(parser.get_key())
        case 'rot13':
            enc.rot13()
        case 'simple_sub':
            pass
        case 'vigenere':
            pass
        case _:
            print("Invalid cipher option.")
            exit(1)
    # Print success message.
    print(f"Encrypted file written to '{parser.get_output()}', using the {parser.get_cipher().title()} cipher.")
    exit(0)
