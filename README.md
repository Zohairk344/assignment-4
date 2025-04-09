# Python Projects

## Overview
This repository contains various Python projects, including games and utilities, demonstrating different programming concepts and techniques.

## Projects

### 1. Guess the Number Game
- **File:** `assignment3/guess_number.py`
- **Description:** A simple number guessing game where the user can either guess a number chosen by the computer or let the computer guess a number chosen by the user.
- **Functions:**
  - `main(x)`: User guesses a number between 1 and `x`.
  - `Computer_Guess(x)`: The computer guesses a number based on user feedback.

### 2. Rock, Paper, Scissors Game
- **File:** `assignment3/rock_paper_scissor.py`
- **Description:** A classic game where the user plays against the computer.
- **Functions:**
  - `play()`: Initiates the game and determines the winner.
  - `Is_Win(Player, Opponent)`: Checks if the player wins against the opponent.

### 3. Hangman Game
- **File:** `assignment3/hangman/game.py`
- **Description:** A word-guessing game where the player tries to guess a hidden word.
- **Functions:**
  - `get_valid_word(words)`: Selects a valid word for the game.
  - `hangman()`: Main game loop for playing Hangman.

### 4. Countdown Timer
- **File:** `assignment3/countdown_timer.py`
- **Description:** A simple countdown timer that counts down from a specified number of seconds.
- **Functions:**
  - `Countdown(Time)`: Starts the countdown based on the input time.

### 5. Mad Libs Game
- **File:** `assignment3/madlib.py`
- **Description:** A fun game where users fill in the blanks to create a silly story.
- **Functions:**
  - `main()`: Collects user inputs and generates the mad lib story.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repositoryname.git
   ```
2. Navigate to the project directory:
   ```bash
   cd repositoryname
   ```

## Usage
To run any of the projects, navigate to the respective directory and execute the Python file. For example, to run the Guess the Number game:
```bash
python assignment3/guess_number.py
```

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
