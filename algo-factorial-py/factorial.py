#!/usr/bin/env python3.12
def factorial(num):
	# your code here
	int_result = 1

	# Iterate through each number backward to determine result

	while num > 0:
		int_result *= num
		num -= 1

	return(int_result)
    
# print(factorial(4))
# print(factorial(5))

def factorial2(num):
	if num == 0:
		return 1
	return num*factorial2(num-1)

print(factorial2(4))