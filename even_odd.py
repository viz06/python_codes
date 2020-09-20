def rearrange(arr,n):
    for i in range(n-1):
        if(i%2==0 and arr[i]>arr[i+1]):
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp
        if(i%2!=0 and arr[i]<arr[i+1]):
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp

def print_array(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()
            
t=int(input("Enter no of testcases: "))
while(t>0):
    n=int(input("Enter no of elements in array: "))
    arr=[int(x) for x in input("Enter array: ").strip().split()]
    rearrange(arr,n)
    print_array(arr,n)
    t=t-1
