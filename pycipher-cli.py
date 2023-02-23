
import encr  # Import encrypter
import decr  # Import decrypter
import par  # Import cli parser

# Execute program if ran from CLI
if __name__ == "__main__":
    if par.ser().decrypt:
        decr.pyt()
    else:
        encr.pyt()
