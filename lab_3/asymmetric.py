from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


class Asymmetric:

    @staticmethod
    def generate_keys():
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
        return private_key, private_key.public_key()

    @staticmethod
    def encrypt_symmetric_key(public_key, symmetric_key):
        return public_key.encrypt(
            symmetric_key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )

    @staticmethod
    def decrypt_symmetric_key(private_key, symmetric_key):
        return private_key.decrypt(
            symmetric_key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
