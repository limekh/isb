from reedsave import *
from task2.decrypt import *


AUTO_KEY = 'task2/auto_key.json'
ENCRYPTED_TEXT = get_text('task2/cod13.txt')
DECRYPTED = decrypt(encrypt_text, read_json('task2/auto_key.json'))
DECRYPTED_TEXT = 'task2/decrypted_text.txt'
FREQ = 'task2/freq.json'
FREQ_RU = 'task2/frequencies.json'
REAL_DECRYPT = decrypt(encrypt_text, read_json('task2/real_key.json'))
REAL_DECRYPTED_TEXT = 'task2/real_decrypt.txt'
