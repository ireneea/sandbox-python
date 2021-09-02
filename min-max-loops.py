import math
numbers = [12, -243, 12 , 198, 8, 895, 42, 76, 9]

def get_min(nums):
    min = math.inf
    for i in numbers:
        if i < min:
            min = i
    return min 

def get_max(nums):
    max = - math.inf
    for i in numbers:
        if i > max:
            max = i
    return max

print(get_min(numbers))
print(get_max(numbers))
         