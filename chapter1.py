import chapter2
from player import Player


def chapter_one(player_name):
    """
    Chapter 1: Introduction
    Introduces the main plot and decisions.
    """
    player = Player(player_name)
    print(f"\nWelcome, {player.name}! You are Dmitry Bivol, the undefeated boxing champion.")
    print("You’ve just won a title defense match, but things are about to get interesting.")

    while True:
        action = input(
            "Do you want to 'negotiate' sponsorship deals or 'accept' a mysterious invitation? ").strip().lower()
        if action == "negotiate":
            print("\nYou meet potential sponsors...")
            if player.skills["negotiation"] >= 2:
                player.earn_money(1000)
                print("Negotiations are successful!")
            else:
                print("Your negotiation skills aren't strong enough. You earn no money.")
        elif action == "accept":
            print("\nYou accept the mysterious invitation and head to the underground league.")
            chapter2.chapter_two(player)
            break
        else:
            print("Invalid choice. Please choose 'negotiate' or 'accept'.")


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    chapter_one(player_name)
