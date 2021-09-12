print("Welcome to my quiz!")
ans = input("Would you like to play? (y/n): ")
accept = ("yeah", "yes", "yea", "y")
decline = ("never", "nah", "no", "n")

while ans not in accept and ans not in decline:
    ans = input("Please make a valid selection. (y/n): ")
if ans in decline:
    print("bye!")
    quit()

print("Okay! Let's play.")
score = 0;

ans = input("What does CPU stand for? ")
if ans.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("What does GPU stand for? ")
if ans.lower() == "graphics processing unit": 
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("What does RAM stand for? ")
if ans.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("What does HDD stand for? ")
if ans.lower() == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("What does SSD stand for? ")
if ans.lower() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print(f"Your score is {score}/5")
print("See you next time")
