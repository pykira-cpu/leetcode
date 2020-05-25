'''
Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that
you cannot load all elements into the memory at once?
'''
'''
Method 1: Naive
Time complexity - O(n*m)
Space Complexity - O(m)

61 / 61 test cases passed.
Status: Accepted
Runtime: 104 ms
Memory Usage: 13 MB
'''

def intersect(nums1,nums2):
	intersection = []
	#finding the array of greater length 
	if len(nums1)>=len(nums2):
	    larger = nums1
	    smaller = nums2
	else:
	    larger = nums2
	    smaller = nums1
	#intersection of smaller to larger
	for i in smaller:
		for j in range(len(larger)):
			if i == larger[j]:
				intersection.append(larger[j])
				larger[j]=None
				break
		
	return intersection

	
#print(intersect([1,2,2,1],[2,2]))
#print(intersect([4,9,5],[9,4,9,8,4]))
#print(intersect([1,1,2],[1,2,3]))
#print(intersect([3,1,2],[1,1]))

'''
Plus One
Solution
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
'''
Method 1: Naive

109 / 109 test cases passed.
Status: Accepted
Runtime: 24 ms
Memory Usage: 12.7 MB
'''

def plusOne(digits):
	"""
	:type digits: List[int]
	:rtype: List[int]
	"""
	numsplusOne = int(''.join(map(str,digits)))+1 # breaking the list to combined integer and adding 1
	#print(numsplusOne)
	numsplusOne = list(str(numsplusOne))
	return [int(i) for i in numsplusOne]

#testcases	
print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([4,9,9,9]))

'''
Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order
of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
'''
Naive method:

21 / 21 test cases passed.
Status: Accepted
Runtime: 976 ms
Memory Usage: 13.9 MB
'''
def moveZeroes(nums):
	counter = nums.count(0)
	while counter>0:
		for i in range(len(nums)-1):
			if nums[i]==0:
				nums[i],nums[i+1]=nums[i+1],nums[i]
		counter -= 1
	return nums


#print(moveZeroes([0,1,0,3,12]))
#print(moveZeroes([1,2,3,4,0,0,2,3]))

