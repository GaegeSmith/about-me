import base64
import os

# these 4 lines I added, and made the code into a class
# https://www.geeksforgeeks.org/clear-screen-python/
os.system('pip install cryptography')
# I knew thats how you send system commands to the terminal, so I figured I would try doing this and it worked

# most of code from https://stackoverflow.com/questions/60653497/encrypt-and-decrypt-files-in-python
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pathlib import Path


class CryptoGraphy:
    # generate an encyption key
    def genKey(password_provided, filePath):
        password = password_provided.encode()

        salt = b"\xb9\x1f|}'S\xa1\x96\xeb\x154\x04\x88\xf3\xdf\x05"

        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                    backend=default_backend())

        key = base64.urlsafe_b64encode(kdf.derive(password))
        with open(f"{filePath}\\key.key", 'wb') as key_file:
            key_file.write(key)

    # read the encryption key from the key file
    def getKey(filePath):
        keyFile = open(f'{filePath}\\key.key', 'rb')
        key = keyFile.read()
        keyFile.close
        return key

    # encrypt some data, as a string, and output that to a file 
    def encrypt(data, dir, output = "default"):
        data = data.encode()
        file = Path(output)
        fernet = Fernet(CryptoGraphy.getKey(dir))
        encrypted = fernet.encrypt(data)

        with open(f'{file}', 'wb') as f:
            f.write(encrypted)
        f.close()

    # decrypt a file and return the decrypted text
    def decrypt(fileName, dir):
        fernet = Fernet(CryptoGraphy.getKey(dir))
        with open(f"{fileName}", 'rb') as f:
            file = f.read()
        f.close()
        decryptedFile = fernet.decrypt(file)
        return decryptedFile.decode()






