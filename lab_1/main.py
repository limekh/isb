from task1.consts import *
from task2.consts import *


def main():
    # task1
    save_text(ENCRYPTED_TEXT, ENCRYPTED)

    # task 2
    save_json(FREQ, freq_analysis(ENCRYPTED_TEXT))
    save_json(AUTO_KEY, create_key(ENCRYPTED, read_json(FREQ_RU)))
    save_text(DECRYPTED_TEXT, DECRYPTED)
    save_text(REAL_DECRYPTED_TEXT, REAL_DECRYPT)


if __name__ == "__main__":
    main()
