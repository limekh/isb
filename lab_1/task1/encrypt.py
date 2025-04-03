from consts import ALPHABET


def create_custom_alphabet(key: str) -> list[str]:
    """
    Changes the original alphabet to the replacement alphabet for encryption
    :param key: The code word
    :return: The replacement alphabet
    """
    key_processed = []
    for char in key.upper():
        if char not in key_processed and char in ALPHABET:
            key_processed.append(char)

    custom_alphabet = key_processed + [char for char in ALPHABET if char not in key_processed]
    return custom_alphabet


def keyword_cipher(text: str, key: str) -> str:
    """
    Encrypts text with given replacement alphabet
    :param text: The text to encrypt
    :param key: The replacement alphabet
    :return:
    """
    custom_alphabet = create_custom_alphabet(key)

    result = []
    for char in text:
        if char.upper() in ALPHABET:
            index = ALPHABET.index(char.upper())
            if char == char.lower():
                result.append(custom_alphabet[index].lower())
            else:
                result.append(custom_alphabet[index])
        else:
            result.append(char)

    return ''.join(result)
