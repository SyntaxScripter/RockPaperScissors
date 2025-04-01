import random
import os

score_win = 0
score_lose = 0
score_tie = 0
os.system('cls')


def rock_paper_scissors():
    global score_win, score_lose, score_tie
    os.system("color 4F")
    options = ["rock", "paper", "scissors"]
    print("Welcome to rock, paper, scissors!\n")
    print("-------------------------------")
    print("|Rules:                        |")
    print("|•rock beats scissors          |")
    print("|•paper beats rock             |")
    print("|•scissors beats paper         |")
    print("-------------------------------\n")
    user_input = input("Which one do you choose?: ")
    while user_input not in ["rock", "paper", "scissors"]:
        user_input = input("Invalid input. Which one do you choose?: ")
    computer_choice = random.choice(options)

    if user_input == computer_choice:
        print(user_input+"!"+" Tie!")
        score_tie = score_tie + 1
    elif user_input == "scissors":
        if computer_choice == "rock":
            print("Rock! Oh no, you lost.")
            score_lose = score_lose + 1
        else:
            print(computer_choice+"!"+" You won!")
            score_win = score_win + 1
    elif user_input == "rock":
        if computer_choice == "paper":
            print("Paper! Oh no, you lost.")
            score_lose = score_lose + 1
        else:
            print(computer_choice+"!"+" You won!")
            score_win = score_win + 1
    elif user_input == "paper":
        if computer_choice == "scissors":
            print("Scissors! Oh no, you lost.")
            score_lose = score_lose + 1
        else:
            print(computer_choice+"!"+"  You won!")
            score_win = score_win + 1

    play_again = input("Do you wanna play again? (yes/no): ")
    while play_again not in ["yes", "no"]:
        play_again = input("Invalid input. Do you wanna play again? (yes/no): ")
    if play_again == "yes":
        os.system('cls')
        rock_paper_scissors()
    else:
        print("\n--------------------")
        print("Score:")
        print("Games won:", score_win)
        print("Games lost:", score_lose)
        print("Games tie:", score_tie)
        print("--------------------")


rock_paper_scissors()
