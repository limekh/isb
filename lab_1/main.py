from task1.consts import *
from task2.consts import *


def main():
    # task1
    save_text("task1/cipher_text.txt", encrypted)

    # task 2
    save_json('task2/freq.json', freq_analysis(encrypt_text))
    save_json('task2/auto_key.json', create_key(encrypt_text, read_json('task2/frequencies.json')))
    save_text('task2/decrypted_text.txt', decrypt_text)
    save_text('task2/real_decrypt.txt', real_decrypt)


if __name__ == "__main__":
    main()
