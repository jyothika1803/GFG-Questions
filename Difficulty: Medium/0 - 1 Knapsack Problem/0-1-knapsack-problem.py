class Solution:
    def knapsack(self, W, val, wt):
        # code here
        n=len(wt)
        dp=[]
        for _ in range(n+1):
            dp.append([-1]*(W+1))
        
        def fun(n,W,val,wt):
            if n==0 or W==0:
                return 0
            if dp[n][W]!=-1:
                return dp[n][W]
            # include & exclude that val
            if wt[n-1]<=W:
                dp[n][W]=max((val[n-1] + fun(n-1, W - wt[n-1], val, wt)), fun(n-1, W, val, wt))
            #exclude the value if it is greater than W
            else:
                dp[n][W]=fun(n-1,W,val,wt)
            return dp[n][W]
        result=fun(n,W,val,wt)
        return result
