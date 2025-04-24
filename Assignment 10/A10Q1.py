import random
def is_valid(board):
    for i in range(len(board)):
        for j in range(i+1,len(board)):
            if abs(board[i]-board[j])==abs(i-j):
                return False
    return True
def generate_solution():
    board=list(range(8))
    while True:
        random.shuffle(board)
        if is_valid(board):
            return board
def print_board(board):
    for row in range(8):
        line=""
        for col in range(8):
            if board[row]==col:
                line+="Q    "
            else:
                line+=".    "
        print(line)
def main():
    solution=generate_solution()
    print("Random valid 8-queens solution:")
    print_board(solution)
if __name__=='__main__':
    main()
