from reedsave import *
from task2.decrypt import *


auto_key = 'task2/auto_key.json'
encrypt_text = get_text('task2/cod13.txt')
decrypted = decrypt(encrypt_text, read_json('task2/auto_key.json'))
decrypted_text = 'task2/decrypted_text.txt'
freq = 'task2/freq.json'
freq_ru = 'task2/frequencies.json'
real_decrypt = decrypt(encrypt_text, read_json('task2/real_key.json'))
real_decrypted_text = 'task2/real_decrypt.txt'
