'''
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
#Method 1 : failed few test cases
from itertools import combinations
def lengthofLongestSubstring_1(s):
	
	a =''.join(set(s))
	substring_index = s.find(a)
	if substring_index != -1:
		return len(a)

	else:

		allsubstrings_list = [''.join(l) for i in range(len(a),0,-1) for l in combinations(a, i)]	

		while substring_index == -1: 
			counter = 0
			a_new = allsubstrings_list[counter]
			counter += 1
			
		return len(a_new)

#Method 2 : passed
def lengthofLongestSubstring(s):

    str_list = []
    max_length = 0
    for x in s:
        if x in str_list:
            str_list = str_list[str_list.index(x)+1:]
        str_list.append(x)
        max_length = max(max_length, len(str_list))
    print(str_list)
    return max_length

#print(lengthofLongestSubstring('abcabcbb'))
#print(lengthofLongestSubstring('bbbbb'))
#print(lengthofLongestSubstring('pwwkew'))

'''
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

#Method 1 - using Merge sort
import random

def median(l):

	if len(l)%2 != 0:
		return l[len(l)//2]
	else:
		median_list = l[(len(l)//2)-1:(len(l)//2)+1]
		return sum(median_list)/2

def quick_sort(l1,l2):

	l3 = l1 + l2 
	if len(l3)<= 1:
		return l3
	smaller,equal,larger = [],[],[]
	pivot = l3[random.randint(0,len(l3)-1)]
	for i in l3:
		if i < pivot:
			smaller.append(i)
		elif i == pivot:
			equal.append(i)
		else:
			larger.append(i)

	l3_sorted = quick_sort(smaller[:len(smaller)//2],smaller[len(smaller)//2:])+equal+quick_sort(larger[:len(larger)//2],larger[len(larger)//2:])
	return l3_sorted

	



sample_list=quick_sort([1,9,8,5,6,7,2],[1,3,4,6,11,14,9])
print(sample_list)
print(median(sample_list))

