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

    match encoder.cipher:
        case 'adfgx':  # FIXME
            encoder.adfgx()
        case 'adfgvx':  # TODO: Implement 01
            pass
        case 'affine':  # TODO: Implement 02
            pass
        case 'autokey':  # TODO: Implement 03
            pass
        case 'atbash':  # TODO: Implement 04
            pass
        case 'beaufort':  # TODO: Implement 05
            pass
        case 'bifid':  # TODO: Implement 06
            pass
        case 'caesar':  # TODO: Implement 07
            pass
        case 'columnar':  # TODO: Implement 08
            pass
        case 'foursquare':  # TODO: Implement 09
            pass
        case 'gronsfeld':  # TODO: Implement 10
            pass
        case 'playfair':  # TODO: Implement 11
            pass
        case 'polybius':  # TODO: Implement 12
            pass
        case 'porta':  # TODO: Implement 13
            pass
        case 'railfence':  # TODO: Implement 14
            pass
        case 'rot13':  # TODO: Implement 15
            pass
        case 'simple-sub':  # TODO: Implement 16
            pass
        case 'vigenere':  # TODO: Implement 17
            pass

    # Print success message.
    print(f"Successfully encrypted {encoder.input} to {encoder.output} using {encoder.cipher} cipher.")
