#https://leetcode.com/problems/letter-tile-possibilities/
#Time limit exceeds

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.result = set()
        self.n = len(tiles)
        tiles = list(tiles)
        self.permute(tiles,0)
        return len(self.result)-1

    def permute(self, tiles, i):
        if i==self.n:
            return
        for j in range(i,self.n):
            tiles[i],tiles[j]=tiles[j],tiles[i]
            self.backtrack(tiles,0,[])
            self.permute(tiles,i+1)
            tiles[i],tiles[j]=tiles[j],tiles[i]

    def backtrack(self,s,i,substring):
        if i==len(s):
            self.result.add("".join(substring))
            return
        self.backtrack(s,i+1,substring)
        substring.append(s[i])
        self.backtrack(s,i+1,substring)
        substring.pop()
