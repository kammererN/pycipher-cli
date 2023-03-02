

import argparse


# Parses
class Parser:

    def __init__(self):
        # Instantiate argparse.
        parser = argparse.ArgumentParser(
            prog="pycipher-cli",
            usage="python3 pycipher-cli.py [-i] PATH/TO/FILE [-c] CIPHER [-k] KEY",
            description='Encrypt or decrypt a file using a cipher.')

        # Add arguments to the parser.
        parser.add_argument('-i', '--input', help='path/to/input/file', required=True)
        parser.add_argument('-c', '--cipher', help='the cipher option selected', required=True)
        parser.add_argument('-o', '--output', help='optional/path/to/output/file', required=False,
                            default='../')
        parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt the input file', required=False,
                            default=False)
        parser.add_argument('-k', '--key', help='key for the cipher', required=False, default=None)

        # Parse the arguments.
        self.args = parser.parse_args()

