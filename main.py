import random
R = "rock"
P = "paper"
S = "scissors"
computer_list = ["R", "P", "S"]
proceed = True

while proceed:
    your_choice = input("Pick between rock, paper, scissors ").upper()
    computer_choice = random.choice(computer_list)
    if your_choice == "R" and computer_choice == "R":
        print(f"Player({R}) : CPU({R}) ")
        print("it is a tie")
    elif your_choice == "S" and computer_choice == "S":
        print(f"Player({S}) : CPU({S}) ")
        print("it is a tie")
    elif your_choice == "P" and computer_choice == "P":
        print(f"Player({P}) : CPU({P}) ")
        print("it is a tie")
    elif your_choice == "R" and computer_choice == "P":
        print(f"Player(Rock) : CPU({P}) ")
        print("the computer is the winner.")
        proceed = False
    elif your_choice == "S" and computer_choice == "P":
        print(f"Player(Scissors) : CPU({P})")
        print("You are the winner.")
        proceed = False
    elif your_choice == "S" and computer_choice == "R":
        print(f"Player(Scissors) : CPU({R}) ")
        print("the computer is the winner.")
        proceed = False
    elif your_choice == "P" and computer_choice == "R":
        print(f"Player(Paper) : CPU({R}) ")
        print("You are the winner.")
        proceed = False
    elif your_choice == "P" and computer_choice == "S":
        print(f"Player(Paper) : CPU({S}) ")
        print("the computer is the winner.")
        proceed = False
    elif your_choice == "R" and computer_choice == "S":
        print(f"Player(Rock) : CPU({S}) ")
        print("You are the winner.")
        proceed = False
    elif your_choice not in computer_list:
        print("error, your input is invalid.")