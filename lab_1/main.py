from task1.consts import *
from task2.consts import *


def main():
    # task1
    save_text(encrypted_text, encrypted)

    # task 2
    save_json(freq, freq_analysis(encrypt_text))
    save_json(auto_key, create_key(encrypt_text, read_json(freq_ru)))
    save_text(decrypted_text, decrypted)
    save_text(real_decrypted_text, real_decrypt)


if __name__ == "__main__":
    main()
