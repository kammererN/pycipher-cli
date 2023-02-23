
import par  # Import cli parser

# Functions which encrypt a file according to a given algorithm. 
def atbash(input): # Atbash Cipher
    return 0


def rot13(input): # Rot 13 Cipher
    return 0


def caesar(input): # Caesar Cipher
    return 0

    
# Function to encrypt a file.
def pyt(): 
        # Parse the cli
        parser = par.ser()
    
        input_file = parser.input
        output_file = parser.output()
        cipher = parser.get_cipher()

        # Apply cipher based on user input. 
        match cipher:
             case "atbash":
                  return print("atbash")#atbash(input_file, output_file)
             case "rot13":
                  return print("rot13")#rot13(input_file, output_file)
             case "caesar":
                  return print("caesar")#caesar(input_file, output_file)
             case __: 
                  return print("error")


