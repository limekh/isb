from reedsave import *
from task1.encrypt import *
from task2.decrypt import *


def main():
    # task1
    key = get_text('task1/key.txt')
    text = get_text('task1/text.txt')
    encrypted = keyword_cipher(text, key)
    save_text("task1/cipher_text.txt", encrypted)

    # task 2
    encrypt_text = get_text('task2/cod13.txt')
    save_json('task2/freq.json', freq_analysis(encrypt_text))
    save_json('task2/auto_key.json', create_key(encrypt_text, read_json('task2/frequencies.json')))
    decrypt_text = decrypt(encrypt_text, read_json('task2/auto_key.json'))
    save_text('task2/decrypted_text.txt', decrypt_text)
    real_decrypt = decrypt(encrypt_text, read_json('task2/real_key.json'))
    save_text('task2/real_decrypt.txt', real_decrypt)


if __name__ == "__main__":
    main()
