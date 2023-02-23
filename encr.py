
import par  # Import cli parser

    
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


