''' Problem 1 : 

Two sum:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
def twoSum(nums,target):
	new_list = []
	new_list_2 = []
	for i,num in enumerate(nums):
		rem = target - num 
		
		if rem == num:

			if i != nums.index(rem):
				new_list_2.extend([nums.index(rem),i])
				return new_list_2
			i +=1

		else:
			if rem in nums:
				new_list.extend([i,nums.index(rem)])
				return new_list
			else:
				[]

#testcases
print(twoSum([1,3,4,5],8))
print(twoSum([3,3],6))
print(twoSum([3,2,4],6))

''' There are lots of approaches for this problem like Brute force, One-pass Hash, Two-pass Hash and 
many more
'''
'''
Problem2 : 

Add two numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked
list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# creating linked list
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
 

ll1 = LinkedList()
ll1.head = Node(1)
second = ll1.head.next
second = Node(2)
third = second.next
third = Node(3)

	#ll1.printList() 

#a = [1,2,3,4,5]
#b = a[::-1]
#print(int("".join(map(str,b))))
class ListNode(object):
	def __init__(self,val=0,next=None):
		self.val = val
		self.next = next

class Solution(object):

	def addTwoNumbers(self,l1,l2,carry = 0):
		total = l1.val + l2.val + carry
		carry = total // 10
		result = ListNode(total % 10)

		if l1.next != None or l2.next != None or carry != 0:
			if l1.next == None:
				l1.next = ListNode(0)
			if l2.next == None:
				l2.next = ListNode(0)
			result.next = self.addTwoNumbers(l1.next,l2.next)
		return result 



l1_sample = ListNode()
l1_sample.val = 2

l1_sample.val = 4
l1_sample.val = 3

l2_sample = ListNode()
l2_sample.val = 5
l2_sample.val = 6
l2_sample.val = 4

sol1 = Solution()

print(sol1.addTwoNumbers(l1_sample,l2_sample))

'''
Problem 7:

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer 
range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the
reversed integer overflows.
Complexity Analysis

Time Complexity: O(log(x)). There are roughly log(x) digits in x. 
​
Space Complexity: O(1)
'''
import math
def reverse(x):
	string_number = str(x)
	if string_number[0] == '-':
		string_number = string_number.replace('-','')
		a = int(string_number[::-1])*(-1)
		if math.pow(-2,31)<= a <= math.pow(2,31)-1:
			return a 
		else:
			return 0

	a = int(string_number[::-1])
	if math.pow(-2,31)<= a <= math.pow(2,31)-1:
		return a 
	else:
		return 0 
"""
def reverse(x: int) -> int:  
        if x > 0:  # handle positive numbers  
            a =  int(str(x)[::-1])  
        if x <=0:  # handle negative numbers  
            a = -1 * int(str(x*-1)[::-1])  
        # handle 32 bit overflow  
        mina = -2**31  
        maxa = 2**31 - 1  
        if a not in range(mina, maxa):  
            return 0  
        else:  
            return a
"""
#testcases
print(reverse(-987))
print(reverse(120))
print(reverse(-200))
print(reverse(1147483648))# reverse(2**31) must return 0
print(reverse(1534236469))
