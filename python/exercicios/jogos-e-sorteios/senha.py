import random

import string

tamanho = 5
senha = ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

print('a senha gerada foi: {}'.format(senha))