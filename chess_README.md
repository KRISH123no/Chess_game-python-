# ♟️ Chess - Dark Wood Tavern

A fully-featured desktop Chess game built with Python and pygame, powered by the Stockfish 18 engine. Features a rich wooden tavern aesthetic with custom piece artwork.

---

## 🎮 Features

- **AI vs Player** — Play against Stockfish at 4 difficulty levels
- **Local Multiplayer** — Challenge a friend on the same computer
- **4 Difficulty Levels** — Easy (1320 Elo) → Medium → Hard (2200 Elo) → Pro (Full Stockfish)
- **Full Chess Rules** — Castling, en passant, pawn promotion, check/checkmate/stalemate
- **Move History Panel** — Algebraic notation displayed in real time
- **Visual Highlights** — Selected piece, legal moves, last move, king in check
- **Pawn Promotion Popup** — Choose Queen, Rook, Bishop or Knight
- **Wooden Tavern UI** — Custom dark wood theme with amber gold accents
- **Smooth 60 FPS** — Non-blocking Stockfish AI using Python threading (Mac M1 optimized)

---

## 🛠️ Requirements

```
Python 3.9+
pygame
python-chess
Stockfish 18
```

Install dependencies:
```bash
pip3 install pygame python-chess
brew install stockfish  # Mac
```

---

## 🚀 How to Run

```bash
cd chess_game
python3 main.py
```

---

## 📁 Project Structure

```
chess_game/
├── main.py        # Entry point and main game loop
├── game.py        # Core gameplay controller
├── board_ui.py    # Chess board rendering
├── pieces.py      # Piece image loading and drawing
├── bot.py         # Stockfish AI integration
├── menu.py        # Main menu and difficulty selection
├── settings.py    # Global constants and configuration
├── ui.py          # UI elements and move history
└── assets/
    └── pieces/    # Chess piece PNG images
```

---

## 🎯 Controls

- **Click** a piece to select it
- **Click** a highlighted square to move
- **ESC** to go back to menu

---

Built with ❤️ using Python, pygame, python-chess and Stockfish 18
