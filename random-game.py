import random

high_num = 50
low_num = 1

secret_num = random.randint(low_num, high_num)

print "I am thinking of a number between %d and %d" %(low_num, high_num)

num_ofguesses = 0
guess = ""

while guess != secret_num:
	guess = raw_input("Take a guess:")
	guess = int(guess)
	num_ofguesses = num_ofguesses + 1

	if guess < secret_num:
		print "Your guess is too low"
	if guess > secret_num:
		print "Your guess is too high"		

print "You guessed the number in %s guesses" %(num_ofguesses)