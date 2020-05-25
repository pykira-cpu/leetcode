'''
Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
'''
#method 1
def removeDuplicates(nums): #space complexity - O(n)
	new_list =[]
	for num in nums:
		if num in new_list:
			new_list.remove(num)
		new_list.append(num)

	return len(new_list)

#print(removeDuplicates([0,0,1,1,1,2,2,2,3,3,4]))

#method 2 - Using two pointer method(preferred)
def removeDuplicates2(nums): #space complexity - O(1) 
	if len(nums)==0:
		return 0
	j = 0
	for i in range(len(nums)):

		if nums[i] != nums[j]:
			j += 1
			nums[j] = nums[i]

	return j+1

print(removeDuplicates2([1,1,2]))
print(removeDuplicates2([1,1,2,3,4,5,5,5,6]))

'''
Best Time to Buy and Sell Stock II

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4             

'''
#Solution 1 : Naive method (120/200 testcases passed) - failed
# Space complexity - O(n)
#Time Complexity - O(n)
def maxProfit(prices):
	maxprofit =[]

	if prices != sorted(prices):
		i = 0
		while(i<len(prices)-1):
			if prices[i] < prices[i+1]:
				maxprofit.append(prices[i+1] - prices[i])
				i += 2
			else:
				i += 1
		
		return sum(maxprofit)
	else:
		n = len(prices)-1
		maxprofit.append(prices[n]-prices[0])
		return sum(maxprofit)


#print(maxProfit([7,1,5,3,6,4]))
#print(maxProfit([7,6,4,3,1]))
#print(maxProfit([1,2,3,4,5]))
#print(maxProfit([6,1,3,2,4,7]))#should be 7 but obtained 4

'''Solution 2 - One simple Pass(adding up profits at each at every transaction)
Space complexity - O(1)
Time complexity - O(n)
'''

def maxProfit2(prices):
	maxprofit = 0
	for i in range(len(prices)-1):
		if prices[i]<prices[i+1]:
			maxprofit += prices[i+1]-prices[i]
			print(maxprofit)
	return maxprofit

#print(maxProfit2([6,1,3,2,4,7]))

'''
Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0


Method 1- Naive method: Taking the help of a copied array
34 / 35 test cases passed.
Status: Time Limit Exceeded
'''
def rotate(nums,k):
	if k==0:
		return nums
	i = 1
	while(i<=k):
		nums_ref = nums[:]
		for j in range(len(nums)-1,0,-1):
			nums[j] = nums[j-1]
		nums[0] = nums_ref[-1]
		i +=1
	return nums


#print(rotate(nums = [1,2,3,4,5,6,7], k = 3))
#print(rotate( nums = [-1,-100,3,99], k = 2))

'''
Method 2 - Brute Force

Time complexity - O(k*n)
Space complexity - O(1)

34 / 35 test cases passed.
Status: Time Limit Exceeded
'''
def rotate2(nums,k):
	for i in range(k):
		previous = nums[-1]
		for j in range(len(nums)):
			nums[j],previous = previous,nums[j]
	return nums
		
#print(rotate2(nums = [1,2,3,4,5,6,7], k = 3))


'''
Using Reverse Algorithm

This approach is based on the fact that when we rotate the array k times, k elements from the back end of the array
come to the front and the rest of the elements from the front shift backwards.

In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by 
reversing the rest n−k elements gives us the required result.



class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    def rotate3(self, nums: List(int), k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
'''
'''
 Contains Duplicate:

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
'''
Method 1 : Naive

Time complexity - O(n^2), O(n) for iterating through nums and another O(n) is for searching duplicates.
Space complexity - O(n), extra array used.

17 / 18 test cases passed.
Status: Time Limit Exceeded
'''
def containsDuplicate(nums):
	dup = 0
	lst = []
	for num in nums:
		if num in lst:
			dup += 1
		lst.append(num)
	if dup != 0:
		return True
	return False

#print(containsDuplicate([1,2,3,4,5]))
#print(containsDuplicate([0,1,2,2,3,4]))

'''
Method 2 - Sorting
As the python in-built sorting function uses Heap sort, it's worst case is O(nlogn) for Time complexity.
Space complexity is constant - O(1)
18 / 18 test cases passed.
Status: Accepted
Runtime: 112 ms
Memory Usage: 16.9 MB

'''
def containsDuplicate2(nums):
	nums = sorted(nums)
	for i in range(len(nums)-1):
		if nums[i]==nums[i+1]:
			return True
	return False

#print(containsDuplicate2([1,2,3,4,5,5]))
#print(containsDuplicate2([8,4,5,2,1,9,0,6]))


''' 
Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

'''
Method 1 : Naive 
Time complexity - O(n^2) ,because we initially did sorting and then searching through n elements. 
Space complexity - O(1), constant space. Nothing extra used.

16 / 16 test cases passed.
Status: Accepted
Runtime: 76 ms
Memory Usage: 14.7 MB
'''

def singlenumber(nums):
	nums = sorted(nums)
	if len(nums)==1:
		return nums[0]
	for i in range(1,len(nums)-1):
		if nums[i-1]!= nums[i] and nums[i]!=nums[i+1]:#if the single number is in between the other elements
			return nums[i]
		elif nums[0]!= nums[1]:#if the single number is our first element
			return nums[0]
		elif nums[len(nums)-1]!=nums[len(nums)-2]:#if the single number is our last element
			return nums[len(nums)-1] 

print(singlenumber([4,1,2,1,2]))
print(singlenumber([2,2,1]))
print(singlenumber([1]))
