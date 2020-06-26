# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head == None: return None
        s = set()
        s.add(head.val)
        p = head
        while p.next != None:
            if p.next.val not in s:
                s.add(p.next.val)
                p = p.next;
            else:
                p.next = p.next.next
        return head