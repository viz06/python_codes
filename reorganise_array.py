#code

def arrange(arr,n):
    x=0
    y=0
    for i in range(n):
        if(arr[i]!=-1 and arr[i]!=i):
            x=arr[i]
            while(arr[i]!=-1 and arr[i]!=x):
                y=arr[x]
                arr[x]=x
                x=y
            arr[x]=x
            if(arr[i]!=i):
                arr[i]=-1

def print_array(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    
    print()
t=int(input())
while(t>0):
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    arrange(arr,n)
    print_array(arr,n)
    t=t-1
