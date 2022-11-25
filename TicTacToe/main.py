from playground import PlayGame

# You can change the colors modifying the below constants. OR you can enhance the logic in order to ask the users
# which colors they prefer.
COLOR_O = '\033[94m'
COLOR_X = '\033[92m'
COLOR_DEFAULT = '\033[0m'

PLAYGROUND = " _________________\n|__1__|__2__|__3__|\n|__4__|__5__|__6__|\n|__7__|__8__|__9__|\n"

player1 = []
player2 = []

game = PlayGame(COLOR_O, COLOR_X, COLOR_DEFAULT, PLAYGROUND)

index = 0
game_over = False

# Introduction for game
print("Welcome to TicTacToe Game. Below you can see the playground for our game.\n")

print(PLAYGROUND)

while not game_over:
    index += 1

    if index % 2 == 0:
        player = "O"
        player_option = int(input(f"\nPlayer_{player}: Please choose the number, "
                                  f"so it will be your option where the {player} will appear: "))

        player2.append(player_option)

        # Change the number from playground with O char
        print(game.output_playground(player, player_option))

        # Check if the player2 has the winner combination
        if game.check_combination(player2):
            game_over = True
            print(COLOR_O + f"The Player_{player} won the Game!")
    else:
        player = "X"
        player_option = int(input(f"\nPlayer_{player}: Please choose the number, "
                                  f"so it will be your option where the {player} will appear: "))
        player1.append(player_option)

        # Change the number from playground with X
        print(game.output_playground(player, player_option))

        # Check if the player1 has the winner combination
        if game.check_combination(player1):
            game_over = True
            print(COLOR_X + f"The Player_{player} won the Game!")

    if index == 9 and not game_over:
        game_over = True
        print(f"It's DRAW!")



