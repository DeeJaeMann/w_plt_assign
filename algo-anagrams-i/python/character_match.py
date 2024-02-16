#!/usr/bin/env python3.12
# Don't forget to run the tests (and create some of your own)
import re

# Part 1
def is_character_match(string1, string2):
	# Construct the string to feed the RegEx pattern
	# Given the string1 as 'charm' this will create the RegEx
	# pattern r'[charm]{5}' with the case insenstivie flag applied
	# This will ensure we find exactly 5 matches of the characters listed in the
	# string
	str_pattern = f"[{string1}]" + "{" + f"{len(string1)}" + "}"

	regex_pattern = re.compile(str_pattern, re.I)

	if re.match(regex_pattern,string2) :
		return True
	return False


# Part 2
def anagrams_for(word, list_of_words):
	lst_result = []
	while list_of_words :
		# Use the match function we've already created
		if is_character_match(word, list_of_words[0]) :
			# if we have a match, add it to the results list
			lst_result.append(list_of_words[0])
		
		# remove the element from the original list
		del(list_of_words[0])
		
	return lst_result

# list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

# print(is_character_match('charm', 'march'))
# print(is_character_match('zach','attack'))

# print(anagrams_for("threads", list_of_words))
# print(anagrams_for("apple", list_of_words))