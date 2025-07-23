# Tic Tac Toe game in Python

b = [' '] * 9  # Initialize the game board

def print_b():
    """Print the game board"""
    print(f"\n| {b[0]} | {b[1]} | {b[2]} |\n| {b[3]} | {b[4]} | {b[5]} |\n| {b[6]} | {b[7]} | {b[8]} |\n")

def check_win():
    """Check if there is a winner"""
    for i in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if b[i[0]] == b[i[1]] == b[i[2]] != ' ':
            return b[i[0]]
    return 'Tie' if ' ' not in b else False

def game():
    """Main game loop"""
    p = 'X'
    while True:
        print_b()
        m = int(input(f"Player {p}, enter your move (1-9): ")) - 1
        if b[m] == ' ':
            b[m] = p
            w = check_win()
            if w:
                print_b()
                print(f"Player {w} wins!" if w != 'Tie' else "It's a tie!")
                break
            p = 'O' if p == 'X' else 'X'
        else:
            print("Invalid move, try again.")

if __name__ == '__main__':
    game()
  