# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node =  head
        dummy = ListNode(0,head)
        m = 0
        cnt = 0
        while node:
            node = node.next
            cnt+=1
        node = dummy
        while m<cnt-n:
            node=node.next
            m+=1
        node.next = node.next.next
            

        
        return dummy.next