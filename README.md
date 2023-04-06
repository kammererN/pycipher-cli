
# PyCipher-CLI:
[![Documentation Status](https://readthedocs.org/projects/pycipher-cli/badge/?version=latest)](https://pycipher-cli.readthedocs.io/en/latest/?badge=latest)

PyCipher-CLI is a command-line encryption tool for text (.txt) files.

Source on [GitHub](https://github.com/nxrada/pycipher-cli) | 
[Documentation](https://pycipher-cli.readthedocs.io/en/master/) | [Demo]()

This project extends [Pycipher](https://github.com/jameslyons/pycipher), a Python library for encryption algorithms, by 
providing a command-line interface for the library's encryption algorithms. 

## Usage:
To call this script, first make sure Python 3.10.x is installed on your machine and that your system's PATH variable is 
configured accordingly. For more information, check out <https://www.python.org/downloads/>.

Once Python is installed, you can use this script by entering the '../src/pycipher-cli/' directory and typing the following
command into your preferred terminal (Windows example provided):

    py pyc-cli.py -i 'input.txt' -o 'output.txt' -c 'caesar' -k '5'

## Arguments:
    -i, --input 'path/to/input'      The path to the file to be encrypted. 

    -o, --output 'path/to/output'    The path to the output file.
    
    -c, --cipher 'cipher'            The selected encryption algorithm.
   
    -k, --key                        Specify the cipher key. 

    -w, --word                       Specify the cipher keyword (if necessary).
    
    -h, --help                       Receive more info on this script. 
  
## Supported Ciphers:
- ADFGX cipher
- ADFGVX cipher 
- Affine cipher
- Autokey cipher
- Atbash cipher
- Beaufort cipher
- Bifid cipher
- Caesar cipher
- Columnar transposition cipher
- Enigma M3 cipher (incomplete)
- Four-square cipher
- Gronsfeld cipher
- M-209 cipher (incomplete)
- Playfair cipher
- Polybius Square cipher (incomplete)
- Porta cipher
- Rail-fence cipher
- Rot13 cipher
- Simple Substitution cipher
- Vigenere cipher

## Licensing:
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
    along with this program.  If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>
