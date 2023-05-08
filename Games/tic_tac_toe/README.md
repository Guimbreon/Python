# TIK TAK TOE

This is a simple command line program that allows two players to play a game of TIK TAK TOE.

## How to Use

1. Run the program in your terminal by running the command `python tiktaktoe.py`.
2. You'll be prompted to enter the symbols each player wants to play with.
3. The game will show the following model:
    ```
    1|2|3
    4|5|6
    7|8|9
    ```
    Players will have to enter the corresponding number of the spot they want to play in.
4. The program will randomly choose which player plays first.
5. Players will take turns entering their chosen spots until the game is over.
6. The program will declare the winner.

## Code Overview

The program is written in Python and consists of a single file `tiktaktoe.py`. It uses the built-in `random` library to choose which player plays first.

The program defines a `check` function that checks if any player has won or if the game is over. The `while` loop runs until the game is over. Within the loop, the program prompts the player to enter their chosen spot and checks if the spot is valid. If the spot is valid, the program checks if the spot is already taken by the other player, and if not, it fills the spot with the player's symbol. The program then calls the `check` function to check if the game is over.

If you choose a spot not in the model the code gave you, the code will error and stop the game!

After the game is over, the program declares the winner and prints the final game board.

## Contributing

If you find a bug or have a suggestion, please feel free to create an issue or submit a pull request.

## License

These projects are licensed under the GNU General Public License. See the `LICENSE` file in the start of the repositor
