#code

def rearrange(arr,n):
    arr.sort()
    arr2=[0]*(n+1)
    index=0
    i=0
    j=n-1
    for i in range(n-1):
        arr2[index]=arr[i]
        index=index+1
        arr2[index]=arr[j]
        index=index+1
        j=j-1
    
    print_array(arr2,n)

def print_array(arr2,n):
    for i in range(n):
        print(arr2[i],end=" ")

t=int(input())
while(t>0):
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    rearrange(arr,n)
    t=t-1
