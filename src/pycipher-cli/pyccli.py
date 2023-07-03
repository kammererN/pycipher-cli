
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
if __name__ == "__main__":  # TODO: WRITE DOCS!!!

    # Instantiate Parser, encrypter and keyCheck objects.
    parser = cliParser.Parser()
    enc = encrypter.Encrypter(parser.get_input(), parser.get_output())
    check = keyCheck.KeyCheck(parser.get_key(), parser.get_key2(), parser.get_keyword(), parser.get_period())

    # Check the cipher selection, and execute the appropriate encryption algorithm.
    match parser.get_cipher().lower():
        case 'adfgx':  # TODO: Test functionality.
            if check is not None:
                if not check.is_25_keysquare():
                    print("Invalid key. Key must be a 25 character keysquare.")
                    exit(1)
                enc.adfgx(parser.get_key(), parser.get_keyword())
            else:
                print("Key is required for ADFGX cipher. Key must be a 26 character keysquare.")
        case 'adfgvx':  # TODO: Test functionality.
            if not check.is_alphanum_str_of_36():
                print("Invalid key. Key must be a 36 character keysquare.")
                exit(1)
            enc.adfgvx(parser.get_key(), parser.get_keyword())
        case 'affine':  # TODO: Test functionality.
            if not check.valid_affine_multiplicative():
                print("Invalid key1. Key1 must be an integer in set [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25].")
                exit(1)
            if not check.valid_affine_additive():
                print("Invalid key2. Key2 must be an integer in range [0, 25].")
                exit(1)
            enc.affine(parser.get_key(), parser.get_key2())
        case 'autokey':  # TODO: Test functionality.
            if not check.is_alpha():
                print("Invalid key. Key must be alphabetical.")
                exit(1)
            enc.autokey(parser.get_key())
        case 'atbash':
            enc.atbash()
        case 'beaufort':  # TODO: Test functionality.
            if not check.is_alpha():
                print("Invalid key. Key must be alphabetical.")
                exit(1)
            enc.beaufort(parser.get_key())
        case 'bifid':  # TODO: Test functionality.
            if not check.is_25_keysquare():
                print("Invalid key. Key must be a 25 character keysquare.")
                exit(1)
            if not check.is_int():
                print("Invalid period. Period must be an integer.")
                exit(1)
            enc.bifid(parser.get_key(), parser.get_period())
        case 'caesar':
            if not check.is_between_0_25():
                print("Invalid key. Key must be an integer between 0 and 25.")
                exit(1)
            enc.caesar(parser.get_key())
        case 'columnar_trans':  # TODO: Test functionality.
            if not check.is_alpha():
                print("Invalid key. Key must be alphabetical.")
                exit(1)
            enc.columnar_transposition(parser.get_key())
        case 'enigma_m3':  # Far too complex a cipher to fit in the scope of this project.
            pass
        case 'four_square':   # TODO: Test functionality.
            if not check.is_25_keysquare():
                print("Invalid key. Key must be a 25 character keysquare string.")
                exit(1)
            enc.four_square(parser.get_key(), parser.get_key2())
        case 'gronsfeld':  # TODO: Test functionality.
            if not check.is_numsequence():
                print("Invalid key. Key must be a sequence of integers.")
                exit(1)
            enc.gronsfeld(parser.get_key())
        case 'm209':  # Like Enigma, this cipher exists outside the scope of this project.
            pass
        case 'playfair':  # TODO: Test functionality.
            if not check.is_25_keysquare():
                print("Invalid key. Key must be a 25 character keysquare string.")
                exit(1)
            enc.playfair(parser.get_key())
        case 'poly_square':  # TODO: Implement, maybe?
            pass
        case 'porta':  # TODO: Test functionality.
            if not check.is_alpha():
                print("Invalid key. Key must be alphabetical.")
                exit(1)
            enc.porta(parser.get_key())
        case 'rail_fence':
            if not check.is_positive_int():
                print("Invalid key. Key must be a positive integer.")
                exit(1)
            enc.rail_fence(parser.get_key())
        case 'rot13':
            enc.rot13()
        case 'simple_sub':
            if not check.is_alphanum_str_of_26():
                print("Invalid key. Key must be a permutation of the alphabet.")
                exit(1)
            enc.simple_substitution(parser.get_key())
        case 'vigenere':  # TODO: Test functionality.
            if not check.is_alpha():
                print("Invalid key. Key must be alphabetical.")
                exit(1)
            enc.vigenere(parser.get_key())
        case _:
            print("Invalid cipher option.")
            exit(1)

    # Print success message.
    print(f"Encrypted file written to '{parser.get_output()}', using the {parser.get_cipher().title()} cipher.")
    exit(0)
