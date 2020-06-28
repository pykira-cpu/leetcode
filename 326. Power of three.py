'''
Power Of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false

'''
def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n==0:
        return False
    if n==1:
        return True
    if n%3!=0:
        return False
    
    while n%3==0:
        n=n/3
    if n==1:
        return True

def isPowerOfThree_2(n):
	"""
    :type n: int
    :rtype: bool
    """
	while i<=19:
		if 3**i==n:
			return True 
			break
		i+=1
	return False
