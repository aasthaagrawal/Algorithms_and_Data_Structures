#https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for t in tasks:
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
        print(d)
        res = []
        index = 0
        while d:
            d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse= True)}
            delKeys = []
            keyCount = n
            for key in d.keys():
                if keyCount>=0:
                    res.append(key)
                    d[key] -= 1
                    keyCount -=1
                    if d[key] == 0:
                        delKeys.append(key)
                else:
                    break
            for key in delKeys:
                del d[key]
            while d and keyCount>=0:
                res.append("*")
                keyCount -=1
        return len(res)
