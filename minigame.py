from random import randrange
a = randrange(1000)
while True:
    b = int(input())
    if a == b:
        print(" you're a winner!")
        break
    print('Smaller' if (a < b) else 'Bigger')
