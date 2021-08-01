"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None
        
        dic = {} 
        curr = head #pointer
        
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
        
        for node in dic:
            if node.next is not None:
                dic[node].next = dic[node.next]
            if node.random is not None:
                dic[node].random = dic[node.random]
        return dic[head]
                
        
        
        