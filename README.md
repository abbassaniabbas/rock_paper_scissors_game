# Rock, Paper, Scissors

A simple Python command-line game where you play one round of Rock, Paper,
Scissors against the computer.

## Requirements

- Python 3.6 or later.
- No external packages are needed; the game uses Python's built-in `random` module.

## How to Run

1. Open a terminal and navigate to the project folder:

   ```bash
   cd "/Users/Abbas/Documents/ChatGPT/FlexiSAF Project"
   ```

   If you saved the project elsewhere, use that folder's path instead.

2. Start the game:

   ```bash
   python3 rock_paper_scissors.py
   ```

3. Type `rock`, `paper`, or `scissors`, then press Enter.

The program accepts uppercase or lowercase input and ignores surrounding spaces.
If you enter an invalid choice, it asks you to try again. The computer randomly
chooses an option, and the program displays both choices and the result.

## Game Rules

- Rock beats scissors.
- Paper beats rock.
- Scissors beats paper.
- Matching choices result in a tie.

The program ends after one valid round. Run it again to play another round.

## Example

```text
Welcome to Rock, Paper, Scissors!
Choose rock, paper, or scissors: rock
You chose: rock
Computer chose: scissors
You win!
```

The computer's choice is random, so your result may differ.

## Project Files

- `rock_paper_scissors.py`: User input, random computer choice, and winner determination.
- `README.md`: Project overview and instructions.
