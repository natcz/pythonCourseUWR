from duze_cyfry import daj_cyfre

def liczba(x):
    x=str(x)
    dlugosc=len(x)
    for i in range(dlugosc):
        j=int(x[i])
        for r in daj_cyfre(j):
           print (r)





liczba(1876)



