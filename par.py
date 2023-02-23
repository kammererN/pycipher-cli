# MIT License
#
# Copyright (c) 2023 Nicholas Kammerer (nkammerer@albany.edu)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


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
