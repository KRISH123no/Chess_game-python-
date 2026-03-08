import pygame
import chess
from board_ui import BoardUI
from pieces import PieceLoader

class GameController:
    def __init__(self, screen, settings, ui, mode='AI', difficulty='MEDIUM'):
        self.screen = screen
        self.settings = settings
        self.ui = ui
        self.mode = mode
        
        self.board = chess.Board()
        self.piece_loader = PieceLoader(settings)
        self.board_ui = BoardUI(screen, settings, self.piece_loader)
        
        self.selected_sq = None
        self.legal_moves = []
        self.game_over = False
        
        # AI Logic
        self.bot = None
        if mode == 'AI':
            from bot import ChessBot
            self.bot = ChessBot(settings, difficulty)
        
        self.ai_triggered = False

    def update(self, events):
        if self.game_over: return

        # AI Turn Logic
        if self.mode == 'AI' and self.board.turn == chess.BLACK:
            if not self.bot or not self.bot.ready:
                # Engine still loading in background...
                return 

            if not self.ai_triggered:
                self.bot.start_calculating(self.board)
                self.ai_triggered = True
            
            if self.bot.move_ready:
                if self.bot.best_move:
                    self.board.push(self.bot.best_move)
                self.ai_triggered = False
                self.bot.move_ready = False # Reset for next turn
                self._check_game_over()
        
        # Player Turn
        else:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._handle_click(event.pos)

    def _handle_click(self, pos):
        curr_w, curr_h = self.screen.get_size()
        off_x, off_y = self.settings.get_offsets(curr_w, curr_h)
        
        col = (pos[0] - off_x) // self.settings.SQUARE_SIZE
        row = 7 - ((pos[1] - off_y) // self.settings.SQUARE_SIZE)

        if 0 <= col <= 7 and 0 <= row <= 7:
            clicked_sq = chess.square(col, row)
            piece = self.board.piece_at(clicked_sq)
            
            if piece and piece.color == self.board.turn:
                self.selected_sq = clicked_sq
                self.legal_moves = [m.to_square for m in self.board.legal_moves if m.from_square == clicked_sq]
            elif self.selected_sq is not None:
                move = chess.Move(self.selected_sq, clicked_sq)
                # Auto-promotion logic
                promo = chess.Move(self.selected_sq, clicked_sq, promotion=chess.QUEEN)
                
                if move in self.board.legal_moves:
                    self.board.push(move)
                    self._after_player_move()
                elif promo in self.board.legal_moves:
                    self.board.push(promo)
                    self._after_player_move()
                else:
                    self.selected_sq = None
                    self.legal_moves = []

    def _after_player_move(self):
        self.selected_sq = None
        self.legal_moves = []
        self._check_game_over()

    def _check_game_over(self):
        if self.board.is_game_over():
            self.game_over = True

    def draw(self, w, h):
        off_x, off_y = self.settings.get_offsets(w, h)
        self.board_ui.draw_board(self.board, self.selected_sq, self.legal_moves, off_x, off_y)
        
        status = "AI Thinking..." if (self.mode == 'AI' and self.board.turn == chess.BLACK) else "Your Turn"
        if not self.bot.ready and self.mode == 'AI': status = "Loading Engine..."
        
        self.ui.draw_side_panel(self.board, status, w, h)
        if self.game_over:
            self.ui.draw_game_over(self.board.result())

    def cleanup(self):
        if self.bot: self.bot.quit()