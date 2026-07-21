# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tmp = []
        node = head
        if not head or not head.next:
            return None
        while node:
            tmp.append(node.val)
            node=node.next
        node = head
        count = 0
        length = len(tmp)-1
        while node:
            if count%2 ==0:
                # first third ect
                node.val = tmp[round(count/2)]
            else:
                node.val = tmp[length]
                length-=1


            count +=1
            node = node.next

        



        return None
        