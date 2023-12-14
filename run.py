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


# function to check the Winner
def check_winner(grid):
    for row in grid:
        if 'S' in row:
            return False
    return True


# main Gameplay function
def play_battleship():
    size = int(input("Enter the grid size: "))
    num_ships = int(input("Enter the number of ships: "))

    player_grid = create_grid(size)
    computer_grid = create_grid(size)

    place_ships(player_grid, num_ships)
    place_ships(computer_grid, num_ships)

    while True:
        print("Player Grid:")
        print_grid(player_grid)

        # print("Computer Grid:")
        # print_grid(computer_grid)

# Guess function to determin hit or miss a shot
        guess = (input("Enter coordinates (row and column): ").split())
        if not validate_input(guess, size):
            print("Invalid input. Please enter valid coordinates.")
            continue

        if check_hit(computer_grid, guess):
            print("You hit a ship!")
            if check_winner(computer_grid):
                print("Great! You destroyed the computer's fleet. You win!")
                break
        else:
            print("You missed.")

        computer_guess = (random.randint(0, size - 1),
                          random.randint(0, size - 1))
        if check_hit(player_grid, computer_guess):
            print("The computer hit your ship!")
            if check_winner(player_grid):
                print("Oh no! The computer destroyed your fleet. You lose!")
                break
        else:
            print("The computer missed.")

# start a new game function
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_battleship()


# Start the game
play_battleship()
