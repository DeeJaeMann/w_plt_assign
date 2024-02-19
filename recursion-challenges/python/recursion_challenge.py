#!/usr/bin/env python3.12
import re

def factorial(x):
	
	if x == 1 :
		return x
	
	return x * factorial(x - 1)

def palindrome(string):
	# A string that is the same forward as it is backward

	# Create a list from the characters matched, ignore spaces, punctuation and case
	regex_pattern = re.compile(r'[a-z]')
	lst = regex_pattern.findall(string.lower())

	# Exit case:
	# If we have no more elements in the array then we have found a palindrome
	if len(lst) == 0 :
		return True
	
	# Check if the first and last indexes are the same
	if lst[0] == lst[-1] :
		# Remove the first and last index and join the characters into a string
		string = "".join(lst[1:-1])
		return palindrome(string)
	else :
		return False

def bottles(num):
	pass

def roman_num(num):
	pass

# print(factorial(5))
print(palindrome("A man, a plan, a canal -- Panama"))
print(palindrome("Pizza"))