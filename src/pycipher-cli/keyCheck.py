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


# Defines various functions for checking the validity of key inputs.
class KeyCheck:
    def __init__(self, key, keyword):
        self.key = key
        self.keyword = keyword

    # Check that the key is a 25 char keysquare.
    def is_25_keysquare(self):
        if len(self.key) != 25:
            return False
        else:
            return True

    # Check that the key is an integer between 0 and 25.
    def is_between_0_25(self):
        if 0 <= int(self.key) <= 25:
            return True
        else:
            return False

    # Check that the key is a positive integer. (Rail-fence)
    def is_positive_int(self):
        if int(self.key) > 0:
            return True
        else:
            return False
