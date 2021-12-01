#https://leetcode.com/problems/maximum-frequency-stack/
#Time Complexity: O(1) for both push and pop
#Space complexity: O(N)

class FreqStack:
    import heapq
    from collections import defaultdict

    def __init__(self):
        self.max_freq = 0
        self.freq_d = defaultdict(int)
        self.freq_group = defaultdict(list)


    def push(self, val: int) -> None:
        self.freq_d[val] += 1
        if self.freq_d[val] > self.max_freq:
            self.max_freq = self.freq_d[val]
        self.freq_group[self.freq_d[val]].append(val)


    def pop(self) -> int:
        ele = self.freq_group[self.max_freq].pop()
        if not self.freq_group[self.max_freq]:
            self.max_freq -= 1
        self.freq_d[ele] -= 1
        return ele


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
