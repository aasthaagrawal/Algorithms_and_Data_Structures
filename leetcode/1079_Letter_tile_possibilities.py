#https://leetcode.com/problems/letter-tile-possibilities/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.result = []
        self.n = len(tiles)
        self.tiles = tiles
        self.getPossibleArrangements(0, [])
        return len(set(self.result))

    def getPossibleArrangements(self, cur_ind, arrangement):
        if cur_ind == self.n:
            return
        arrangement.append(self.tiles[cur_ind])
        self.result.append("".join(arrangement))
        self.getPermutations(0, len(arrangement), arrangement)
        self.getPossibleArrangements(cur_ind+1, arrangement)

        arrangement.pop(-1)
        self.getPossibleArrangements(cur_ind+1, arrangement)

    def getPermutations(self, cur_ind, n, st):
        if cur_ind == n-1:
            self.result.append("".join(st))
            return
        for i in range(cur_ind, n):
            st[i], st[cur_ind] = st[cur_ind], st[i]
            self.getPermutations(cur_ind+1, n, st)
            st[i], st[cur_ind] = st[cur_ind], st[i]
