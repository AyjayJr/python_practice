import random
    
play = True
user_score = 0
computer_score = 0
rps = ("rock", "paper", "scissors")

while play == True:
    user_choice = input("Type Rock, Paper, Scissors to start playing or Q to quit: ").lower()
    
    # quit functionality
    if user_choice == "q":
        play = False
        continue

    # if they don't make a valid choice ask again
    if user_choice not in rps:
        continue

    # assign user_choice
    if user_choice in rps:
        user_choice = rps.index(user_choice)
        user_choice = rps[user_choice]

    # generate random choice
    rand_num = random.randrange(0, 3)
    computer_choice = rps[rand_num] 
    
    # evaluate who won the round and assign points
    if user_choice == computer_choice:
        print(f"Draw!\nComputer picked {computer_choice}")
        print(f"You: {user_score} vs. Computer: {computer_score}")
    elif (user_choice == "rock" and computer_choice == "scissors" or
          user_choice == "paper" and computer_choice == "rock" or
          user_choice == "scissors" and computer_choice == "paper"):
        print(f"You Win!\nComputer picked {computer_choice}")
        user_score += 1
        print(f"You: {user_score} vs. Computer: {computer_score}")
    else:
        print(f"You Lose!\nComputer picked {computer_choice}")
        computer_score += 1
        print(f"You: {user_score} vs. Computer: {computer_score}")

    # game over screen
    if user_score == 5 or computer_score == 5:
        if user_score > computer_score:
            print("YOU WIN :)")
        else:
            print("YOU LOST :(")
        while True:
            user_choice = input("Would you like to play again? (y/n): ")
            if user_choice == "y":
                user_score = 0
                computer_score = 0
                break
            elif user_choice == "n":
                print("See you next time!")
                play = False
                break
            else:
                continue
