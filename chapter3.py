import chapter4


def chapter_three(player):
    """
    Chapter 3: Decisions with Consequences
    Player must choose between diving deeper or stepping back.
    """
    print(f"\nRumors spread about {player.name}'s involvement in the underground league.")

    while True:
        action = input("Do you want to 'dive deeper' into the league or 'step back'? ").strip().lower()
        if action == "dive deeper":
            print("\nYou choose to stay and uncover the league's secrets.")
            chapter4.chapter_four(player)
            break
        elif action == "step back":
            print("\nYou decide to leave the underground league, preserving your professional career.")
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please choose 'dive deeper' or 'step back'.")


if __name__ == "__main__":
    from player import Player

    player = Player("Test Player")
    chapter_three(player)




