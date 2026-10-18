# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashset = set()

        curr = headA 
        while curr is not None:
            hashset.add(curr)
            curr = curr.next 
        curr = headB 
        while curr is not None:
            if curr in hashset:
                return curr
            curr = curr.next
        
        return None