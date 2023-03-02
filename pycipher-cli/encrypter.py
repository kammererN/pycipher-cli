
import pycipher


# Class that handles the execution of file encryption.
class Encrypter:

    # Empty constructor.
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    # Encrypts a file using the Caesar cipher.
    def caesar(self, key):
        key = key

        caesar = pycipher.Caesar(key)


