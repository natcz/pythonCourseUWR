

def  koperta(n):
   print((2*n+1)*"*")
   for i in range(n-1):
       print("*",i*" ","*",sep="",end="")
       print((2*n-3-2*i)*" ",end="")
       print ("*", i*" ","*",sep="")
   print("*",(n-1)*" ",sep="",end="")
   print("*",(n-1)*" ","*",sep="")
   for j in range(n-1):
       print("*",(n-j-2)*" ","*",sep="",end="")
       print((2*j+1)*" ",end="")
       print("*",(n-j-2)*" ","*",sep="")

   print((2*n+1)*"*")
   






koperta(3)
