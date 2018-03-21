m=input("enter rows:")
n=input("enter columns:")
matrix = [[0 for j in range(n)] for i in range(m)]
for i in range(0,m):
	for j in range(0,n):
		matrix[i][j]=input()

print (matrix)
