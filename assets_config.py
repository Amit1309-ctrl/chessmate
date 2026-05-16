import pygame
import os

ASSETS_PATH = os.path.join("assets", "images")

white_piece_images = {
    "pawn": pygame.image.load(os.path.join(ASSETS_PATH, "white_pawn.png")),
    "rook": pygame.image.load(os.path.join(ASSETS_PATH, "white_rook.png")),
    "knight": pygame.image.load(os.path.join(ASSETS_PATH, "white_knight.png")),
    "bishop": pygame.image.load(os.path.join(ASSETS_PATH, "white_bishop.png")),
    "queen": pygame.image.load(os.path.join(ASSETS_PATH, "white_queen.png")),
    "king": pygame.image.load(os.path.join(ASSETS_PATH, "white_king.png")),
}

black_piece_images = {
    "pawn": pygame.image.load(os.path.join(ASSETS_PATH, "black_pawn.png")),
    "rook": pygame.image.load(os.path.join(ASSETS_PATH, "black_rook.png")),
    "knight": pygame.image.load(os.path.join(ASSETS_PATH, "black_knight.png")),
    "bishop": pygame.image.load(os.path.join(ASSETS_PATH, "black_bishop.png")),
    "queen": pygame.image.load(os.path.join(ASSETS_PATH, "black_queen.png")),
    "king": pygame.image.load(os.path.join(ASSETS_PATH, "black_king.png")),
}