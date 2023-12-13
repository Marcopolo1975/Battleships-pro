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


# Function to create the game grid
def create_grid(size):
    grid = [['O' for _ in range(size)] for _ in range(size)]
    return grid


# function to add ships to the Grid
def place_ships(grid, num_ships):
    size = len(grid)
    ships_placed = 0
    while ships_placed < num_ships:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if grid[x][y] == 'O':
            grid[x][y] = 'S'
            ships_placed += 1


# function to display grid on Game Board
def print_grid(grid):
    size = len(grid)
    for row in grid:
        print(' '.join(row))


# Function to validate user inputs
def validate_input(guess, size):
    if len(guess) != 2:
        return False
    x = guess[0]
    y = guess[1]
    if not x.isdigit() or not y.isdigit():
        return False
    x = int(x)
    y = int(y)
    if x < 0 or x >= size or y < 0 or y >= size:
        return False
    return True


# Function for checking if a ship is hit or miss
def check_hit(grid, guess):
    x = int(guess[0])
    y = int(guess[1])
    if grid[x][y] == 'S':
        grid[x][y] = 'X'
        return True
    else:
        grid[x][y] = 'M'
        return False


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
