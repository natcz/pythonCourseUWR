def usun_nawiasy(s):
    jest=True
    for i in range(len(s)):
        
        if s[i]=='(':
           jest=False
        if s[i]==')':
            jest = True
        if jest==True and s[i] != ')':
           print(s[i], end="")


    print()




usun_nawiasy("Ala ma kota (perskiego)!")
usun_nawiasy("Ala (ma) kota (perskiego) i nie je nic mięsnego")
usun_nawiasy("Koty są (wredne) i dużo spią")
