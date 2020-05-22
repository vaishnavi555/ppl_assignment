import random
print("welcome to dice game!")
dice = input("press 0 to roll the dice or enter any number to exit: ")
while dice == 0:
	print(random.randrange(1,7))
	dice = input("enter Y to roll the dice or enter Y to exit: ")		

	

