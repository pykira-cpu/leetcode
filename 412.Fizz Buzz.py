'''
Fizz Buzz

Solution
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples
of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
'''

def fizzBuzz(n):
	fb = []
	for i in range(1,n+1):
		
		if i%3 == 0 and i%5 == 0:
			fb.append("FizzBuzz")
		elif i%3 == 0:
			fb.append("Fizz")
		elif i%5 == 0:
			fb.append("Buzz")
	
		else:
			fb.append(str(i))

	return fb

print(fizzBuzz(15))
		

