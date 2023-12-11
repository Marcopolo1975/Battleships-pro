# import Function
import random


# Function for welcome message
    
def start():
   
    print('''
          
                             __/___\_
              _____/______\_____
       ______/_____   _____\______\_____
   __/_____/______\_/_______\_______\____\__
  /_______________________________________\_
  \_______________________________________/
BBBBB      A    TTTTTT  TTTTTT  L       EEEEE   SSSSS  HH   HH  III  PPPP
B    B    A A     TT      TT    L       E      S       HH   HH   I   P   P
BBBBB    AAAAA    TT      TT    L       EEEE    SSSS   HHHHHHH   I   PPPP
B    B  A     A   TT      TT    L       E          S   HH   HH   I   P
BBBBB   A     A   TT      TT    LLLLLL  EEEEE  SSSSS   HH   HH  III  P


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

#Function to validate user inputs 
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

        print("Computer Grid:")
        print_grid(computer_grid)           