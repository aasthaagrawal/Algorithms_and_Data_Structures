#https://leetcode.com/discuss/interview-question/383669/

m=[[1, 2, 3],[4, 5, 1],[6,2,3]]
numR=len(m)
numC=len(m[0])
dp=[[0 for j in range(numC)] for i in range(numR)]
for j in range(1,numC):
    if j==1:
        dp[0][j]=m[0][j]
    else:
        dp[0][j]=min(dp[0][j-1],m[0][j])
for i in range(1,numR):
    if i==1:
        dp[i][0]=m[i][0]
    else:
        dp[i][0]=min(dp[i-1][0],m[i][0])
for i in range(1,numR):
    for j in range(1,numC):
        x=max(dp[i-1][j],dp[i][j-1])
        dp[i][j]=min(x,m[i][j])
print(max(dp[-1][-2],dp[-2][-1]))
