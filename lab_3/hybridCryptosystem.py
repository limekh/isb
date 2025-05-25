from asymmetric import Asymmetric
from fileManager import FilesManager
from symmetric import Symmetric


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
            print("Key len must be 64, 18 or 192")
    sym_key = Symmetric.generate_key(key_len)
    Symmetric.serialization_symmetric_key(sym_key_path, sym_key)

    print("The keys are generated and save successfully")


def encrypt(private_key_path, initial_file_path, encrypted_file_path, sym_key_path):
    print("## Encrypt Mode ##")

    encr_symmetric_key = FilesManager.get_bytes(sym_key_path)
    private_key = FilesManager.read_private_key(private_key_path)
    symmetric_key = Asymmetric.decrypt_symmetric_key(private_key, encr_symmetric_key)
    text = FilesManager.get_txt(initial_file_path)

    Symmetric.encrypt_text(symmetric_key, text, encrypted_file_path)
    print("Text successfully encrypted")


def decrypt(private_key_path, encrypted_file_path, sym_key_path, decrypted_file_path):
    print("## Decrypt Mode ##")

    encr_symmetric_key = FilesManager.get_bytes(sym_key_path)
    private_key = FilesManager.read_private_key(private_key_path)
    symmetric_key = Asymmetric.decrypt_symmetric_key(private_key, encr_symmetric_key)

    Symmetric.decrypt_text(symmetric_key, encrypted_file_path, decrypted_file_path)
    print("Text successfully decrypted")
