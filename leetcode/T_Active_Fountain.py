#https://leetcode.com/discuss/interview-question/363036/twitter-oa-2019-activate-fountain

# https://leetcode.com/discuss/interview-question/363036/walmart-oa-2019-activate-fountains

def activateFountains(A):
    if not A: 
        return 0
    # For all left end of interval, store the largest right end
    n = len(A)
    aux = [0 for i in range(n+1)]
    
    for i, x in enumerate(A, 1):
        aux[max(i - x, 1)] = max(min(i + x, n),aux[max(i - x, 1)])
    #print(aux)

    ans, l, r = 0, 1, aux[1]
    while r <= n:
        new_r, ans = r, ans + 1
        # If the fountain ranges overlap
        # get the rightmost bound for next search
        while l <= r:
            new_r = max(new_r, aux[l])
            l += 1
        if l > n: break
        # If the fountain ranges don't overlap
        r = max(new_r, aux[l])
    return ans  

print(activateFountains([10,0,0,3,0,0,2,0,0]),1)
print(activateFountains([0,0,0,3,0,0,2,0,0]), 2)
print(activateFountains([3,0,2,0,1,0]), 2)
print(activateFountains([3,0,1,0,1,0]), 2)
print(activateFountains([3,0,1,0,0,1]), 2)
print(activateFountains([2,0,2,0,1,0]), 2)
print(activateFountains([2,0,0,0,0]), 3)
print(activateFountains([0,0,0,0,0]), 5)
print(activateFountains([1,2,1]), 1)
print(activateFountains([0,1,0]), 1)
