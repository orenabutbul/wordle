# 🟩 Wordle Clone

A web-based Wordle game built with Python and Streamlit.

![Wordle Screenshot](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)

## Features

- 🎮 Classic Wordle gameplay - guess the 5-letter word in 6 tries
- 🟩🟨⬛ Color-coded feedback (green, yellow, gray)
- ⌨️ On-screen keyboard showing letter states
- 🔄 New game button to play again
- 📱 Responsive design

## Setup Instructions

### Option 1: Using UV (Recommended)

[UV](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

```bash
# Install UV (if not already installed)
pip install uv

# Create virtual environment and install dependencies
uv venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On macOS/Linux

uv pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Option 2: Using pip

```bash
# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## How to Play

1. **Start the app** - Run `streamlit run app.py`
2. **Make a guess** - Type a 5-letter word and press Enter or click Submit
3. **Read the feedback**:
   - 🟩 **Green** = Correct letter in the correct position
   - 🟨 **Yellow** = Correct letter in the wrong position
   - ⬛ **Gray** = Letter not in the word
4. **Keep guessing** - You have 6 attempts to find the word
5. **Play again** - Click "New Game" after winning or losing

## Project Structure

```
wordle/
├── app.py              # Main Streamlit application
├── game_logic.py       # Core game logic (check guesses, keyboard states)
├── words.py            # Word lists (answers and valid guesses)
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .gitignore          # Git ignore patterns
```

## Tips for Playing

- Start with words containing common letters: **E, A, R, I, O, T, N, S, L**
- Good starting words: **CRANE**, **SLATE**, **AUDIO**, **RAISE**
- Use different letters in early guesses to eliminate possibilities
- Pay attention to yellow letters - they're in the word but wrong position

## License

MIT License - feel free to use and modify!