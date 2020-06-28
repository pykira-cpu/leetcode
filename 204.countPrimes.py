'''
  Count Primes

'''
'''
The Algorithm used for the 3rd function is Seive of Eratosthenes. It is an efficient one with
Time complexity of O(n*log(log(n)))
'''

class Solution(object):

	def countPrimes(self,n):
		cnt = 0

		for i in range(n):	
			if self.isprime(i) == True:
				cnt += 1
		return cnt

	def isprime(self,n):
		if n>1:
			for i in range(2,n):
				if n%i == 0:
					return False
			return True
		else:
			return False

	def SeiveofEratosthenes(self,n):

	    prime= [True for i in range(n)]
	    prime[0]=False
	    prime[1]=False

	    p = 2
	    while p*p <= n:
	        if prime[p]==True:
	            for i in range(p*p,n,p):
	                prime[i]= False
	        p += 1
	    
	    count = 0
	    for p in range(2,n):
	        if prime[p]:
        		count += 1

	    return count



sol1 = Solution()
print(sol1.countPrimes(10))
print(sol1.countPrimes(100))
print(sol1.countPrimes(12))
print(sol1.SeiveofEratosthenes(2))
print(sol1.SeiveofEratosthenes(1000000))
