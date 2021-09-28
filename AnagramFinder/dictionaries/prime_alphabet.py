import os
arq = open(os.path.dirname(os.path.abspath(__file__))+'/palavras_2.txt', 'r', encoding ='utf8')
newarq = open(os.path.dirname(os.path.abspath(__file__))+'/palavras_5.txt', 'w', encoding ='utf8')
alfabet_dict = {'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,'h':19,'i':23,'j':29,'k':31,'l':37,
                'm':41,'n':43,'o':47,'p':53,'q':59,'r':61,'s':67,'t':71,'u':73,'v':79,'w':83,'x':89,
                'y':97,'z':101,'ç':103,'A':2,'B':3,'C':5,'D':7,'E':11,'F':13,'G':17,'H':19,'I':23,'J':29,
                'K':31,'L':37,'M':41,'N':43,'O':47,'P':53,'Q':59,'R':61,'S':67,'T':71,'U':73,'V':79,'W':83,
                'X':89,'Y':97,'Z':101,'Ç':103}
for line in arq:
    product = 1
    line = line.strip()
    for char in line:
        if char in alfabet_dict:
            product *= alfabet_dict[char]

    newline = line + " = " + str(product) + "\n"
    newarq.write(newline)

arq.close()
newarq.close()
print("done")
