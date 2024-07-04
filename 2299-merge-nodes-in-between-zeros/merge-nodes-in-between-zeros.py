# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        start = head
        while curr.next != None:
            if curr.val == 0:
                start=curr
                if curr.next is None:
                    curr = None
                else:
                    curr = curr.next
            else:
                start.val += curr.val
                start.next = curr.next
                curr = curr.next
        curr = head
        while curr.next != None:
            if curr.next.val == 0:
                curr.next = None
                break
            curr = curr.next
        return head