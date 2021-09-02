inUs = input("Are you in the us (y/n) ").lower()
localFloor = int(input("What's the floor number? "))

if inUs == 'y':
    # The convention in the us is to have the ground floor as 1
    floor = localFloor - 1
else:
    # in the rest of the world ground floor is 0
    floor = localFloor

if floor == 0:
    print('You are on the ground floor')
else:
    print('You are on the ' + str(floor) +' level')

