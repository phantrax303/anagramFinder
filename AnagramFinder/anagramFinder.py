import tkinter as tk
import os

alfabet_dict = {'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,'h':19,'i':23,'j':29,'k':31,'l':37,
                'm':41,'n':43,'o':47,'p':53,'q':59,'r':61,'s':67,'t':71,'u':73,'v':79,'w':83,'x':89,
                'y':97,'z':101,'ç':103,'A':2,'B':3,'C':5,'D':7,'E':11,'F':13,'G':17,'H':19,'I':23,'J':29,
                'K':31,'L':37,'M':41,'N':43,'O':47,'P':53,'Q':59,'R':61,'S':67,'T':71,'U':73,'V':79,'W':83,
                'X':89,'Y':97,'Z':101,'Ç':103}

root = tk.Tk()
root.title("anagram finder")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

searchFrame = tk.Frame(root)
searchFrame['padx'] = 5
searchFrame['pady'] = 5
searchFrame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E)
searchFrame.grid_columnconfigure(0, weight=1)
searchFrame.grid_columnconfigure(1, weight=8)
searchFrame.grid_columnconfigure(2, weight=1)

anagramFrame = tk.Frame(root)
anagramFrame['padx'] = 5
anagramFrame['pady'] = 5
anagramFrame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.W+tk.E)
anagramFrame.grid_columnconfigure(0, weight=1)
anagramFrame.grid_rowconfigure(0, weight=1)

searchLabel = tk.Label(searchFrame)
searchLabel['text'] = 'word: ' 
searchLabel['padx'] = 5
searchLabel['pady'] = 5
searchLabel.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E)

sv = tk.StringVar()
searchEntry = tk.Entry(searchFrame, textvariable = sv)
searchEntry.grid(row = 0, column = 1, sticky=tk.N+tk.S+tk.W+tk.E)

anagramList = tk.Listbox(anagramFrame)
anagramList.grid(row=0, column=0, sticky= tk.N+tk.S+tk.W+tk.E)

def searchAnagram():
    word = searchEntry.get()
    product = 1
    anagrams = []

    for char in word:
        if char in alfabet_dict:  
            product *= alfabet_dict[char]

    with open(os.path.dirname(os.path.abspath(__file__))+'/dictionaries/palavras_5.txt' , "r", encoding="utf8") as arq:

        for line in arq:
            word2, prime = line.split(" = ", 1)
            prime = int(prime)
            if product == prime:
                if word2 != word:
                    anagrams.append(word2)
        
        arq.close()

    anagramList.delete(0, tk.END)
    for x in anagrams:
        anagramList.insert(tk.END,x)

searchButton = tk.Button(searchFrame, text = "search", command=searchAnagram)
searchButton['padx'] = 5
searchButton['pady'] = 5
searchButton.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)

root.mainloop()

