x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}

#Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = Dict.keys()
Students.sort()
for S in Students:
      print"=".join((S,str(Dict[S])))	
print (Dict['Charlie'])
print(company)
print(emp)
print(profile)
