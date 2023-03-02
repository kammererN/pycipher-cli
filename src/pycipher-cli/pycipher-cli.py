
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

# Execute file
if __name__ == "__main__":

    # Instantiate Parser object.
    parser = cliParser.Parser()

    # Check the cipher selection, and execute the appropriate encryption algorithm.
    match parser.get_cipher().lower():
        case 'atbash':
            atbash = encrypter.Encrypter(parser.get_input(), parser.get_output())
            atbash.atbash()
            print(f'Encrypted file written to {parser.get_output()}.')
        case 'caesar':
            caesar = encrypter.Encrypter(parser.get_input(), parser.get_output())
            caesar.caesar(parser.get_key())
            print(f'Encrypted file written to {parser.get_output()}.')
            exit(0)
        case _:
            print("Invalid cipher option.")
            exit(1)
