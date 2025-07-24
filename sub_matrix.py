k=int(input())
matrix=[[1,2,-1,4],[-8,-3,4,2],[3,8,10,-8],[-4,-1,1,7]]
'''n=int(input("enter dimensions(rows) of array"))
for i in range(n):
    sub=[]
    for j in range(n):
        sub.append(int(input()))
    matrix.append(sub)'''
rows,cols=len(matrix),len(matrix[0])
i=0
j=1
def generate1(m,a,b):
    tmp=[]
    for x in range(a,b-1):
        for y in range(a+1,b):
            tmp.append(m[x][y])
    return tmp   
total_subs=[]
am=generate1(matrix,i,cols)
total_subs.append(am)
def generate_rows(m,i,j):
    tmp=[]
    for x in range(i,j):
        for y in range(i,j):
            tmp.append(m[x][y])           
    return tmp
def generate_cols(m,i,j):
    tmp=[]
    for x in range(i,j):
        for y in range(i-1,j-1):
            tmp.append(m[x][y])
    return tmp
while i+k<=rows:
    ab=generate_rows(matrix,i,i+k)
    total_subs.append(ab)
    i+=1
while j+k<=cols:
    ab=generate_cols(matrix,j,j+k)
    total_subs.append(ab)
    j+=1
max_sum=-999
print(total_subs)
for arr in total_subs:
    if sum(arr)>max_sum:
        max_sum=sum(arr)
print(max_sum)

    


        




