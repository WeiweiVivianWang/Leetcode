# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#http://fisherlei.blogspot.com/2013/11/leetcode-linked-list-cycle-ii-solution.html
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return None
#check whether there is a cycle
 # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an entrance to
        # a cycle.        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
# To find the entrance to the cycle, we have two pointers traverse at
       # the same speed -- one from the front of the list, and the other from
        # the point of intersection.     
        if fast == slow:
            fast = head   
            while fast != slow:
                fast = fast.next
                slow = slow.next
                
            return slow
        
        return None
            
#Time O(n)
#Space O(1)