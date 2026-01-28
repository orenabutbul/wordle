# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.1.0] - 2026-01-27

### Added
- **Dark/Light Mode Toggle**: Added theme switching capability with a toggle button (🌙/☀️) in the top-right corner
- **Light Mode Theme**: New light theme with white background and adjusted colors for better visibility
- **Version Display**: Version number now shown at the bottom of the app
- **Streamlit Configuration**: Added `.streamlit/config.toml` for headless server mode

### Changed
- Refactored CSS styling into `get_theme_css()` function for dynamic theme generation
- Updated tile, keyboard, and UI element colors to support both themes
- Improved color contrast for light mode accessibility

### Theme Colors
| Element | Dark Mode | Light Mode |
|---------|-----------|------------|
| Background | #121213 | #ffffff |
| Text | #ffffff | #1a1a1b |
| Correct (Green) | #538d4e | #6aaa64 |
| Present (Yellow) | #b59f3b | #c9b458 |
| Absent (Gray) | #3a3a3c | #787c7e |

## [1.0.0] - 2026-01-27

### Added
- Initial release of Wordle Clone
- **Game Board**: 6x5 grid for displaying guesses
- **Color-Coded Feedback**: Green (correct), Yellow (present), Gray (absent)
- **On-Screen Keyboard**: Visual keyboard showing letter states
- **Word Validation**: Validates guesses against word list
- **Win/Lose Detection**: Tracks game state and displays appropriate messages
- **New Game Button**: Allows starting a fresh game
- **How to Play Section**: Collapsible instructions for new players

### Technical
- Built with Python and Streamlit
- Session state management for game persistence
- Custom CSS styling for authentic Wordle appearance
- Word lists with ~500+ answer words and extended valid guesses