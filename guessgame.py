#Number guessing game
import random

guessesTaken = 0 #Stores the number of guesses a player makes

print("Hello, what is your name?")
YourName = input()

number = random.randint(1,10) #Function stores a return value
print('Well, '+YourName+'I am thinking of a number between 1 and 10.')

while guessesTaken < 4:
    print('Take a guess:')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Your guess is too low")

    if guess > number:
        print("Your guess is too high")
    
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job '+YourName +' You guessed my number in ' + guessesTaken + ' guesses')

if guess != number:
    number = str(number)
    print('Sorry the number I was thinking of was ' + number)