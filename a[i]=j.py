import array as arr

def rearrange(a,n):
    temp=[0]*(n+1)
    for i in range(n):
        temp[a[i]]=i

    for i in range(n):
        a[i]=temp[i]

a=arr.array('i',[1,3,0,2])
n=len(a)
rearrange(a,n)
for i in range(n):
    print(a[i],end=" ")
    
