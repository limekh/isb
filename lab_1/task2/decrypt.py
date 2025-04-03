from collections import Counter


def freq_analysis(text: str) -> dict[str, float]:
    """
    Creates frequency table for given text
    :param text: Text for create frequency table
    :return: Frequency table
    """
    count = Counter(text)
    frequencies = {letter: count / len(text) for letter, count in count.items() if letter != "\n"}
    return dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))


def create_key(encrypted_text: str, ru_frequencies: dict[str, float]) -> dict[str, str]:
    """
    Creates decryption key, based on a frequency analysis method
    :param encrypted_text: Text to decrypt
    :param ru_frequencies: Frequency table for russian language
    :return: Decryption key
    """
    cur_text_freq = freq_analysis(encrypted_text)
    key = dict()
    for (letter_text, _), (letter_key, _) in zip(cur_text_freq.items(), ru_frequencies.items()):
        key[letter_text] = letter_key
    return key


def decrypt(encrypted_text: str, key: dict[str, float]) -> str:
    """
    Decrypts text with given key
    :param encrypted_text: Text to decrypt
    :param key: key in form of a dict
    :return: Decrypted text
    """
    encrypted_text = encrypted_text.replace("\n", " ")
    decrypted_text = ""
    for letter in encrypted_text:
        match letter in key:
            case True:
                decrypted_text += key[letter]
            case False:
                decrypted_text += letter
    return decrypted_text
