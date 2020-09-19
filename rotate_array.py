def rotate_one(arr,n,d):
    for i in range(d):
        rotate_array(arr,n,d)

def rotate_array(arr,n,d):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
        arr[n-1]=temp

def print_array(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()

t = int(input())
while(t>0):
    n_d = [int(x) for x in input().strip().split()]
    n = n_d[0]
    d = n_d[1]
    arr=[int(x) for x in input().strip().split()]
    rotate_one(arr,n,d)
    print_array(arr,n)
