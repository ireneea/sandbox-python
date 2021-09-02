def get_user_input():
    inUs = input("Are you in the us (y/n) ").lower()
    localFloor = int(input("What's the floor number? "))
    isUs = inUs == 'y'
    return (isUs, localFloor)

def to_eu_floor(isUs, floor):
    if isUs:
        # The convention in the us is to have the ground floor as 1
        floor = floor - 1
    else:
        # in the rest of the world ground floor is 0
        floor = floor
    return floor

def print_floor_level(floorNumber):
    if floorNumber == 0:
        print('You are on the ground floor')
    else:
        print('You are on the ' + str(floorNumber) +' level')


user_input = get_user_input()
floorNumber = to_eu_floor(user_input[0], user_input[1])
print_floor_level(floorNumber)



