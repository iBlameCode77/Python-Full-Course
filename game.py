import random
import sys


def game():
    attempt = 1
    player_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
     
    while player_choice not in ["rock", "paper", "scissors"]:
        player_choice = input(
            "Invalid choice. Enter rock, paper, or scissors: "
        ).lower()
        attempt += 1

        if attempt == 3:
            print("Bruh, are you high?")
        if attempt == 5:
            print("Nigga you crazy?")
        if attempt == 6:
            print("Oh hell naah")
            sys.exit()    

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
        return "tie"

    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        print(f"You win! {player_choice} beats {computer_choice}.")
        return "player"

    else:
        print(f"You lose! {computer_choice} beats {player_choice}.")
        return "computer"


print("===== ROCK PAPER SCISSORS =====")
print("1. Single Game")
print("2. Best of 3")
print("3. Best of 5")
print("4. Free Play")

gender = input("\n Select your gender (M/F): ")
mode = input("\nChoose a game mode (1-4): ")

player_score = 0
computer_score = 0


# ---------------- SINGLE GAME ----------------
if mode == "1":

    result = game()

    if result == "player":
        player_score += 1
    elif result == "computer":
        computer_score += 1


# ---------------- BEST OF 3 ----------------
elif mode == "2":

    while player_score < 2 and computer_score < 2:

        result = game()

        if result == "player":
            player_score += 1

        elif result == "computer":
            computer_score += 1

        print(
            f"Score -> You: {player_score} | Computer: {computer_score}"
        )


# ---------------- BEST OF 5 ----------------
elif mode == "3":

    while player_score < 3 and computer_score < 3:

        result = game()

        if result == "player":
            player_score += 1

        elif result == "computer":
            computer_score += 1

        print(
            f"Score -> You: {player_score} | Computer: {computer_score}"
        )


# ---------------- FREE PLAY ----------------
elif mode == "4":

    while True:

        result = game()

        if result == "player":
            player_score += 1

        elif result == "computer":
            computer_score += 1

        print(
            f"Score -> You: {player_score} | Computer: {computer_score}"
        )

        play_again = input("\nPlay another round? (y/n): ").lower()

        attempts = 0

        while play_again not in ["y", "n"]:

            attempts += 1

            if attempts == 3:
                print("Are you high?")

            elif attempts == 5:

                if gender.upper() == "M":
                    print("Boy don't play with me")
                elif gender.upper() == "F":
                    print("Do dem dishes woman")
                else:
                    print("Game Over")

                sys.exit()

            play_again = input(
                "Please enter only y or n: "
            ).lower()

        if play_again == "n":
            break

print("\n===== FINAL SCORE =====")
print(f"You: {player_score}")
print(f"Computer: {computer_score}")

if player_score > computer_score:
    print("🏆 Congratulations! You won the match!")

elif computer_score > player_score:
    print("💻 Computer won the match!")

else:
    print("🤝 The match ended in a tie!")