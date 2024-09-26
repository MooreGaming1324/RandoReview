import lib
import os

title = r"""
$$$$$$$\                            $$\           $$$$$$$\                      $$\                         
$$  __$$\                           $$ |          $$  __$$\                     \__|                        
$$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$$ | $$$$$$\  $$ |  $$ | $$$$$$\ $$\    $$\ $$\  $$$$$$\  $$\  $$\  $$\ 
$$$$$$$  | \____$$\ $$  __$$\ $$  __$$ |$$  __$$\ $$$$$$$  |$$  __$$\\$$\  $$  |$$ |$$  __$$\ $$ | $$ | $$ |
$$  __$$<  $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$  __$$< $$$$$$$$ |\$$\$$  / $$ |$$$$$$$$ |$$ | $$ | $$ |
$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____| \$$$  /  $$ |$$   ____|$$ | $$ | $$ |
$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$  |$$ |  $$ |\$$$$$$$\   \$  /   $$ |\$$$$$$$\ \$$$$$\$$$$  |
\__|  \__| \_______|\__|  \__| \_______| \______/ \__|  \__| \_______|   \_/    \__| \_______| \_____\____/
"""

while True:
    #Main Menu Loop
    os.system("cls")
    print(title)
    print("Guess the Steam game based on the user reviews! You have 3 guesses!\n")
    print("1. Start the game")
    print("2. Exit\n")
    choice = input(">>> ")
    match choice:
        case "1":
            while True:
                os.system("cls")
                print(title)
                print("(Game randomly selected from top games played in the past 2 weeks)")
                print("Generating game...")
                game = lib.get_game()
                reviews = lib.get_reviews(game["appid"], game["name"])
                trynum = 0
                print("Game found.\n")
                while trynum < 3:
                    user = lib.get_user(reviews[trynum]["author"]["steamid"])
                    print(f"Review #{trynum+1}:")
                    print(f"\tUser: {user}")
                    print(f"\tPlaytime: {(reviews[trynum]["author"]["playtime_at_review"] / 60):,.2f}hrs ({(reviews[trynum]["author"]["playtime_forever"] / 60):,.2f}hrs Total)\n")
                    print(reviews[trynum]["review"])
                    
                    while True:
                        guess = input("\nGuess: ")
                        closest = lib.get_closest(guess)
                        if closest == False:
                            print("Incorrect!")
                            trynum += 1
                            break
                        confirm_closest = input(f"Did you mean {closest}? (Y/n): ")
                        if confirm_closest.lower() == "y":
                            if closest.lower() == game["name"].lower():
                                print(f"\n\nCongradulations!! You guessed correctly! {game["name"]}")
                                trynum = 4
                                break
                            else:
                                print("Incorrect!")
                                trynum += 1
                                break
                    if trynum < 3: 
                        print(f"1 attempt remaining...\n") if trynum == 2 else print(f"2 attempts remaining...\n")
                    if trynum == 3:
                        print(f"\n\nYou loose! The answer is {game["name"]}")
                retry = input("Would you like to play again? (Y/n): ")
                if retry.lower() == "y":
                    continue
                else:
                    exit()
        case "2":
            exit()
        case _:
            continue

