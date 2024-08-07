# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=prev.next
        next=curr.next
        count=1
        list_=[]
        prev_loc=None
        min_=99999
        while next != None:
            if next == None:
                break
            if ((curr.val > prev.val) and (curr.val > next.val)) or ((curr.val < prev.val) and (curr.val < next.val)):
                list_.append(count)
                if prev_loc is not None:
                    min_=min(min_,(count-prev_loc))
                prev_loc=count
            count+=1
            prev=curr
            curr=next
            next=next.next
        if len(list_) < 2:
             return [-1,-1]
        max_=list_[-1]-list_[0]
        return [min_,max_]