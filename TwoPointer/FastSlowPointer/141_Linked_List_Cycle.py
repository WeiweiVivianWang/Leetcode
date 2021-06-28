# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

#Time O(n) n is the total number of nodes in the linkedlist.
# no cycle: the fast pointer reaches the end first and run time depends on the list's length, which is O(n)
# has cycle: 
#1. The slow pointer takes "non-cyclic length" steps to enter the cycle. At this point, the fast pointer has already reached the cycle. 
#Number of iterations=non-cyclic length=N
#2.Both pointers are now in the cycle. Consider two runners running in a cycle - the fast runner moves 2 steps while the slow runner moves 
# 1 steps at a time. Since the speed difference is 1, it takes (difference between the 2 runners/difference of speed) loops
#for the fast runner to catch up with the slow runner. As the distance is at most "cyclic length K" and the speed difference
# is 1, we conclude that Number of iterations=almost "cyclic length K
#Therefore, the worst case time complexity is O(N+K)which is O(n).

#space O(1) we only used two nodes (slow and fast)
