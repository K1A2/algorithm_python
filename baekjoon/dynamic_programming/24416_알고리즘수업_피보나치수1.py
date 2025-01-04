a = int(input())
dp=[0]*(a+1)
dp[1]=dp[2]=1
for i in range(3,a+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[a],a - 2)