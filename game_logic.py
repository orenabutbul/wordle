"""
Core game logic for Wordle.
"""

from enum import Enum
from typing import List, Tuple


class LetterState(Enum):
    """State of a letter in a guess."""
    CORRECT = "correct"      # Green - right letter, right position
    PRESENT = "present"      # Yellow - right letter, wrong position
    ABSENT = "absent"        # Gray - letter not in word


def check_guess(guess: str, answer: str) -> List[LetterState]:
    """
    Check a guess against the answer and return the state of each letter.
    
    Args:
        guess: The 5-letter guess (lowercase)
        answer: The 5-letter answer (lowercase)
    
    Returns:
        List of LetterState for each position in the guess
    """
    guess = guess.lower()
    answer = answer.lower()
    
    result = [LetterState.ABSENT] * 5
    answer_chars = list(answer)
    
    # First pass: mark correct letters (green)
    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = LetterState.CORRECT
            answer_chars[i] = None  # Mark as used
    
    # Second pass: mark present letters (yellow)
    for i in range(5):
        if result[i] == LetterState.CORRECT:
            continue
        if guess[i] in answer_chars:
            result[i] = LetterState.PRESENT
            # Remove first occurrence to handle duplicates correctly
            answer_chars[answer_chars.index(guess[i])] = None
    
    return result


def get_keyboard_states(guesses: List[str], results: List[List[LetterState]]) -> dict:
    """
    Get the state of each letter on the keyboard based on all guesses.
    
    Priority: CORRECT > PRESENT > ABSENT
    
    Args:
        guesses: List of guessed words
        results: List of results for each guess
    
    Returns:
        Dictionary mapping each letter to its best state
    """
    keyboard_states = {}
    
    for guess, result in zip(guesses, results):
        for letter, state in zip(guess.lower(), result):
            current_state = keyboard_states.get(letter)
            
            # Update state based on priority
            if current_state is None:
                keyboard_states[letter] = state
            elif state == LetterState.CORRECT:
                keyboard_states[letter] = LetterState.CORRECT
            elif state == LetterState.PRESENT and current_state != LetterState.CORRECT:
                keyboard_states[letter] = LetterState.PRESENT
            # ABSENT doesn't override anything
    
    return keyboard_states


def is_valid_guess(guess: str, valid_words: List[str]) -> Tuple[bool, str]:
    """
    Validate a guess.
    
    Args:
        guess: The word to validate
        valid_words: List of valid words
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    guess = guess.lower().strip()
    
    if len(guess) != 5:
        return False, "Word must be 5 letters"
    
    if not guess.isalpha():
        return False, "Word must contain only letters"
    
    if guess not in valid_words:
        return False, "Not in word list"
    
    return True, ""