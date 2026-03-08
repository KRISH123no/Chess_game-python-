import chess
import chess.engine
import threading
import os
import pygame

class ChessBot:
    def __init__(self, settings, difficulty):
        self.settings = settings
        self.difficulty = difficulty.capitalize()
        self.engine = None
        self.ready = False
        
        # Calculation state
        self.move_ready = False
        self.best_move = None
        
        # Start Engine Initialization in background thread
        self.init_thread = threading.Thread(target=self._init_engine, daemon=True)
        self.init_thread.start()

    def _init_engine(self):
        """Initializes and configures Stockfish in the background."""
        try:
            path = self.settings.STOCKFISH_PATH
            if not os.path.exists(path):
                path = "stockfish" 
            
            self.engine = chess.engine.SimpleEngine.popen_uci(path)
            
            # Stockfish 18 Elo Configuration (Min Elo 1320)
            if self.difficulty == "Easy":
                self.engine.configure({"UCI_LimitStrength": True, "UCI_Elo": 1320})
            elif self.difficulty == "Medium":
                self.engine.configure({"UCI_LimitStrength": True, "UCI_Elo": 1600})
            elif self.difficulty == "Hard":
                self.engine.configure({"UCI_LimitStrength": True, "UCI_Elo": 2200})
            elif self.difficulty == "Pro":
                self.engine.configure({"UCI_LimitStrength": False})
            
            self.ready = True
            print(f"Stockfish 18 ready at {self.difficulty} difficulty.")
        except Exception as e:
            print(f"Engine Init Error: {e}")

    def start_calculating(self, board):
        """Triggers the calculation thread."""
        if not self.ready or self.engine is None:
            return
            
        self.move_ready = False
        self.best_move = None
        
        # Pass a copy of the board to avoid thread-safety issues
        calc_thread = threading.Thread(target=self._calculate_move_task, args=(board.copy(),), daemon=True)
        calc_thread.start()

    def _calculate_move_task(self, board_copy):
        """Calculates the best move within a 2-second limit."""
        try:
            # We set a 1.5s limit to ensure the overhead doesn't exceed 2s total
            result = self.engine.play(board_copy, chess.engine.Limit(time=1.5))
            self.best_move = result.move
            self.move_ready = True
        except Exception as e:
            print(f"Calculation Error: {e}")
            self.move_ready = True 

    def quit(self):
        if self.engine:
            self.engine.quit()