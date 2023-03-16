import os
from cryptography.fernet import Fernet

class SymmetricEncryption:
    def __init__(self):
        # generate a new symmetric key
        self.key = Fernet.generate_key()

    def encrypt(self, message):
        # create a Fernet cipher instance using the symmetric key
        cipher = Fernet(self.key)
        # encrypt the message using the cipher
        ciphertext = cipher.encrypt(message)
        return ciphertext

    def decrypt(self, ciphertext):
        # create a Fernet cipher instance using the symmetric key
        cipher = Fernet(self.key)
        # decrypt the ciphertext using the cipher
        plaintext = cipher.decrypt(ciphertext)
        return plaintext

    def get_key(self):
        # return the symmetric key
        return self.key

    def save_key(self, file_path):
        # save the symmetric key to a file
        with open(file_path, "wb") as f:
            f.write(self.key)

    def load_key(self, file_path):
        # load the symmetric key from a file
        with open(file_path, "rb") as f:
            self.key = f.read()
