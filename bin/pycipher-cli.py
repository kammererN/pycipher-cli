
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

import encr  # Import encrypter
import decr  # Import decrypter
import par  # Import cli parser


# Execute program if ran from CLI
if __name__ == "__main__":
    if par.ser().decrypt:
        decr.pyt()
    else:
        encr.pyt()
