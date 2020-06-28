# easy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head: return None
        visited = set([head.val])
        cur = head
        while cur.next:
            next_item = cur.next
            if next_item.val not in visited:
                visited.add(next_item.val)
                cur = cur.next
            else:
                cur.next = cur.next.next
        return head

def build_list(list_input):
    if len(list_input) == 0:
        return None
    head = ListNode(list_input[0])
    head.next = build_list(list_input[1:])
    return head

def tra(head):
    if head is None:
        return
    print(head.val)
    tra(head.next)

if __name__ == "__main__":
    s = Solution()
    list_input = [1, 2, 3, 3, 2, 1]
    head = build_list(list_input)
    tra(s.removeDuplicateNodes(head))
