#code

def pivotedBinarySearch(arr,n,k):
    
    pivot=findPivot(arr,0,n-1);
    
    if pivot==-1:
       return binarySearch(arr,0,n-1,k)
        
        
    if key==arr[pivot]:
        return pivot
    if key>=arr[0]:
        return binarySearch(arr,0,pivot-1,k)
    return binarySearch(arr,pivot+1,n-1,k)

def binarySearch(arr,l,h,k):
    
    if h<l:
        return -1
        
    mid=int((l+h)/2)
    if key==arr[mid]:
        return mid
    if key>arr[mid]:
        return binarySearch(arr,mid+1,h,k)
    return binarySearch(arr,l,mid-1,k)

def findPivot(arr,l,h):
    
    if h<l:
        return -1
    if h==l:
        return l
        
    mid=int(l+(h-l)/2)
    if mid<h and arr[mid]>arr[mid+1]:
        return mid
    if mid>l and arr[mid]<arr[mid-1]:
        return (mid-1)
    if arr[l]>=arr[mid]:
        return findPivot(arr,l,mid-1)
    return findPivot(arr,mid+1,h)

t= int(input())
while(t>0):
    n=int(input())
    arr= [int(x) for x in input().strip().split()]
    key=int(input())
    index=pivotedBinarySearch(arr,n,key);
    print(index)
    t=t-1
