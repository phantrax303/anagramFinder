import os
arq = open(os.path.dirname(os.path.abspath(__file__))+'/palavras.txt', 'r', encoding ='utf8')
arqtemp = arq.read()
accent = set('áàâãéèêíìîóòôõúùû')
arq.close()
 
for x in accent:
    if x == 'á' or 'à' or 'â' or 'ã':
        arqtemp = arqtemp.replace(x,'a')
    elif x == 'é' or 'è' or 'ê':
        arqtemp = arqtemp.replace(x,'e')
    elif x == 'í' or 'ì' or 'î':
        arqtemp = arqtemp.replace(x,'i')
    elif x == 'ó' or 'ò' or 'ô' or 'õ':
        arqtemp = arqtemp.replace(x,'o')
    else:
        arqtemp = arqtemp.replace(x,'u')

arqtemp = arqtemp.split('\n')
arqtemp2 = []
for x in arqtemp:
    if x not in arqtemp2:
        arqtemp2.append(x)

for x in range(0,len(arqtemp2)-1):
    arqtemp2[x] = arqtemp2[x].lower()+'\n'

arqtemp2.pop(-1)

arq = open(os.path.dirname(os.path.abspath(__file__))+'/palavras_2.txt', 'w', encoding ='utf8')
arq.writelines(arqtemp2)
arq.close()
print ('done')