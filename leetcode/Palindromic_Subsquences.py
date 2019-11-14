#https://leetcode.com/discuss/interview-question/372459/Facebook-or-Phone-Screen-or-Palindromic-Subsequences

s="abac"
n=len(s)
result=[]

def func(subs,index):
    if index==n:
        tmp="".join(subs)
        if tmp==tmp[::-1] and tmp!="":
            result.append(tmp)
        return
    subs.append(s[index])
    func(subs,index+1)
    subs.pop(-1)
    func(subs,index+1)
    
func([],0,)
print(result)
