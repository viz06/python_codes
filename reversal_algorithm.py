class Solution:
    def leftRotate(self, arr, n, d):
        if d==0:
            return
        rotate(arr,0,d-1)
        rotate(arr,d,n-1)
        rotate(arr,0,n-1)

def rotate(arr,start,end):
    while(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end=end-1
