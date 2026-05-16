import pygame
import os
from assets_config import *

# Initialize
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Mate!")

black_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

black_location = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                  (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

white_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

white_location = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                  (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]


ROWS, COLS = 8, 8
# SQUARE_SIZE = WIDTH // COLS

BORDER = 20
PADDING = 10
BOARD_SIZE = min(WIDTH, HEIGHT) - 2 * (BORDER + PADDING)
SQUARE_SIZE = BOARD_SIZE // COLS
OFFSET_X = (WIDTH - BOARD_SIZE) // 2
OFFSET_Y = (HEIGHT - BOARD_SIZE) // 2

HOZ_POS = ['A','B','C','D','E','F','G','H']

font = pygame.font.SysFont(None,24)
TEXT_COLOR = (0,0,0)

PINE_DARK = (155, 127, 91)
PINE_LIGHT = (230, 197, 130)
# 80, 15, 30

BORDER_COLOR = (180, 140, 121)
BORDER_WIDTH = 20

HIGHLIGHT_COLOR = (200, 200, 0)   # light yellow

# Track selection
selected_piece = None
selected_index = None

# draw main game board
def draw_board():
    # DRAW SQUARES
    for row in range(ROWS):
        for col in range(COLS):
            # Alternate colors
            if (row + col) % 2 == 0:
                color = PINE_LIGHT
            else:
                color = PINE_DARK
            pygame.draw.rect(
                screen,
                color,
                (col * SQUARE_SIZE + OFFSET_X, row * SQUARE_SIZE + OFFSET_Y, SQUARE_SIZE, SQUARE_SIZE)
            )
    # DRAW BORDER
    pygame.draw.rect(
        screen,
        BORDER_COLOR,
        (
            OFFSET_X - PADDING,
            OFFSET_Y - PADDING,
            BOARD_SIZE + 2 * PADDING,
            BOARD_SIZE + 2 * PADDING
        ),
        BORDER
    )
    # DRAW HIGHLIGHT
    if selected_piece is not None:
        x, y = white_location[selected_index]

        pygame.draw.rect(
            screen,
            HIGHLIGHT_COLOR,
            (
                x * SQUARE_SIZE + OFFSET_X,
                y * SQUARE_SIZE + OFFSET_Y,
                SQUARE_SIZE,
                SQUARE_SIZE
            )
        )
# Draw markings
for col in range(COLS):
    letter = HOZ_POS[col]
    text = font.render(letter, True, (255, 255, 255))
    screen.blit(text, (OFFSET_X + col * SQUARE_SIZE, OFFSET_Y - 20))

for row in range(ROWS):
    number = str(ROWS - row)
    text = font.render(number, True, (255, 255, 255))
    screen.blit(text, (OFFSET_X - 20, OFFSET_Y + row * SQUARE_SIZE))

ASSETS_PATH = os.path.join("assets", "images")

# Game moves validation
class Piece:
    def get_valid_moves(self, board):
        pass

class Pawn(Piece):
    def get_valid_moves(self, board):
        # pawn logic
        pass

class Rook(Piece):
    def get_valid_moves(self, board):
        # rook logic
        pass


for key in white_piece_images:
    if key == "pawn":
        size = int(SQUARE_SIZE * 0.80)
    else:
        size = SQUARE_SIZE
    white_piece_images[key] = pygame.transform.scale(white_piece_images[key], (size, size))
    black_piece_images[key] = pygame.transform.scale(black_piece_images[key], (size, size))

# # Draw pieces on the board
def draw_pieces():
    PAWN_SCALE = int(SQUARE_SIZE * 0.80)
    # white pieces
    for i in range(len(white_pieces)):
        piece = white_pieces[i]
        x, y = white_location[i]

        if piece == "pawn":
            offset = (SQUARE_SIZE - PAWN_SCALE) // 2
            screen.blit(
                white_piece_images[piece],
                (x * SQUARE_SIZE + OFFSET_X + offset,
                 y * SQUARE_SIZE + OFFSET_Y + offset)
            )
        else:
            screen.blit(
                white_piece_images[piece],
                (x * SQUARE_SIZE + OFFSET_X,
                 y * SQUARE_SIZE + OFFSET_Y)
            )

    # black pieces
    for i in range(len(black_pieces)):
        piece = black_pieces[i]
        x, y = black_location[i]

        if piece == "pawn":
            offset = (SQUARE_SIZE - PAWN_SCALE) // 2
            screen.blit(
                black_piece_images[piece],
                (x * SQUARE_SIZE + OFFSET_X + offset,
                 y * SQUARE_SIZE + OFFSET_Y + offset)
            )
        else:
            screen.blit(
                black_piece_images[piece],
                (x * SQUARE_SIZE + OFFSET_X,
                 y * SQUARE_SIZE + OFFSET_Y)
            )

# Game loop
running = True
while running:
    draw_board()
    draw_pieces()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            col = (mx - OFFSET_X) // SQUARE_SIZE
            row = (my - OFFSET_Y) // SQUARE_SIZE
            # 1️⃣ If nothing selected → try selecting a pawn
            if selected_piece is None:
                for i in range(len(white_pieces)):
                    if white_pieces[i] == "pawn" and white_location[i] == (col, row):
                        selected_piece = "pawn"
                        selected_index = i
                        break

            # 2️⃣ If already selected → try moving
            else:
                x, y = white_location[selected_index]

                # allow 1 step forward
                if (col, row) == (x, y - 1):
                    white_location[selected_index] = (col, row)

                # reset selection
                selected_piece = None
                selected_index = None
                    
pygame.quit()