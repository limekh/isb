from encrypt import*
from reedsave import *


ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
KEY = get_text('task1/key.txt')
TEXT = get_text('task1/text.txt')
ENCRYPTED = keyword_cipher(TEXT, KEY)
ENCRYPTED_TEXT = "task1/cipher_text.txt"
