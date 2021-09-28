import os
arq = open(os.path.dirname(os.path.abspath(__file__))+'/palavras_2.txt', 'r', encoding ='utf8')
accent = set('áéíóúàèìòùâêîôûãõ')
for line in arq:
    if any(char in line for char in accent):
        print(line)



print(os.stat(os.path.dirname(os.path.abspath(__file__))+'/palavras_2.txt').st_size)
arq.close()
