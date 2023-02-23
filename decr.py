# MIT License
#
# Copyright (c) 2023 Nicholas Kammerer (nkammerer@albany.edu)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

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