# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        mp=set(nums)
        while head and head.val in mp:
            head=head.next
        curr=head
        while curr and curr.next:
            while curr.next and curr.next.val in mp:
                curr.next=curr.next.next
            curr=curr.next
        return head
        