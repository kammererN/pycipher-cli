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
# Import modules
import cliParser as clip
import encoder as ncdr

# Execute file
if __name__ == "__main__":

    # Instantiate Parser, Encoder and Collector objects.
    parser = clip.Parser()
    encoder = ncdr.Encoder(parser.args.input, parser.args.output, parser.args.cipher, parser.args.keys)

    # Encrypt
    if not parser.args.decrypt:
        match encoder.cipher:
            case 'adfgx':
                encoder.adfgx()
            case 'adfgvx':
                encoder.adfgvx()
            case 'affine':
                encoder.affine()
            case 'autokey':
                encoder.autokey()
            case 'atbash':
                encoder.atbash()
            case 'beaufort':
                encoder.beaufort()
            case 'bifid':
                encoder.bifid()
            case 'caesar':
                encoder.caesar()
            case 'col-trans':
                encoder.columnar_transposition()
            case 'gronsfeld':
                encoder.gronsfeld()
            case 'playfair':
                encoder.playfair()
            case 'polybius':
                encoder.polybius_square()
            case 'porta':
                encoder.porta()
            case 'rail-fence':
                encoder.rail_fence()
            case 'rot13':
                encoder.rot13()
            case 'simple-sub':
                encoder.simple_substitution()
            case 'vigenere':
                encoder.vigenere()

    # Decrypt
    else:
        print("Yikes! Decryption is not yet supported. Feel free to contribute to this feature by forking the"
              " repository at https://github.com/nxrada/pycipher-cli/.")

