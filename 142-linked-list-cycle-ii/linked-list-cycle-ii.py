# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        Hash_set=set()
        while temp:
            if temp in Hash_set:
                return temp
            Hash_set.add(temp)
            temp=temp.next
        return None
            

        