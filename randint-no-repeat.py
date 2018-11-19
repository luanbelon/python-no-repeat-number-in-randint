from random import randint
import time
'''c = {};
for c in range(0,15):
    print(randint(0,25))
    time.sleep(3)'''


lotofacil = []
megasena = []
quina = []
lotomania = []


while len(lotofacil) != 15:
    r = randint(1, 25)
    '''time.sleep(2)'''
    if r not in lotofacil:
        lotofacil.append(r)
print(f'Lotofacil: {sorted(lotofacil)} \n')

while len(megasena) != 6:
    r = randint(0, 99)
    '''time.sleep(2)'''
    if r not in megasena:

        megasena.append(r)
print(f'Megasena: {sorted(megasena)} \n')

while len(quina) != 5:
    r = randint(1, 80)
    '''time.sleep(2)'''
    if r not in quina:

        quina.append(r)
print(f'Quina: {sorted(quina)} \n')

#lotomania

while len(lotomania) != 50:
    r = randint(0, 99)
    '''time.sleep(2)'''
    if r not in lotomania:

        lotomania.append(r)
print(f'Lotomania: {sorted(lotomania)}')
