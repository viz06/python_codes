def minimum(arr,n):
    if(arr[0]<arr[n-1]):
        return arr[0]
    else:
        for i in range(n-1):
            if(arr[i]>arr[i+1]):
                return arr[i+1]
                break
   
t=int(input())
while(t>0):
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    sm=minimum(arr,n)
    print(sm)
    t=t-1
