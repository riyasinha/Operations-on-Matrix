def swapRows(A,r1,r2):
	temp=A[r1]
	A[r1]=A[r2]
	A[r2]=temp
	return A

def Row_Transformation(A,x,r1,r2):
	length=len(A[0])
	for p in range(0,length):
		A[r2][p]=round(A[r2][p]+x*A[r1][p],6)
	return A
def Matrix(A):
        return()

def MatrixRank(A):
	cl=len(A[1])
	rl=len(A)
	rank=rl
	
	limit=min(cl,rl)
	
	for m in range(0,min(cl,rl)):
		if A[m][m] !=0:
			for n in range(m+1,rl):
				if A[n][m]!=0:
					A=Row_Transformation(A,-(A[n][m]/A[m][m]),m,n)
					
		else:
			for n in range(m,rl):
				if A[n][m]!=0:
					A=swapRows(A,n,m)
					
					m-=1
					break
		

	f=0
	for m in range(0,rl):
		count=0
		for n in range(0,cl):
			if A[m][n]==0 :
				count+=1
				
		if count==cl:
			f+=1
			
	rank=rank-f
	print(A)
	return rank



