#https://leetcode.com/problems/design-skiplist/

import random
class Node:
    def __init__(self,val):
        self.val = val
        self.nextNode = None
        self.nextLevelNode = None

class Skiplist:

    def __init__(self):
        self.head = Node(-float("inf"))
        self.maxLevel = 1

    def search(self, target: int) -> bool:
        cur = self.head
        for level in range(self.maxLevel,0,-1):    
            while cur.nextNode and cur.nextNode.val < target:
                cur = cur.nextNode
            if cur.nextLevelNode:
                cur = cur.nextLevelNode
        while cur.nextNode and cur.nextNode.val< target:
            cur = cur.nextNode
        if cur.nextNode and cur.nextNode.val==target:
            return True
        return False

    def add(self, num: int) -> None:
        num_levels = 1
        for i in range(self.maxLevel):
            p = random.uniform(0, 1)
            if p >= 0.5:
                num_levels += 1
        if num_levels > self.maxLevel:
            new_head = Node(-float("inf"))
            new_head.nextLevelNode = self.head
            self.head = new_head
            self.maxLevel += 1
        cur = self.head
        prev_level_new_node = None
        for level in range(self.maxLevel,0,-1):
            while cur.nextNode and cur.nextNode.val < num:
                cur = cur.nextNode
            if num_levels >= level:
                tmp = Node(num)
                tmp.nextNode = cur.nextNode
                cur.nextNode = tmp
                if prev_level_new_node:
                    prev_level_new_node.nextLevelNode = tmp
                prev_level_new_node = tmp
            if cur.nextLevelNode:
                cur = cur.nextLevelNode
    
    def erase(self, num: int) -> bool:
        cur = self.head
        foundAny = False
        for level in range(self.maxLevel, 0, -1):
            while cur.nextNode and cur.nextNode.val <num:
                cur = cur.nextNode
            if cur.nextNode and cur.nextNode.val == num:
                foundAny = True
                tmp = cur.nextNode
                cur.nextNode = tmp.nextNode
                del tmp
            cur = cur.nextLevelNode
        return foundAny
                
        
    def displaySkipList(self):
        print("Printing skiplist")
        headOfLevel = self.head
        for level in range(self.maxLevel,0,-1):
            printset = []
            cur = headOfLevel
            while cur is not None:
                printset.append(cur.val)
                cur = cur.nextNode
            print(printset)
            del printset
            headOfLevel = headOfLevel.nextLevelNode
            
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
