# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        temp=head
        while temp is not None:
            count+=1
            temp=temp.next
        position=count-n
        if position==0:
            return head.next
        if head is None:
            return None
        temp=head
        count1=0
        while temp is not None and count1<position-1:
            temp=temp.next
            count1+=1
        while temp is None or temp.next is None:
            return None
        temp.next=temp.next.next
        return head


        