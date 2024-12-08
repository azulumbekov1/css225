import chapter3

def chapter_two(player):
    """
    Chapter 2: Exploration and Preparation
    Player explores the underground league and prepares for their first fight.
    """
    print(f"\n{player.name} enters the underground league. It's a dangerous place.")
    trained = False

    while True:
        action = input("Do you want to 'train', 'explore', or 'fight'? ").strip().lower()
        if action == "train":
            player.train()
            trained = True
        elif action == "explore":
            print("\nYou discover rumors about illegal betting rings and powerful criminal bosses.")
        elif action == "fight":
            if trained:
                print("\nYou step into the ring, prepared for the challenge...")
                print("You win the fight and earn respect in the league!")
                player.earn_money(500)
                chapter3.chapter_three(player)
                break
            else:
                print("You are unprepared and lose the fight.")
                player.take_damage(30)
                if not player.is_alive():
                    print("You have been defeated. Game over.")
                    break
        else:
            print("Invalid choice. Please choose 'train', 'explore', or 'fight'.")

if __name__ == "__main__":
    from player import Player
    player = Player("Test Player")
    chapter_two(player)

