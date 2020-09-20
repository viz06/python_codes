def reorder(arr,index,n):
    temp=[0]*(n+1)
    for i in range(n):
        temp[index[i]]=arr[i]
    for i in range(n):
        arr[i]=temp[i]

def print_array(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    
t=int(input())
while(t>0):
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    index=[int(x) for x in input().strip().split()]
    reorder(arr,index,n)
    print_array(arr,n)
    t=t-1
