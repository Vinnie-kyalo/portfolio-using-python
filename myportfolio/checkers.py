import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
BOARD_SIZE = 8
SQUARE_SIZE = 60
WINDOW_SIZE = BOARD_SIZE * SQUARE_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load and scale images
try:
    black_piece = pygame.image.load('black.png')
    white_piece = pygame.image.load('white.png')
    black_piece = pygame.transform.scale(black_piece, (SQUARE_SIZE, SQUARE_SIZE))
    white_piece = pygame.transform.scale(white_piece, (SQUARE_SIZE, SQUARE_SIZE))
except pygame.error as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    sys.exit()

def initialize_board():
    board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for row in range(3):
        for col in range(row % 2, BOARD_SIZE, 2):
            board[row][col] = 'B'
    for row in range(5, BOARD_SIZE):
        for col in range(row % 2, BOARD_SIZE, 2):
            board[row][col] = 'W'
    return board

def draw_board(board):
    screen.fill(WHITE)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, WHITE if (row + col) % 2 == 0 else BLACK, rect)
            
            piece = board[row][col]
            if piece == 'B':
                screen.blit(black_piece, rect.topleft)
            elif piece == 'W':
                screen.blit(white_piece, rect.topleft)
    
    pygame.display.flip()

def move_piece(board, start_row, start_col, end_row, end_col):
    piece = board[start_row][start_col]
    board[start_row][start_col] = ' '
    board[end_row][end_col] = piece

def play_turn(board, player):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // SQUARE_SIZE
                row = pos[1] // SQUARE_SIZE
                return row, col

def main():
    global screen
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Checkers")

    board = initialize_board()
    player = 'W'

    while True:
        draw_board(board)
        print(f"Player {player}'s turn")
        start_row, start_col = play_turn(board, player)
        print(f"Selected position: ({start_row}, {start_col})")
        end_row, end_col = play_turn(board, player)
        print(f"Move to position: ({end_row}, {end_col})")
        move_piece(board, start_row, start_col, end_row, end_col)
        player = 'B' if player == 'W' else 'W'

if __name__ == "__main__":
    main()
