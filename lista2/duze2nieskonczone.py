from duze_cyfry import daj_cyfre

def liczba(x):
    x=str(x)
    dlugosc=len(x)
    for g in range (4):
        for i in range(dlugosc-1):
            j=x[i]
            print(daj_cyfre(j[g]))
                




liczba(187)
