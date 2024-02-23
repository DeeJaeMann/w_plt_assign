#!/usr/bin/env python3.12
import re

def factorial(x):
	
	if x == 1 :
		return x
	
	return x * factorial(x - 1)

def palindrome(string):
	# A string that is the same forward as it is backward

	# Create a list from the characters matched, ignore spaces, punctuation and case
	# This is our search pattern:  any letter from a to z
	# We compile this into a RegEx object to process the findall method 
	regex_pattern = re.compile(r'[a-z]')
	# Findall locates every match and returns a list of all matches found.  This will 
	# both split the string into a list and omit any spaces and punctuation
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
	# Our elements do not match, there is no need to process any more letters
	else :
		return False

def bottles(num):
	
	if num == 0 :
		return (f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
	elif num == 1 :
		print(f"{num} bottle of beer on the wall, {num} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.")
		return bottles(num-1)
	elif num == 2 :
		print(f"{num} bottles of beer on the wall, {num} bottles of beer.\nTake one down and pass it around, {num-1} bottle of beer on the wall.")
		return bottles(num-1)
	else :
		print(f"{num} bottles of beer on the wall, {num} bottles of beer.\nTake one down and pass it around, {num-1} bottles of beer on the wall.")
		return bottles(num-1)


def roman_num(num):
	pass

# print(factorial(5))
# print(palindrome("A man, a plan, a canal -- Panama"))
# print(palindrome("Pizza"))
print(bottles(5))