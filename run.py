"""
Battleships Game
"""
# import Function
import random


# Function for Game Logo
def start():

    print('''
          
BBBBB      A     TTTTT   TTTTT  L       EEEE   SSSS    H   H  III  PPPP   SSSS
B    B    A A      T       T    L       E      S       H   H   I   P   P  S
BBBBB    AAAAA     T       T    L       EEE    SSSS    HHHHH   I   PPPP   SSSS
B    B  A     A    T       T    L       E         S    H   H   I   P         S
BBBBB   A     A    T       T    LLLL    EEEE   SSSS    H   H  III  P      SSSS

    ''')


start()


# function to creat grid on Game Board
def create_grid(size):
    grid = []
    for _ in range(size):
        grid.append(["O"] * size)
    return grid


def print_grid(grid):
    for row in grid:
        print(" ".join(row))


# Function to validate user inputs
def get_valid_input(message, max_value):
    while True:
        try:
            guess = int(input(message))
            if guess < 0 or guess >= max_value:
                print("Invalid input! Please enter a number within the grid range.")
            else:
                return guess
        except ValueError:
            print("Invalid input! Please enter a number.")


# Function for ability that the user can set the grid size and number of ships
def play_battleship():
    print("Let's play Battleship!")
    grid_size = get_valid_input("Enter the grid size (maximum 10): ", 11)
    num_ships = get_valid_input("Enter the number of ships (maximum 10): ", 11)
    player_grid = create_grid(grid_size)
    computer_grid = create_grid(grid_size)
    player_ships = set()
    computer_ships = set()

# Randomly place ships for the player and computer
    for _ in range(num_ships):
        while True:
            player_ship = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
            if player_ship not in player_ships:
                player_ships.add(player_ship)
                break
        while True:
            computer_ship = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
            if computer_ship not in computer_ships and computer_ship not in player_ships:
                computer_ships.add(computer_ship)
                break

 # Game main function
    while True:
        print("\nPlayer's grid and ships:")
        print("Player's ships: ", player_ships)
        
        print("\nPlayer's turn:")
        print_grid(player_grid)
        player_guess_row = get_valid_input("Enter your guess for the row: ", grid_size)
        player_guess_col = get_valid_input("Enter your guess for the column: ", grid_size)
        player_guess = (player_guess_row, player_guess_col)

        if player_guess in computer_ships:
            print("welldone! You hit the computer's ship!")
            computer_ships.remove(player_guess)
            computer_grid[player_guess_row][player_guess_col] = "X"
        else:
            print("Oops! You missed the computer's ship.")
            computer_grid[player_guess_row][player_guess_col] = "-"

        if not computer_ships:
            print("\nGreat! You destroyed the computers Fleet. You win!")
            break

        print("\nComputer's turn:")
        computer_guess = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))

        if computer_guess in player_ships:
            print("The computer hit your ship!")
            player_ships.remove(computer_guess)
            player_grid[computer_guess[0]][computer_guess[1]] = "X"
        else:
            print("The computer missed your ship.")
            player_grid[computer_guess[0]][computer_guess[1]] = "-"

        if not player_ships:
            print("\nOh no! The computer destroyed your Fleet. You lose!")
            break


# start a new game function
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_battleship()
    else:
        print("Thank you for playing Battleship!")


# Start the game
play_battleship()
