# Author: Alikhan Zulumbekov
# Date: 12/2/2024
#
# Game Description:
#This is a text-based adventure game where the player assumes the role of Dmitry Bivol,
# an undefeated boxing champion. The game is set in an underground boxing league filled with dark secrets and tough decisions.
# The player navigates through different chapters, each offering important choices that shape the outcome of the story.
#Chapter 1: The Champion's Call
# Dmitry Bivol, an undefeated boxing champion, receives a mysterious invitation to an underground boxing league.
# The player decides whether to negotiate sponsorship deals or accept the invitation to explore the dangerous league.
# 
# Chapter 2: The Underground League
# Dmitry enters the underground league. The player chooses to train, explore the league’s secrets, or fight.
# Winning fights earns respect, but losing may result in injury or worse.
#
# Chapter 3: Decisions and Alliances
# Dmitry’s involvement in the league becomes public.
# The player must decide whether to continue fighting in the underground world or step back to preserve his career and reputation.
#
# Chapter 4: The League’s Secrets
# The truth behind the league is revealed: it’s tied to crime.
# Dmitry must choose to confront the leader or align with the league to gain power and wealth.
#
# Chapter 5: The Final Showdown
# Dmitry faces the ultimate challenge: fight the leader, negotiate a resolution, or rise to power in the league.
# The player’s choices determine Dmitry’s legacy and the game’s outcome.

import chapter1

def game_intro():
    print("Welcome to the Advanced Dmitry Bivol Adventure Game!")
    name = input("Enter your name: ")
    return name

def main():
    player_name = game_intro()
    chapter1.chapter_one(player_name)

if __name__ == "__main__":
    main()

