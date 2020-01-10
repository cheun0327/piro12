num=int(input())
dp=[]
dp.append(0)
dp.append(0)
for i in range(2,num+1):
    minn = dp[i-1]
    if i%2==0:
        if minn>dp[i//2]:
            minn=dp[i//2]
    if i%3==0:
        if minn>dp[i//3]:
            minn=dp[i//3]
    dp.append(minn+1)
print(dp[num])

