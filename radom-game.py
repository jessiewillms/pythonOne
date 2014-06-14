import random

secret_num = random.randinit(1, 1005)

print "I am thinking of a number between 1 and 1005"

guess = 0 

while guess != secret_num:
	guess = raw_input("Take a guess:")
	guess = int(guess)

	if guess < secret_num:
		print "Your guess is too low"
	if guess > secret_num:
		print "Your guess is too high"		