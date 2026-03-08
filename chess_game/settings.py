import pygame
import os

class Settings:
    def __init__(self):
        # Initial Window Dimensions
        self.WINDOW_WIDTH = 1000
        self.WINDOW_HEIGHT = 800
        self.FPS = 60
        
        # Premium Wood Palette
        self.WOOD_BASE = (59, 31, 14)
        self.WOOD_GRAIN_MID = (74, 37, 18)
        self.WOOD_GRAIN_LIGHT = (107, 58, 42)
        
        self.ACCENT_COLOR = (200, 134, 10)
        self.TEXT_COLOR = (245, 222, 179)
        
        # Board Colors
        self.LIGHT_SQUARE = (212, 169, 106)
        self.DARK_SQUARE = (107, 58, 42)
        
        # Default M1/M2 Homebrew Path
        self.STOCKFISH_PATH = "/opt/homebrew/bin/stockfish"
        
        self.BOARD_SIZE = 640
        self.SQUARE_SIZE = 80
        
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ASSETS_PATH = os.path.join(self.BASE_DIR, "assets", "pieces")

    def get_offsets(self, current_w, current_h):
        """Dynamically calculate centering for the board and panels."""
        board_x = (current_w - self.BOARD_SIZE - 300) // 2 # Leave room for panel
        board_y = (current_h - self.BOARD_SIZE) // 2
        return board_x, board_y

    def get_font(self, size, bold=True):
        try:
            return pygame.font.SysFont("georgia", size, bold=bold)
        except:
            return pygame.font.SysFont("timesnewroman", size, bold=bold)