import random

ans = input("Do you think you can guess my number? (y/n)")
accept = ("yea", "yes", "y")
decline = ("nah","no","n")

while ans not in accept and ans not in decline:
    ans = input("Please enter a valid response. (y/n)")

if ans in decline:
    print("Ok, maybe next time!")
    quit()

num = input("Enter the max number: ")

while not num.isdigit():
    num = input("Please enter a valid number.")

if num.isdigit():
    num = int(num)

rand = random.randint(0, num)
print(f"num = {num} and rand = {rand}")
