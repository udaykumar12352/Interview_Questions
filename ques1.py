import math
n=int(input("Enter the number:"))
squares=[]
res=0
me=m=1
while(me<n):
    me=m*m
    squares.append(me)
    m=m+1
ind=len(squares)//2
if n<0:
    print("Validation failed.The given number is a non negative number")
if n in squares:
    res=squares.index(n)+1
else:
    while(ind>0 and ind<len(squares)):
        if n>squares[ind] and n<squares[ind+1]:
            res=ind+1
            break
        elif n<squares[ind]:
            ind=ind-1
        else:
            ind=ind+1   
print(res)       
