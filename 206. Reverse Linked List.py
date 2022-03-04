# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prevnode = None
#         currentnode = head
#         nextnode = None
#         while currentnode:
#             nextnode = currentnode.next
#             currentnode.next = prevnode
#             prevnode = currentnode
#             currentnode = nextnode
        prev = None
        curr = head
        
        while curr:
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node
        
        return prev
        
        #         head = prevnode
#         return head
#         self.prevnode = 0
#         self.currentnode = self.nextnode = head
#         while(nextnode != 0):
#             self.nextnode = self.nextnode -> self.next
#             self.currentnode -> self.next = self.prevnode
#             self.prevnode = self.currentnode
#             self.currentnode = self.nextnode
#         self.head = self.prevnode
#         return head
