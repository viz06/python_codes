class Solution:
    count=0
    def findKRotation(self,arr,  n):
        for i in range(n-1):
            if(arr[i]>arr[i+1]):
                return i+1
        
        return 0

if __name__=='__main__':
    tc=int(input())
    while tc>0:
        n=int(input())
        a=list(map(int,input().strip().split()))
        ob=Solution()
        ans=ob.findKRotations(a,n)
        print(ans)
        tc=tc-1
    
