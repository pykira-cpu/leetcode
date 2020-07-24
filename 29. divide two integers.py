'''
29. Divide Two Integers
Medium

1212

5294

Add to List

Share
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and
 truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
 For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

 '''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # if dividend<0 or divisor <0 :
        #     sign = -1
        # else:
        #     sign = 1
        
        # quotient = 0
        # while dividend > divisor:
        #     dividend -= divisor
        #     quotient += 1
        
        # quotient = sign * quotient
        
        # if -2**31 <= quotient <= 2**31 + 1:
        #     return quotient
        # elif quotient -2**31 > quotient:
        #     return -2**31
        # else:
        #     2**31 + 1
        
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2 ** 31, res), 2 ** 31 - 1)

sol = Solution()
print(sol.divide(10,3))