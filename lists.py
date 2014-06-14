# for num in range(10):
# 	print "num is", num

# nums = range(10)
# nums

# for nums in nums:
# 	print "num:", num	

secret = "fakePassword"
print "What's your password?"
for i in range(3):
	pass = raw_input("Please provide password")
	if pass == secret:
		print "Success"
		break 
	if pass != secret:
		print "Whoops, you will need to reset your password."