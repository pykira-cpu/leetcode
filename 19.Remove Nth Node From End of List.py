'''
Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Solution 1:

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """              
        a = numnodes(head)
        b = head
        if a == 1:
            head = None
            return head
        if a<=n:
            head = head.next
            return head
        for i in range(a-n-1):
            b = b.next
        b.next=b.next.next
        return head
def numnodes(head):
    a = 0
    while head:
        a+=1
        head = head.next
    return a


#Solution 2:

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
 		length = 1
        cur = p = head
        while cur.next:
            length += 1
            cur = cur.next
            if size > n + 1:
                p = p.next
        if length == n:
            return head.next
        else:
            p.next = p.next.next
            return head

'''
The logic here is to move cur forward til n and then start another pointer
 p from begin. When the end of LL is reached, pointer p will be at the required node position.        	
'''