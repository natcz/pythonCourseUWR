alfabet = ['a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n','ń','o','ó','p','r','s','ś','t','u','w','y','z','ź','ż']
alf={}
for i in range(len(alfabet)):
	alf[alfabet[i]]=i
	
def ceasar(s,k):
	wynik=''
	for i in range(len(s)):
		poz=alf[s[i]]
		if(poz+k<=31):
			wynik+=alfabet[poz+k]
		else:
			wynik+=alfabet[(poz+k)%31 -1]
		
	


	return wynik


print(ceasar('zabawkż',15))
