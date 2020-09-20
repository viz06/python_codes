def rearrange(arr,n):
    min_index=0
    max_index=n-1
    max_elm=arr[n-1]+1
    for i in range(0,n):
        if(i%2==0):
            arr[i]+=(arr[max_index]%max_elm)*max_elm
            max_index-=1
        else:
            arr[i]+=(arr[min_index]%max_elm)*max_elm
            min_index+=1
    for i in range(0,n):
        a[i]=a[i]/max_elm

def print_array(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()

t=int(input("Enter no of test cases: "))
while(t>0):
    n=int(input("Enter no of elements in array: "))
    arr=[int(x) for x in input("Enter array: ").strip().split()]
    rearrange(arr,n)
    print_array(arr,n)
