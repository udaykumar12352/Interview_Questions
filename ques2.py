n=int(input("enter size of array:"))
arr=[]
res=[]
i=j=0
for _ in range(n):
    m=int(input())
    arr.append(m)
k=int(input("Enter k value:"))
if arr[0]>=k:
    print("no valid pair")
fore=0
back=1
while(fore<len(arr) and back<len(arr) and fore<=back):
    if back<n and arr[fore]+arr[back]<k:
        res.append([fore,back])
    back=back+1
    if back>=n or arr[fore]+arr[back]>=k:
        fore=fore+1
        back=fore+1    
print(res)
        
        
        
        
    
