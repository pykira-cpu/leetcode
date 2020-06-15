'''
Reverse Linked List


Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head): #iterative
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None
        
        while cur:
        	new_cur = cur.next #Remebering the next node
        	cur.next = prev #Reversing None
        	prev = cur # Used in next iteration 
        	cur = new_curr # Move to next node

        return prev


    def reverseList_recursive(self, head):# Recursive
        """
        :type head: ListNode
        :rtype: ListNode
        """     
        if not head or not head.next:
            return head
        
        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return prev 

