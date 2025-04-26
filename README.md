# Scissors Paper Stone Game

A simple command-line implementation of the classic "Scissors, Paper, Stone" game (also known as Rock, Paper, Scissors) built in Python. Play against a computer opponent that randomly selects its move.

## Game Features

- Play the classic Scissors, Paper, Stone game against the computer
- Simple command-line interface
- Score tracking throughout your session
- Option to play multiple rounds
- Clear game instructions and feedback

## Prerequisites

- Python 3.x or higher

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Troaxx/scissorsPaperStone.git
   cd scissorsPaperStone
   ```

2. No additional dependencies required. This project only uses Python's standard library.

## How to Play

Run the game using:
```bash
python scissorsPaperStone.py
```

### Game Rules
- Scissors cuts Paper
- Paper covers Stone
- Stone breaks Scissors

### Controls
Follow the on-screen prompts to:
- Choose your move by entering the corresponding number
- Play multiple rounds
- View your current score against the computer

## Example Gameplay

```
Welcome to Scissors, Paper, Stone!
Choose an option:
1. Scissors
2. Paper
3. Stone
4. Quit
Enter your choice (1-4): 2

You chose Paper
Computer chose Scissors
Scissors cuts Paper. You lose!

Score: Computer 1 - You 0

Play again? (Y/N): y

Welcome to Scissors, Paper, Stone!
Choose an option:
1. Scissors
2. Paper
3. Stone
4. Quit
Enter your choice (1-4): 3

You chose Stone
Computer chose Scissors
Stone breaks Scissors. You win!

Score: Computer 1 - You 1

Play again? (Y/N): n

Thanks for playing! Final Score: Computer 1 - You 1
```

## Project Structure
```
├── scissorsPaperStone.py  # Main game file
├── README.md              # This documentation
└── LICENSE                # MIT License
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request if you'd like to improve the game.

Potential enhancements:
- Add a graphical user interface
- Implement additional moves (like Rock, Paper, Scissors, Lizard, Spock)
- Add difficulty levels for the computer player
- Save high scores to a file
