# Minimum requirements for riding the roller coaster
min_age = 12
min_height = 48

# Ask the user for their age and height
age = int(input("Enter your age: "))
height = int(input("Enter your height in inches: "))

old_enough = age >= min_age
tall_enough = height >= min_height

# Determine whether or not the user can ride the
# roller coaster
cannot_ride_roller_coaster = not (old_enough and tall_enough)
if cannot_ride_roller_coaster:
    print "You can't ride the roller coaster."
else:
    print "You can ride the roller coaster!"

# Ask the user if they fulfill either requirement
# for using the swimming pool
swim_response = input("Can you swim? ")
life_jacket_response = input("Do you have a life jacket? ")

can_swim = swim_response == "yes"
has_life_jacket = life_jacket_response == "yes"

# Determine whether or not they can use the swimming
# pool
cannot_use_swimming_pool = not can_swim and not has_life_jacket
if cannot_use_swimming_pool:
    print "You can't go in the swimming pool."
else:
    print "You can go in the swimming pool!"


