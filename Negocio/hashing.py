from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import base64
import os


class Encryption:
    def __init__(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()
        self.aes_key = os.urandom(32) 

    @staticmethod
    def hash_data(data):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(data.encode('utf-8'))
        return base64.b64encode(digest.finalize()).decode()

    def encrypt_aes(self, plaintext):
        iv = os.urandom(16)  
        cipher = Cipher(algorithms.AES(self.aes_key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted = encryptor.update(plaintext.encode()) + encryptor.finalize()
        return base64.b64encode(iv + encrypted).decode()

    def decrypt_aes(self, encrypted_text):
        encrypted_data = base64.b64decode(encrypted_text)
        iv = encrypted_data[:16]
        encrypted_message = encrypted_data[16:]
        cipher = Cipher(algorithms.AES(self.aes_key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        return (decryptor.update(encrypted_message) + decryptor.finalize()).decode()

    def encrypt_rsa(self, plaintext):
        ciphertext = self.public_key.encrypt(
            plaintext.encode(),
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        return base64.b64encode(ciphertext).decode()

    def decrypt_rsa(self, encrypted_text):
        encrypted_data = base64.b64decode(encrypted_text)
        plaintext = self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        return plaintext.decode()

    def export_keys(self):
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return private_pem.decode(), public_pem.decode()
