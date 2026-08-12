# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        curr=head
        len=1
        while(curr.next!=None):
            curr=curr.next
            len+=1
        
        pos_from_start=len-n
        #if we want to remove head
        if(pos_from_start==0):
            return head.next
            
        for i in range(pos_from_start-1):
            temp=temp.next

        temp.next=temp.next.next

        return head