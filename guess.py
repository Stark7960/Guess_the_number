import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            diff=random_number -guess
            if diff<5:
                print('Sorry, guess again. You are close but low.')
            else:
                print('Sorry, guess again. Too low.')
        elif guess > random_number:
            diff= guess - random_number
            if diff<5:
                print('Sorry, guess again. You are close but high.')
            else:
                print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

def computer_guess(x):
    print("\nNow think of a number from 1 to 100 and the computer will guess it.\n")
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


guess(100)
computer_guess(100)