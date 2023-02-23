
import argparse

# Main function
def ser():
    # Instantiate argparse.
    parser = argparse.ArgumentParser( 
        prog = "encrPytion",
        usage = "python3 encr.py [-i] PATH/TO/FILE [-c] CIPHER",
        description='Encrypt or decrypt a file using a cipher.') 

    # Add arguments to the parser. 
    parser.add_argument('-i', '--input', help='path/to/input/file', required=True)
    parser.add_argument('-c', '--cipher', help='the cipher option selected', required=True)
    parser.add_argument('-o', '--output', help='optional/path/to/output/file',required=False, default='../default/output.txt')
    parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt the input file', required=False, default=False)


    # Parse the arguments.
    args = parser.parse_args()

    return args
