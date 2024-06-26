# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        head = ListNode()
        curr = head
        while(curr1  and curr2):
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
                curr = curr.next
            else:
                curr.next = curr2
                curr2 = curr2.next
                curr = curr.next
        if curr1 != None:
                curr.next = curr1
                curr = curr.next
        if curr2 != None:
                curr.next = curr2
                curr = curr.next
        return head.next