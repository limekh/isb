from reedsave import *
from task2.decrypt import *


encrypt_text = get_text('task2/cod13.txt')
decrypt_text = decrypt(encrypt_text, read_json('task2/auto_key.json'))
real_decrypt = decrypt(encrypt_text, read_json('task2/real_key.json'))
