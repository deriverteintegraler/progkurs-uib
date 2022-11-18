import random

choices = ["rock", "paper", "scissors"]

def rock_paper_scissors():
    game_round = 1
    player_score = 0
    ai_score = 0

    while True:
        print(f"Let's play round {game_round}")

        while True:
            player_choice = input("Your choice (Rock/Paper/Scissors)? ").lower()
            try:
                if player_choice not in choices:
                    raise Exception
                else:
                    break
            except Exception:
                print(f"I don't understand {player_choice}. Try again")

        ai_choice = choices[random.randint(0, 2)]

        if player_choice == ai_choice:
            print(f"My choice was {ai_choice}. Tie!")
        elif player_choice == "rock":
            if ai_choice == "paper":
                print("My choice was paper. I win.")
                ai_score += 1
            else:
                print("My choice was scissors. You win.")
                player_score += 1
        elif player_choice == "paper":
            if ai_choice == "scissors":
                print("My choice was scissors. I win.")
                ai_score += 1
            else:
                print("My choice was rock. You win.")
                player_score += 1
        elif player_choice == "scissors":
            if ai_choice == "rock":
                print("My choice was rock. I win.")
                ai_score += 1
            else:
                print("My choice was paper. You win.")
                player_score += 1

        print(f"Score: me: {ai_score}, you: {player_score}")
        cont = input("Continue (y/n)? ")
        if cont != 'y': break
        game_round += 1

rock_paper_scissors()