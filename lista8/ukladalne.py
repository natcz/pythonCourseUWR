def literki(s):
	slowo={}
	pomocniczy=set()
	for i in range(len(s)):
		if s[i] not in pomocniczy: 
			slowo[s[i]]=1
			pomocniczy.add(s[i])
		else:
			slowo[s[i]]+=1
	return slowo
	

	

def czy_ukladalne(s1,s2):
	pierwsze=literki(s1)
	drugie=literki(s2)
	zbior1=set(pierwsze)
	zbior2=set(drugie)
	ukladalne=True
	for i in range(len(s2)):
		if(s2[i] not in zbior1):
			ukladalne=False
			break
		elif(pierwsze[s2[i]]<drugie[s2[i]]):
			ukladalne=False
			break
		else:
			continue
			
	return ukladalne
		




s1=input("pierwsze słowo:")
s2=input("drugie słowo:")
if (czy_ukladalne(s1,s2)==True):
	print('Można ułozyć',s2,'z',s1)
else:
	print('Nie można ułozyć',s2,'z',s1)
	
