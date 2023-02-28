
'''
GNU General Public License v3+

PyCipher-CLI: tool that encrypts/decrypts a text (.txt) file.  
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

'''

import argparse


# Main function
def ser():
    # Instantiate argparse.
    parser = argparse.ArgumentParser( 
        prog = "pycipher-cli",
        usage = "python3 pycipher-cli.py [-i] PATH/TO/FILE [-c] CIPHER",
        description='Encrypt or decrypt a file using a cipher.') 

    # Add arguments to the parser. 
    parser.add_argument('-i', '--input', help='path/to/input/file', required=True)
    parser.add_argument('-c', '--cipher', help='the cipher option selected', required=True)
    parser.add_argument('-o', '--output', help='optional/path/to/output/file',required=False, default='../default/output.txt')
    parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt the input file', required=False, default=False)


    # Parse the arguments.
    args = parser.parse_args()

    return args
