import random

ans = input("Do you think you can guess my number? (y/n)\n")
accept = ("yea", "yes", "y")
decline = ("nah","no","n")

while ans not in accept and ans not in decline:
    ans = input("Please enter a valid response. (y/n)\n")

if ans in decline:
    print("Ok, maybe next time!")
    quit()

top_of_range = input("Enter a positve number: ")

while not top_of_range.isdigit():
    top_of_range = input("Please enter a valid number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

ans = random.randint(0, top_of_range)

print(f"Ok, my number will be between 0 and {top_of_range}")

guess = input("Enter what you think my number is: ")
while not guess.isdigit():
    guess = input("Please enter a valid number: ")

attempts = 1
while int(guess) != ans:
    while not 0 <= int(guess) <= top_of_range:
        guess = input(f"Please enter a number between 0 and {top_of_range}: ")
        attempts += 1
    if int(guess) > ans:
        guess = input("You were above the number! Try again: ")
    else:
        guess = input("You were below the number! Try again: ")
    attempts += 1

if (int(guess) == ans):
    if (attempts == 1):
        print(f"Correct! It only took {attempts} try")
    else:
        print(f"Correct! It only took {attempts} tries")
