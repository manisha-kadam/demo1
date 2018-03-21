num=input("enter number:")
for i in range(2,num/2):
	if (num%i)==0:
		print "%d is not prime"% num
		break
else:
	print "%d is prime"% num
