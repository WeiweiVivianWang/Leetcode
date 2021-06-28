# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        res = ListNode(0)
        res.next = head
        fast = slow = res
        
        for i in range(n):
            fast = fast.next
            
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return res.next
        
#先让快指针走n步，然后快慢一起走，走到头的时候慢指针指向的点删掉。

#Time O(L) The algorithm makes one traversal of the list of  L nodes. Therefore time complexity is  O(L).
#Space O(1)