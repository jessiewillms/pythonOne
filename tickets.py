num_tickets = 100
print "How many tickets would you like?"

# need a while loop for when user inputs something
# that is not a number; goes back to top

isNumber = False

while not isNumber:
	try:
		tickets = int(raw_input('Enter the number of tickets!'))
		isNumber = True
	except: 
		print "That's not a number!"

if tickets <= 0:
	print "Sorry, please input a postive number!"
else:	
	print "You wanted %d tickets" %(tickets)

	left_tickets = num_tickets - tickets

	if tickets > num_tickets:
		print "Sorry, we don't have that many tickets"
	else: 
		print "There are %d tickets remaining" %(left_tickets)