'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of 
s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

def longestPalindrome(s):
	if s == "":
		return ""
	def check(l,r):
		while 0<= l<= r < len(s) and s[l] == s[r]:
			l -= 1
			r += 1
		return s[l+1:r]

	palindrome = [check(i, i) for i in range(len(s))] + [check(i, i+1) for i in range(len(s)-1) if s[i] == s[i+1]]
	if palindrome:
		return sorted(palindrome,key = len)[-1]
	else:
		""

'''
103 / 103 test cases passed.
Status: Accepted
Runtime: 888 ms
Memory Usage: 16.8 MB
'''


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome(""))
