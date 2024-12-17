from Negocio.encryption import Encryption

class Decryption:
    def __init__(self):
        self.encryption = Encryption()

    def decrypt_aes_data(self, encrypted_text):
        return self.encryption.decrypt_aes(encrypted_text)

    def decrypt_rsa_data(self, encrypted_text):
        return self.encryption.decrypt_rsa(encrypted_text)
