import chapter5

def chapter_four(player):
    """
    Chapter 4: High-Stakes Decisions
    The player discovers the league's secrets and makes critical choices.
    """
    print(f"\n{player.name}, your investigation uncovers dark truths about the league.")
    print("You learn that the league is tied to organized crime, and its leader is a dangerous figure.")

    while True:
        action = input("Do you want to 'confront the leader' or 'align with the league'? ").strip().lower()
        if action == "confront the leader":
            print("\nYou decide to confront the league's leader, putting your life on the line.")
            print("This is a dangerous move, but it aligns with your moral compass.")
            chapter5.chapter_five(player, confront=True)
            break
        elif action == "align with the league":
            print("\nYou choose to align with the league, gaining wealth and power but compromising your integrity.")
            print("The league welcomes you, and you rise to a position of influence.")
            chapter5.chapter_five(player, confront=False)
            break
        else:
            print("Invalid choice. Please choose 'confront the leader' or 'align with the league'.")

if __name__ == "__main__":
    from player import Player
    player = Player("Test Player")
    chapter_four(player)



