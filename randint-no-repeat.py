from random import randint

lotofacil = []

#enquanto lotofacil for menor igual a 15
while len(lotofacil) != 15:
    
    #r receberá um randint entre 1 e 25 (Numeros disponiveis para jogar na lotofacil)
    r = randint(1, 25)
    
    #condicão se r nao estiver dentro de lotofacil
    if r not in lotofacil:
        
        #lotofacil acrescenta (.append) r a lista
        lotofacil.append(r)
        
#Por ultimo pede para imprimir lotofacil
print(f'Lotofacil: {sorted(lotofacil)} \n')
