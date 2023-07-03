
# PyCipher-CLI:
[![Documentation Status](https://readthedocs.org/projects/pycipher-cli/badge/?version=latest)](https://pycipher-cli.readthedocs.io/en/latest/?badge=latest)

PyCipher-CLI is a command-line encryption tool for plain-text (.txt) files.

This project extends [Pycipher](https://github.com/jameslyons/pycipher), a Python library for encryption algorithms, by 
providing a command-line interface for the library's encryption algorithms. 

Source on [GitHub](https://github.com/nxrada/pycipher-cli). Docs hosted at [readthedocs.io.](https://pycipher-cli.readthedocs.io/en/master/) Here's a [demo video.]()

## Usage:
To call this script, first make sure Python 3.10.x is installed on your machine and that your system's PATH variable is 
configured accordingly. This project also depends on pycipher. For more information, check out <https://www.python.org/downloads/>. 

Once Python is installed, you can use this script by entering the '../src/pycipher-cli/' directory and typing the following
command into your preferred terminal (Windows example provided):
```
    python3 pyccli.py -i 'input.txt' -o 'output.txt' -c 'caesar' -k '5'
```

### Arguments:
    -i, --input 'path/to/input'      The path to the file to be encrypted. 

    -o, --output 'path/to/output'    The path to the output file.
    
    -c, --cipher 'cipher'            The selected encryption algorithm.
   
    -k, --key                        Specify the cipher key. 

    -w, --word                       Specify the cipher keyword (if necessary).
    
    -h, --help                       Receive more info on this script. 
  
## Supported Ciphers:
* [ADFGX](http://practicalcryptography.com/ciphers/adfgx-cipher/)
* [ADFGVX](http://practicalcryptography.com/ciphers/adfgvx-cipher/) 
* [Affine](http://practicalcryptography.com/ciphers/affine-cipher/)
* [Autokey](http://practicalcryptography.com/ciphers/autokey-cipher/)
* [Atbash](http://practicalcryptography.com/ciphers/atbash-cipher-cipher/)
* [Beaufort](http://practicalcryptography.com/ciphers/beaufort-cipher/)
* [Bifid](http://practicalcryptography.com/ciphers/bifid-cipher/)
* [Caesar](http://practicalcryptography.com/ciphers/caesar-cipher/)
* [Columnar transposition](http://practicalcryptography.com/ciphers/columnar-transposition-cipher/)
* [Four-square](http://practicalcryptography.com/ciphers/four-square-cipher/)
* [Gronsfeld cipher](http://practicalcryptography.com/ciphers/classical-era/vigenere-gronsfeld-and-autokey/#variants)
* [Playfair](http://practicalcryptography.com/ciphers/classical-era/playfair/)
* [Polybius Square](http://practicalcryptography.com/ciphers/classical-era/polybius-square/) (wip)
* [Porta](http://practicalcryptography.com/ciphers/classical-era/porta/)
* [Rail-fence](http://practicalcryptography.com/ciphers/classical-era/rail-fence/)
* [Rot13](http://practicalcryptography.com/ciphers/classical-era/rot13/)
* [Simple Substitution](http://practicalcryptography.com/ciphers/classical-era/simple-substitution/)
* [Vigenere](http://practicalcryptography.com/ciphers/classical-era/vigenere-gronsfeld-and-autokey/)

### Acknowledgments:
This project builds heavily on information compiled by James Lyons at http://practicalcryptography.com, as well as his [pycipher](https://github.com/jameslyons/pycipher) library.

To learn more about cryptography and its history, check out [Practical Cryptography](http://practicalcryptography.com). 

### Licensing:
Copyright &copy; 2023 nxrada

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.
    
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>
