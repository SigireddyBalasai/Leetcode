# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        next=head.next.next
        prev=head
        curr=head.next
        count=1
        list_=[]
        prev_loc=None
        min_=99999
        while next != None:
            if prev == None or next == None:
                continue
            if (curr.val > prev.val) and (curr.val > next.val):
                list_.append(count)
                if prev_loc is not None:
                    min_=min(min_,(count-prev_loc))
                prev_loc=count
            if (curr.val < prev.val) and (curr.val < next.val):
                if prev_loc is not None:
                    min_=min(min_,(count-prev_loc))
                print(min_,count,prev_loc)
                list_.append(count)
                prev_loc=count
            count+=1
            prev=curr
            curr=next
            next=next.next
        if len(list_) < 2:
             return [-1,-1]
        max_=abs(list_[-1]-list_[0])
        return [min_,max_]