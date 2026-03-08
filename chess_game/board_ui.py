import pygame
import chess

class BoardUI:
    def __init__(self, screen, settings, piece_loader):
        self.screen = screen
        self.settings = settings
        self.piece_loader = piece_loader
        self.font = settings.get_font(16, bold=False)

    def draw_board(self, board, selected_sq, legal_moves, off_x, off_y):
        sq_sz = self.settings.SQUARE_SIZE
        
        for r in range(8):
            for c in range(8):
                rect = pygame.Rect(off_x + c * sq_sz, off_y + (7 - r) * sq_sz, sq_sz, sq_sz)
                
                # Base Squares
                color = self.settings.LIGHT_SQUARE if (r + c) % 2 != 0 else self.settings.DARK_SQUARE
                pygame.draw.rect(self.screen, color, rect)
                
                # Last move highlight
                if board.move_stack:
                    last_move = board.move_stack[-1]
                    if rect.collidepoint(self._sq_to_pos(last_move.from_square, off_x, off_y)) or \
                       rect.collidepoint(self._sq_to_pos(last_move.to_square, off_x, off_y)):
                        pygame.draw.rect(self.screen, (139, 69, 19, 100), rect)

                # Selected Square Glow
                curr_sq = chess.square(c, r)
                if selected_sq == curr_sq:
                    pygame.draw.rect(self.screen, self.settings.ACCENT_COLOR, rect, 3)

                # Legal Move Dots
                if curr_sq in legal_moves:
                    pygame.draw.circle(self.screen, self.settings.ACCENT_COLOR, rect.center, 8)

                # Pieces
                piece = board.piece_at(curr_sq)
                if piece:
                    self.piece_loader.draw_piece(self.screen, piece, rect)

    def _sq_to_pos(self, sq, off_x, off_y):
        c, r = chess.square_file(sq), chess.square_rank(sq)
        return (off_x + c * 80 + 40, off_y + (7 - r) * 80 + 40)