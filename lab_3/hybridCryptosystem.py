from asymmetric import Asymmetric
from symmetric import Symmetric


class HybridCryptoSystem:
    @staticmethod
    def keys_generator(sym_key_path, public_key_path, private_key_path):
        print("## Keys Generator Mode ##")

        private_key, public_key = Asymmetric.generate_keys()
        Asymmetric.serialization_private_key(private_key_path, private_key)
        Asymmetric.serialization_public_key(public_key_path, public_key)

        key_len = 64
        flag = True
        while flag:
            key_len = int(input("Enter key len: "))
            if key_len in [64, 128, 192]:
                flag = False
            else:
                print("Key len must be 64, 128 or 192")
        sym_key = Symmetric.generate_key(key_len)
        encr_sym_key = Asymmetric.encrypt_symmetric_key(public_key, sym_key)
        Symmetric.serialization_symmetric_key(sym_key_path, encr_sym_key)

        print("## The keys are generated and save successfully ##")

    @staticmethod
    def encrypt(private_key_path, initial_file_path, encrypted_file_path, sym_key_path):
        print("## Encrypt Mode ##")

        symmetric_key = Asymmetric.decrypt_symmetric_key(private_key_path, sym_key_path)
        Symmetric.encrypt_text(symmetric_key, initial_file_path, encrypted_file_path)

        print("## Text successfully encrypted ##")

    @staticmethod
    def decrypt(private_key_path, encrypted_file_path, sym_key_path, decrypted_file_path):
        print("## Decrypt Mode ##")

        symmetric_key = Asymmetric.decrypt_symmetric_key(private_key_path, sym_key_path)
        Symmetric.decrypt_text(symmetric_key, encrypted_file_path, decrypted_file_path)

        print("## Text successfully decrypted ##")
