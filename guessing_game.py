import random

winning_number = random.randint(1,10)
attempts = 0
copy = ''

def start_game():
    print('''
***********************************
Welcome to the number guessing game
***********************************
    
    ''')

start_game()

while True:
    try:
        guess = int(input('Guess a number between 1-10: '))
    except ValueError:
        print('That doesnt look like a number, please try again.')
        continue
    if guess > 10 or guess < 1:
        print('Sorry, your guess is outside of the 1-10 range.')
        continue
    attempts += 1
    if guess == winning_number:
        if attempts > 1:
            copy = 's'
        print('Bingo, got it! The number was {}. It took you {} attempt{}.'.format(winning_number, attempts, copy))
        break
    elif guess < winning_number:
        print('The number is higher, guess again.')
        continue
    elif guess > winning_number:
        print('The number is lower, guess again.')

print('The game is over, thank you for playing!')