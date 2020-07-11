import time
import os
import random


def is_big_small(number, guessed):
    if number > guessed:
        return '\nYour entered number is greater than the guessed number'
    else:
        return '\nYour entered number is smaller than the guessed number'


def is_multiple(number, guessed):
    if number > guessed:
        if number % guessed == 0:
            return '\n' + str(number) + ' is a multiple of the original number'
    else:
        if guessed % number == 0:
            return '\n' + str(number) + " comes in multiplication table of the computer's number"


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def hello():
    print('\t\t\t              ______                           ______ ')
    time.sleep(0.25)
    print('\t\t\t|       |    |          |          |          |      |')
    time.sleep(0.25)
    print('\t\t\t|       |    |          |          |          |      |')
    time.sleep(0.25)
    print('\t\t\t|-------|    |---       |          |          |      |')
    time.sleep(0.25)
    print('\t\t\t|       |    |          |          |          |      |')
    time.sleep(0.25)
    print('\t\t\t|       |    |______    |______    |______    |______|')
    time.sleep(0.25)
    print('\t\t   _________________________________________________________')
    time.sleep(0.5)


def welcome_screen():
    print('\n\nWelcome to our number guessing game')
    print('\nA dynamic game to check b/w you and our program (a.k.a your computer) ;~)')
    print('\nExcited to play the game...')
    print("\nLet's begin")
    time.sleep(0.5)
    print('\nOhh wait! wanna take a look at the instructions ?')
    choice = input('Enter your choice y/n --> ')
    if choice.startswith(('y', 'Y')):
        clear()
        instructions()
    elif choice.startswith(('n', 'N')):
        print('\nYou already seem a pro at the game...')
        print("Let's go")
        time.sleep(2.0)
    else:
        print('You seem a noob, have a look at the instructions:')
        time.sleep(1.0)
        clear()
        instructions()
    clear()


def instructions():
    print('\n')
    print('\t\t\t\t\t\tINSTRUCTIONS')
    print('\t\t\t\t\t   --------------')
    print('\n\n1 --> Computer will guess a random number between 1 to 1000 (both inclusive), you have to guess '
          'that number')
    print('\n2 --> You will be given some hints based on the number you entered, for your score to become more ;)')
    print('\n3 --> Your score will start from 100, and will decrease as more chances you will take to find my '
          'number ;|')
    print("\n\nThat's it ... ")
    print("As soon as you are ready just press any key and hit enter, to start your experience (F.Y.I - game)")
    input()


def game():
    guessed = random.randint(1, 1000)
    mess = 0
    score = 100
    while score:
        try:
            number = int(input('Enter your number --> '))
            if number == guessed:
                print('Congratulations!!! you won the game with a score of %d ;} ;) ;]' % (score))
                exit(0)
            else:
                if number < 1 or number > 1000:
                    print(
                        "Ohfo! didn't you read the instructions carefully, the number will only be in inclusive range "
                        "of 1 to 1000")
                    score -= 10
                    print('Now you have a remaining score of %d' % score)
                    continue
                print('Wrong answer :(')
                print(is_big_small(number, guessed))
                if is_multiple(number, guessed) != None:
                    print(is_multiple(number, guessed))
            score -= 10
            if score < 0:
                break
            print('\nNow you have a remaining score of %d' % score)
        except:
            print("\n\nYou really don't wanna mess with me, I can make your score reduced")
            if mess == 0:
                print('\nThis time I forgive you')
            else:
                score -= 5
            print('\nNow you have a remaining score of %d' % score)
            mess = 1
    print('\n\nNo worry champ! you can do better than this.')
    print('The original number which I guessed is --> %d ' % guessed)
    print('\nHope to see you again ;~)')
    print('Bye Bye')


if __name__ == '__main__':
    hello()
    welcome_screen()
    game()
