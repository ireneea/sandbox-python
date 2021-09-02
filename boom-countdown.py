import time

delay = 5
n = delay

while n > 0:
    print(n)
    time.sleep(0.5)
    n -= 1

print('BOOOOM')