#https://leetcode.com/problems/string-compression/
#Complexity: O(n)

class Solution:
    def compress(self, chars: List[str]) -> int:
        origStrLen=len(chars)
        currChar=chars[0]
        count=1
        index=0
        for i in range(1,origStrLen):
            if chars[i] is not currChar:
                chars[index]=currChar
                currChar=chars[i]
                index+=1
                if count>1:
                    for i in str(count):
                        if index==i:
                            chars.insert(index,i)
                        else:
                            chars[index]=i
                        index+=1
                count=0
            count+=1
        chars[index]=currChar
        index+=1
        if count>1:
            for i in str(count):
                chars.insert(index,i)
                index+=1
        del chars[index:]
        return index
