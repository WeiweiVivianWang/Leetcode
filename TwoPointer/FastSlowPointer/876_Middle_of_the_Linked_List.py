# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        if head is None: return None
        
        fast = slow = head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            
        return slow
    
## linklist： node不可以是none 但是node.next 可以使为none
##此题 因为有限定“If there are two middle nodes, return the second middle node.”
##所以 需要while fast is not None and fast.next is not None:
##一定要加 fast is not none这个条件 因为linkedlist node不能为none

##若while fast.next is not None and fast.next.next is not None:---> 得到的是first middle node

#Time O(N) N is the number of nodes in the given list
#Space O(1) the space used by slow and fast