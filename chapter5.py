def chapter_five(player, confront):
    """
    Chapter 5: The Grand Finale
    The final confrontation or alliance that determines the player's fate.
    """
    if confront:
        print(f"\n{player.name}, you stand face-to-face with the league's leader.")
        print("This fight will determine the fate of the league and your legacy.")

        while True:
            action = input("Do you want to 'fight' or attempt to 'negotiate'? ").strip().lower()
            if action == "fight":
                print("\nYou engage in a brutal fight with the leader.")
                if player.skills["boxing"] >= 3 and player.stamina > 20:
                    print("Your skill and preparation pay off. You defeat the leader!")
                    print("The league collapses, and you secure your place as a champion of justice.")
                else:
                    print("You are overpowered and defeated. The league remains in control.")
                break
            elif action == "negotiate":
                if player.money > 1000:
                    print("\nUsing your resources, you negotiate a peaceful resolution.")
                    print("The league reforms under your guidance, becoming a force for good.")
                else:
                    print("Your negotiation fails. You must fight to determine the outcome.")
                break
            else:
                print("Invalid choice. Please choose 'fight' or 'negotiate'.")
    else:
        print(f"\n{player.name}, as a new leader of the league, you now control its vast resources.")
        print("However, the shadows of crime follow you, and your legacy is forever tainted.")
        print("Congratulations on your rise to power, but at what cost?")

    print("\nThank you for playing! The journey of Dmitry Bivol is complete.")

if __name__ == "__main__":
    from player import Player
    player = Player("Test Player")
    chapter_five(player, confront=True)


