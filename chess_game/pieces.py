import pygame
import os
import chess

class PieceLoader:
    def __init__(self, settings):
        self.settings = settings
        self.pieces = {}
        # Create directory if it doesn't exist to prevent crash
        if not os.path.exists(self.settings.ASSETS_PATH):
            print(f"Warning: Folder {self.settings.ASSETS_PATH} not found!")
            os.makedirs(self.settings.ASSETS_PATH, exist_ok=True)
        self.load_assets()

    def load_assets(self):
        piece_map = {
            'white': {
                chess.KING: "white_king.png", chess.QUEEN: "white_queen.png",
                chess.ROOK: "white_rook.png", chess.BISHOP: "white_bishop.png",
                chess.KNIGHT: "white_knight.png", chess.PAWN: "white_pawn.png"
            },
            'black': {
                chess.KING: "black_king.png", chess.QUEEN: "black_queen.png",
                chess.ROOK: "black_rook.png", chess.BISHOP: "black_bishop.png",
                chess.KNIGHT: "black_knight.png", chess.PAWN: "black_pawn.png"
            }
        }

        for color_name, mapping in piece_map.items():
            color_bool = chess.WHITE if color_name == 'white' else chess.BLACK
            for piece_type, filename in mapping.items():
                path = os.path.join(self.settings.ASSETS_PATH, filename)
                if os.path.exists(path):
                    try:
                        img = pygame.image.load(path).convert_alpha()
                        img = pygame.transform.smoothscale(img, (70, 70))
                        self.pieces[(piece_type, color_bool)] = img
                    except:
                        self.pieces[(piece_type, color_bool)] = None
                else:
                    self.pieces[(piece_type, color_bool)] = None

    def draw_piece(self, screen, piece, rect):
        image = self.pieces.get((piece.piece_type, piece.color))
        if image:
            img_rect = image.get_rect(center=rect.center)
            screen.blit(image, img_rect)
        else:
            color = (240, 240, 240) if piece.color == chess.WHITE else (40, 40, 40)
            pygame.draw.circle(screen, color, rect.center, 30)
            pygame.draw.circle(screen, self.settings.ACCENT_COLOR, rect.center, 30, 2)