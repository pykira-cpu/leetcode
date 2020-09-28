'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
def isValid(s):
	
	mapping = {"}": "{", "]":"[", ")":"("}
	stack =[]

	for char in s:
		# if it is a closing bracket
		if char in mapping:
			if stack:
				top_element = stack.pop()
			else:
				# assingning some dummy value if there's nothing in the stack
				top_element = "*"

			if top_element != mapping[char]:
				return False

		else:
			stack.append(char)

	return stack == []

'''
Time complexity:  O(n)
SPace complexity: O(n)
'''
#Driver's code

print(isValid("{{()}}"))
print(isValid("}"))

