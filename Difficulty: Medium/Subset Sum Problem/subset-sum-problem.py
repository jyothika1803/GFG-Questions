class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n=len(arr)
        dp=[]
        for _ in range(n+1):
            dp.append([-1]*(sum+1))
        def fun(arr,sum,n):
            if sum==0:
                return 1
            if n==0 and sum!=0:
                return 0
            if dp[n][sum]!=-1:
                return dp[n][sum]
            if arr[n-1]>sum:
                dp[n][sum]=fun(arr,sum,n-1)
            else:
                dp[n][sum]=max(fun(arr,sum,n-1),fun(arr,sum-arr[n-1],n-1))
            return dp[n][sum]
        return fun(arr,sum,n)
        
        