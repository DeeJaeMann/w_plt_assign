#def bottle_song():
	# write your code here!
#	pass

#bottle_song()

####kldjsfalkfdajalskdfjdfls

def bottle_song(num):
	 #= num
	print(num)
	while num >=3:
		main_string = f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num-1} bottles of beer on the wall."
		print(main_string)
		num = num-1
	if num == 2:
		print(f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num-1} bottle of beer on the wall.")
		num = num-1
	if num ==1:
		print(f"{num} bottle of beer on the wall, {num} bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")
# 1 bottle of beer on the wall, 1 bottle of beer. )

# write your code here!

#(bottle_song(99))

# Exit case
# if num == 0
#	exit


# if(num > 3) :
#	print normal message
# elif num == 2:
#	2 msg
# else:
#	last message

def bottle_song_two(num):


	if num >=3:
		main_string = f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num-1} bottles of beer on the wall."
		print(main_string)
		#num = num-1
		#call function again here
	elif num == 2:
		print(f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num-1} bottle of beer on the wall.")
		#num =  num-1
	elif num == 1:
		print(f"{num} bottle of beer on the wall, {num} bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")
		#num = num-1
	else:
		# num is 0
		# exit case
		return



	if num > 0:
		return bottle_song_two(num-1)

bottle_song_two(10)



