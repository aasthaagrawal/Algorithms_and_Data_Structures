#https://leetcode.com/problems/maximum-frequency-stack/
#Time complexity: O(nlogn) for push and O(1) for pop
#Space complexity: O(n)

class FreqStack:
    import heapq
    from collections import defaultdict

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        self.freq_d = defaultdict(int)
        self.index = 0

    def push(self, val: int) -> None:
        self.freq_d[val] += 1
        heapq.heappush(self.heap, (-self.freq_d[val], -self.index, val))
        self.index += 1

    def pop(self) -> int:
        f,i,v = heapq.heappop(self.heap)
        self.freq_d[v] -= 1
        return v

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
