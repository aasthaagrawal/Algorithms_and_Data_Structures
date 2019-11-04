#https://leetcode.com/discuss/interview-question/370157

def numSubstrings(s,k):
    if not s:
        if k==0:
            return 1
        else:
            return 0
    result=0
    n=len(s)
    for i in range(n):
        dist_count=0
        d={}
        for j in range(i,n):
            if s[j] in d:
                d[s[j]]+=1
            else:
                dist_count+=1
                d[s[j]]=1
            if dist_count==k:
                result+=1
                print(s[i:j+1])
            elif dist_count>k:
                break
    return result

s = "pqpqs"
k = 2
print(numSubstrings(s,k))
print("******************")
s = "aabab"
k = 3
print(numSubstrings(s,k))
