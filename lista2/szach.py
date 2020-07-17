def szachownica(n,k):
    for i in range(2*n):
        if i%2==0: 
          for p in range(k):
              for m in range(n):
                 print(k*" ",k*"#",sep="",end="")
              print()
             
              
                
        else:
             for p in range(k):
                 for m in range(n):
                    print(k*"#",k*" ",sep="",end="")
                 print()
                 
            




szachownica(5,2)

