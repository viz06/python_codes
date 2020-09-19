def rotate_by_one(arr,n):
    temp=arr[n-1]
    for i in range(n):
        arr[n-1-i]=arr[n-i-2]
    arr[0]=temp
    
def print_array(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()

t= int(input())
while(t>0):
    n= int(input())
    arr= [int(x) for x in input().strip().split()]
    rotate_by_one(arr,n)
    print_array(arr,n)
    t=t-1
