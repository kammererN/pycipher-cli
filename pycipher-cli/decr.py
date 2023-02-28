
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

# import https://pycipher.readthedocs.io/en/master/
import par  # Import cli parser 


# Function to decrypt a file. 
def pyt(): 
     # Parse the cli
     parser = par.ser()
    
     input_file = parser.input
     output_file = parser.output()
     cipher = parser.get_cipher()

     # Apply cipher based on user input. 
     match cipher:
          case "atbash":
               return print(cipher)
          case "adfgx":
               return print(cipher)
          case "adfgvx":
               return print(cipher)
          case "affine":
               return print(cipher)
          case "autokey":
               return print(cipher)
          case "atbash":
               return print(cipher)
          case "beaufort":
               return print(cipher)
          case "bifid":
               return print(cipher)
          case "caesar":
               return print(cipher)
          case "columnar-transposition":
               return print(cipher)
          case "enigma_m3":
               return print(cipher)
          case "foursquare":
               return print(cipher)
          case "gronsfeld":
               return print(cipher)
          case "m_209":
               return print(cipher)
          case "playfair":
               return print(cipher)
          case "polybius_square":
               return print(cipher)
          case "porta":
               return print(cipher)
          case "railfence":
               return print(cipher)
          case "rot13":
               return print(cipher)
          case "simple_substitution":
               return print(cipher)
          case "vigenere":
               return print(cipher)