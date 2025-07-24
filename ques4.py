res=[]
s=input()
t=input()
substr=[]
n=len(t)
temp=t
for i in range(len(s)):
    m=s[i]
    substr.append(m)
    for j in range(i+1,len(s)):
        m=m+s[j]
        if len(m)>=n:
            substr.append(m)           
for se in substr:
    unq=[]
    for ch in se:
        if ch not in unq:
            unq.append(ch)
    m=''.join(res)
    if len(unq)==n and m in :
        res.append(se)
print(res)
final_res=""
min_len=99999
for s in res:
    if len(s)<min_len:
        final_res=s
        min_len=len(s)
print(final_res)


        
