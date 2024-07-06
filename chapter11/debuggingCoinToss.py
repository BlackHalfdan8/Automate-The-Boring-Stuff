import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()

toss = random.randint(0, 1)  # 0 is tails, 1 is heads

# Convert the toss result to 'heads' or 'tails'
toss_result = 'heads' if toss == 1 else 'tails'

if toss_result == guess:
    print('You got it!')
else:
    print('Nope! Guess again! Enter heads or tails:')
    guess = input().lower()
    if toss_result == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
