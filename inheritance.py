class person:
	def __init__(self,fname,lname):
		self.fname=fname;
		self.lname=lname;
	def display(self):
		print("name:"+self.fname+"  "+self.lname);

class emp(person):
	def __init__(self,fname,lname,salary):
		person.__init__(self,fname,lname);
		self.salary=salary;
	def display(self):
		person.display(self);
		print("salary:{}".format(self.salary));
#p=person("a","b");
#p.display();

e=emp("a","b",50000);
e.display();
