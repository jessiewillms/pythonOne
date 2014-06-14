favourite_foods = []
ask = 3
message = "You like these foods: "

while ask != 0:
	food = raw_input("What do you like to eat?")
	favourite_foods.append(food)
	ask -= 1

for food in favourite_foods:
	message = message + food + " "

message+= "Sounds YUMMMYY!"
print message