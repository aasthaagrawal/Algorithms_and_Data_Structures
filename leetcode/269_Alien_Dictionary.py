#https://leetcode.com/problems/alien-dictionary/

class WordNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        words_graph = WordNode("root")
        graph_dict = {}
        indegree = {}

        for i,word in enumerate(words):
            if i >= 1:
                if words[i-1].startswith(words[i]) and words[i]!=words[i-1]:
                    return ""
            node = words_graph
            for ch in word:
                if ch not in graph_dict:
                    graph_dict[ch] = []
                    indegree[ch] = 0
                if not node.children:
                    node.children.append(WordNode(ch))
                elif node.children[-1].val != ch:
                    if ch not in graph_dict[node.children[-1].val]:
                        graph_dict[node.children[-1].val].append(ch)
                        indegree[ch] += 1
                    node.children.append(WordNode(ch))
                node = node.children[-1]

        result = []

        while graph_dict:
            tmp = []
            for key,val in indegree.items():
                if val == 0:
                    tmp.append(key)
                    result.append(key)
            if len(tmp) == 0:
                return ""
            for key in tmp:
                for neighbour in graph_dict[key]:
                    indegree[neighbour] -= 1
                del indegree[key]
                del graph_dict[key]

        return "".join(result)
