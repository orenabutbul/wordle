"""
Wordle Clone - Streamlit App
A web-based word guessing game built with Streamlit.
"""

import random
import streamlit as st
from game_logic import check_guess, get_keyboard_states, is_valid_guess, LetterState
from words import ANSWER_WORDS, VALID_GUESSES


# Page configuration
st.set_page_config(
    page_title="Wordle",
    page_icon="🟩",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Main container */
    .main {
        max-width: 500px;
        margin: 0 auto;
    }
    
    /* Title styling */
    .title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        letter-spacing: 0.1em;
    }
    
    /* Game board grid */
    .game-board {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 5px;
        margin-bottom: 20px;
    }
    
    .guess-row {
        display: flex;
        gap: 5px;
    }
    
    /* Letter tiles */
    .tile {
        width: 58px;
        height: 58px;
        border: 2px solid #3a3a3c;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 2rem;
        font-weight: bold;
        text-transform: uppercase;
        color: white;
        box-sizing: border-box;
    }
    
    .tile-empty {
        background-color: #121213;
        border-color: #3a3a3c;
    }
    
    .tile-filled {
        background-color: #121213;
        border-color: #565758;
    }
    
    .tile-correct {
        background-color: #538d4e;
        border-color: #538d4e;
    }
    
    .tile-present {
        background-color: #b59f3b;
        border-color: #b59f3b;
    }
    
    .tile-absent {
        background-color: #3a3a3c;
        border-color: #3a3a3c;
    }
    
    /* Keyboard styling */
    .keyboard {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        margin-top: 20px;
    }
    
    .keyboard-row {
        display: flex;
        gap: 6px;
    }
    
    .key {
        min-width: 43px;
        height: 58px;
        border-radius: 4px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.85rem;
        font-weight: bold;
        text-transform: uppercase;
        color: white;
        background-color: #818384;
        cursor: default;
    }
    
    .key-correct {
        background-color: #538d4e;
    }
    
    .key-present {
        background-color: #b59f3b;
    }
    
    .key-absent {
        background-color: #3a3a3c;
    }
    
    /* Message styling */
    .message {
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .message-win {
        color: #538d4e;
    }
    
    .message-lose {
        color: #b59f3b;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Input styling */
    .stTextInput > div > div > input {
        text-transform: uppercase;
        font-size: 1.2rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


def initialize_game():
    """Initialize or reset the game state."""
    st.session_state.answer = random.choice(ANSWER_WORDS).lower()
    st.session_state.guesses = []
    st.session_state.results = []
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.message = ""


def render_tile(letter: str, state: str = "empty") -> str:
    """Render a single tile as HTML."""
    tile_class = f"tile tile-{state}"
    return f'<div class="{tile_class}">{letter}</div>'


def render_game_board():
    """Render the game board with all guesses."""
    html = '<div class="game-board">'
    
    # Render completed guesses
    for i, (guess, result) in enumerate(zip(st.session_state.guesses, st.session_state.results)):
        html += '<div class="guess-row">'
        for letter, state in zip(guess, result):
            state_class = state.value
            html += render_tile(letter.upper(), state_class)
        html += '</div>'
    
    # Render empty rows
    remaining_rows = 6 - len(st.session_state.guesses)
    for _ in range(remaining_rows):
        html += '<div class="guess-row">'
        for _ in range(5):
            html += render_tile("", "empty")
        html += '</div>'
    
    html += '</div>'
    return html


def render_keyboard():
    """Render the on-screen keyboard with letter states."""
    keyboard_rows = [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
    ]
    
    keyboard_states = get_keyboard_states(st.session_state.guesses, st.session_state.results)
    
    html = '<div class="keyboard">'
    for row in keyboard_rows:
        html += '<div class="keyboard-row">'
        for letter in row:
            state = keyboard_states.get(letter.lower())
            key_class = "key"
            if state:
                key_class += f" key-{state.value}"
            html += f'<div class="{key_class}">{letter}</div>'
        html += '</div>'
    html += '</div>'
    
    return html


def process_guess(guess: str):
    """Process a guess and update game state."""
    guess = guess.lower().strip()
    
    # Validate the guess
    is_valid, error = is_valid_guess(guess, VALID_GUESSES)
    if not is_valid:
        st.session_state.message = f"❌ {error}"
        return
    
    # Check the guess
    result = check_guess(guess, st.session_state.answer)
    st.session_state.guesses.append(guess)
    st.session_state.results.append(result)
    st.session_state.message = ""
    
    # Check win condition
    if all(state == LetterState.CORRECT for state in result):
        st.session_state.game_over = True
        st.session_state.won = True
        st.session_state.message = f"🎉 Congratulations! You won in {len(st.session_state.guesses)} guess{'es' if len(st.session_state.guesses) > 1 else ''}!"
    
    # Check lose condition
    elif len(st.session_state.guesses) >= 6:
        st.session_state.game_over = True
        st.session_state.won = False
        st.session_state.message = f"😔 Game over! The word was: {st.session_state.answer.upper()}"


# Initialize game state if needed
if 'answer' not in st.session_state:
    initialize_game()


# Main UI
st.markdown('<div class="title">WORDLE</div>', unsafe_allow_html=True)

# Game board
st.markdown(render_game_board(), unsafe_allow_html=True)

# Message display
if st.session_state.message:
    message_class = "message-win" if st.session_state.won else "message-lose" if st.session_state.game_over else ""
    st.markdown(f'<div class="message {message_class}">{st.session_state.message}</div>', unsafe_allow_html=True)

# Input and controls
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if not st.session_state.game_over:
        guess_input = st.text_input(
            "Enter your guess:",
            max_chars=5,
            key="guess_input",
            label_visibility="collapsed",
            placeholder="Type a 5-letter word"
        )
        
        if st.button("Submit", use_container_width=True, type="primary"):
            if guess_input:
                process_guess(guess_input)
                st.rerun()
    else:
        if st.button("🔄 New Game", use_container_width=True, type="primary"):
            initialize_game()
            st.rerun()

# Keyboard display
st.markdown(render_keyboard(), unsafe_allow_html=True)

# Instructions (collapsible)
with st.expander("How to Play"):
    st.markdown("""
    **Guess the word in 6 tries!**
    
    - Each guess must be a valid 5-letter word
    - After each guess, the color of the tiles will change:
    
    🟩 **Green** = Letter is correct and in the right spot  
    🟨 **Yellow** = Letter is in the word but in the wrong spot  
    ⬛ **Gray** = Letter is not in the word
    
    **Tips:**
    - Start with words that have common letters (E, A, R, I, O, T)
    - Try to use different letters in each guess to narrow down possibilities
    """)