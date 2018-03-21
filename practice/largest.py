a1=[]
a2=[]
n=input('enter elements:')
for i in range(1,n+1):
	b=input()
	if(b%2==0):
		a1.append(b)
	else:
		a2.append(b)

print a1
print a2
