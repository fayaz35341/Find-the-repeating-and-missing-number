class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n=len(arr)
        # s1=sum(arr)
        s1=0
        s1n=int(n*(n+1)//2)
        # s2=sum(i*i for i in arr)
        s2=0
        s2n=int(n*(n+1)*(2*n+1)//6)
        for i in arr:
            s1+=i
            s2+=i*i
        val1=s1-s1n
        val2=s2-s2n
        val2=int(val2//val1)
        x=int(val1+val2)//2
        y=int(x-val1)
        return [x,y]

# //2965. Find Missing and Repeated Values
class Solution:
    def findMissingAndRepeatedValues(self, arr: List[List[int]]) -> List[int]:
        N=len(arr)
        n=N*N
        # s1=sum(arr)
        s1=0
        s1n=int(n*(n+1)//2)
        # s2=sum(i*i for i in arr)
        s2=0
        s2n=int(n*(n+1)*(2*n+1)//6)
        for i in range(N):
            for j in range(N):
                s1+=arr[i][j]
                s2+=arr[i][j]*arr[i][j]
        val1=s1-s1n
        val2=(s2-s2n)//val1
        # val2=int(val2//val1)
        x=int(val1+val2)//2
        y=int(x-val1)
        return [x,y] 
        
