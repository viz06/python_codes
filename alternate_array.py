#code

def rearrange(arr,n):
    temp=[0]*(n+1)
    smallest=0
    largest=n-1
    i=0
    while(i<n):
        temp[i]=arr[largest]
        temp[i+1]=arr[smallest]
        smallest+=1
        largest=largest-1
        i=i+2
        
    for i in range(n):
        arr[i]=temp[i]

def print_array(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()

t=int(input())
while(t>0):
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    rearrange(arr,n)
    print_array(arr,n)
    t=t-1
