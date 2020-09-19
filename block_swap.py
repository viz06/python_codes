import array as arr

def rearrange(a,n):
    temp=[0]*(n+1)
    count=0
    for i in range(n):
        if(a[i]<0):
            temp[count]=a[i]
            count+=1
    
    while(count<n):
        if(a[i]>=0):
            temp=[count]=a[i]
            count=+1
    
    for i in range(n):
        a[i]=temp[i]

def print_array(a,n):
    for i in range(n):
        print(a[i],end=" ")

a=arr.array[12 11 -13 -5 6 -7 5 -3 -6]
n=len(a)
rearrange(a,n)
print_array(a,n)s
