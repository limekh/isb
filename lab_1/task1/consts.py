from encrypt import*
from reedsave import *


ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key = get_text('task1/key.txt')
text = get_text('task1/text.txt')
encrypted = keyword_cipher(text, key)
