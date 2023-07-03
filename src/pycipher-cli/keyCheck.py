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
    def __init__(self, key, key2, keyword, period):
        if key:
            self.key = key
        else:
            self.key
        self.key2 = key2
        self.keyword = keyword
        self.period = period

    # Check that the key is a 25 char keysquare.
    def is_25_keysquare(self):
        # If keysquare is in text file, read it to a string.
        if self.key is not None:
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

    # Check that a key is a 26-character alphanumeric string
    def is_alphanum_str_of_26(self):
        if self.key is not None:
            if len(self.key) == 26 and self.key.isalpha():
                return True
            else:
                return False

    # Check that a key is a 26-character string of alphabetical characters.
    def is_alphanum_str_of_36(self):
        if len(self.key) == 36 and self.key.isalpha():
            return True
        else:
            return False

    # Check that a key is only alphabetical characters.
    def is_alpha(self):
        if self.key.isalpha():
            return True
        else:
            return False

    # Check that a key is a sequence of numbers 0-9.
    def is_numsequence(self):
        if self.key.isdigit():
            return True
        else:
            return False

    # Check that a period is an integer.
    def is_int(self):
        if self.period.isdigit():
            return True
        else:
            return False

    # Check that a key is a valid affine multiplicative.
    def valid_affine_multiplicative(self):
        valid_affine_multis = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
        if self.key in valid_affine_multis:
            return True
        else:
            return False

    # Check that a key is a valid affine additive.
    def valid_affine_additive(self):  # TODO: Add functionality for key2.
        if self.key in range(0, 26):
            return True
        else:
            return False


