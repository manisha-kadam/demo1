import re

def main1():
	print("Hello");
	print(":".join("Python"))
	word="guru99 career guru99"
#	r1=re.findall("^\w+",word)
	r1=re.split('s',word)
	print r1		
	print(word.split('r'))	
	Tup1 = (50,);
	tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
	tup2 = (1,2,3,4,5,6,7);
	print(tup1[0])
	print(tup2[-1])

if __name__=="__main__":
	main1();

