from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

from fileManager import FilesManager


class Symmetric:

    @staticmethod
    def generate_key(key_len):
        if key_len not in [64, 128, 192]:
            raise ValueError("Wrong key length! Must be 64, 128 or 192 bits!")
        key = os.urandom(key_len // 8)
        return key

    @staticmethod
    def encrypt_text(key, text_name, path_to_save):
        plaintext = FilesManager.get_bytes(text_name)
        iv = os.urandom(8)  # 3DES использует 8-байтовый IV

        # Применяем padding к данным
        padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
        padded_text = padder.update(plaintext) + padder.finalize()

        # Шифруем
        cipher = Cipher(
            algorithms.TripleDES(key),
            modes.CBC(iv),
        )
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_text) + encryptor.finalize()

        FilesManager.write_bytes(path_to_save, ciphertext)

    @staticmethod
    def decrypt_text(key, ciphertext_path, path_to_save):
        cipher_text = FilesManager.get_bytes(ciphertext_path)
        iv = cipher_text[:8]

        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(cipher_text) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
        depadder_dc_text = unpadder.update(decrypted_text) + unpadder.finalize()

        FilesManager.write_txt(path_to_save, depadder_dc_text.decode('UTF-8'))
        return depadder_dc_text.decode('UTF-8')

    @staticmethod
    def serialization_symmetric_key(path_to_save, key):
        FilesManager.write_bytes(path_to_save, key)

    @staticmethod
    def deserialization_symmetric_key(file_name):
        return FilesManager.get_bytes(file_name)
