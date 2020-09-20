class Solution:
    def leftRotate(self, arr, k, n):
        for i in range(k):
            temp=arr[0]
            for j in range(n-1):
                arr[j]=arr[j+1]
            arr[n-1]=temp

if __name__=='__main__':

    t=int(input())
    for _ in range(0,t):
        l-list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a=list(map(int,input().split()))
        ob=Solution()
        ob.leftRotate(a,k,n)
        print(*a)
