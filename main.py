from encryption.asymmetric import AsymmetricEncryption
from encryption.symmetric import SymmetricEncryption

def asymmetric():

    # create an instance of AsymmetricEncryption
    asymmetric_encryption = AsymmetricEncryption()

    # save the private key to a PEM file
    asymmetric_encryption.save_private_key_to_pem("private_key.pem")

    # save the public key to a PEM file
    asymmetric_encryption.save_public_key_to_pem("public_key.pem")

    # message to be encrypted
    message = b"Hello World!"

    # encrypt the message using the public key
    ciphertext = asymmetric_encryption.encrypt(message)

    # print the ciphertext
    print(f'Asymmetric Encrypt: {ciphertext}')

    # decrypt the ciphertext using the private key
    plaintext = asymmetric_encryption.decrypt(ciphertext)

    # print the decrypted plaintext
    print(f'Asymmetric Decrypt: {plaintext}')

def symmetric():

    # create an instance of SymmetricEncryption
    symmetric_encryption = SymmetricEncryption()

    # get the symmetric key
    key = symmetric_encryption.get_key()

    # save the symmetric key to a file
    symmetric_encryption.save_key("key.txt")

    # load the symmetric key from a file
    symmetric_encryption.load_key("key.txt")

    # message to be encrypted
    message = b"Hello World!"

    # encrypt the message using the symmetric key
    ciphertext = symmetric_encryption.encrypt(message)

    # print the ciphertext
    print(f'Symmetric Encrypt: {ciphertext}')

    # decrypt the ciphertext using the symmetric key
    plaintext = symmetric_encryption.decrypt(ciphertext)

    # print the decrypted plaintext
    print(f'Symmetric Decrypt: {plaintext}')

    # print the symmetric key
    print(f'Symmetric Key: {key}')


asymmetric()
symmetric()