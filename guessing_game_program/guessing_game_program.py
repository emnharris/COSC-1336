import random

def main():
    intro()
    keep_going = 'y'
    while keep_going == 'y':
        attempts = 0
        roll = roll_number()
        guess = accept_guesses()
    
        while guess != roll:
            feedback(roll, guess)
            guess = accept_guesses()
            attempts += 1
    
        print('\nYOU WIN!!')
        print('Number of tries:',attempts)
        keep_going = input('\nDo you want to keep playing? y or n\n')

def intro():
    print('='*45)
    print(('='*15),'GUESSING GAME',('='*15))
    print('\n\n',(' '*4),'Guess a number between 1 and 1000!\n')

def accept_guesses():
    answer = int(input('\nYour guess: '))
    return answer

def roll_number():
    return random.randint(1, 1000)

def feedback(random, answer):
    difference = 10
    colder = random - difference
    hotter = random + difference
    if answer < colder:
        print('Too low. Try again.\n')
    elif (answer >= colder and answer < random):
        print('Getting warm but too low. Try again.\n')
    elif (answer > hotter):
        print('Too high. Try again.\n')
    elif (answer <= hotter and answer > random):
        print('Getting warm but too high. Try again.\n')

main()
