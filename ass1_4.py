import random
print("welcome to guessing game!")
no = random.randrange(1,11)
for x in range(3):
	guess = input("guess the number from 1-10: ")
	if guess > no:
		print("guess is greater than no. !")
	elif guess < no:
		print("guess is smaller than no. !")
	else:
		print("correct guess!")
		break
print("{} was the number".format(no))
	
