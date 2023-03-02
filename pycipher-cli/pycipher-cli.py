
"""
GNU General Public License v3+

PyCipher-CLI: tool for encryption of text (.txt) files.
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
import pycipher


def pycipher_cli():

    # Parse CLI arguments
    args = cliParser.Parser().args

    # Call encrypter
    if not args.decrypt:
        pass


# Execute file
if __name__ == "__main__":
    pycipher_cli()
