# Internpe_Task_1
This code is an implementation of the classic game Tic-Tac-Toe using the Tkinter library in Python. Here's a summary of what the code does:

1. It imports the necessary modules: `tkinter` for creating the GUI and `random` for generating random moves for the computer player.

2. It initializes the game board, which is represented by a list of 9 elements. Each element corresponds to a position on the board and is initially set to a space character (' ') to represent an empty position.

3. The code defines several helper functions:
   - `is_board_full()` checks if the board is full by checking if there are any empty positions left.
   - `is_winner(player)` checks if a player has won by examining the board's rows, columns, and diagonals.
   - `handle_click(position)` is the event handler for button clicks. It updates the board, checks for a win or tie, toggles the player, and triggers the computer player's move.
   - `reset_game()` resets the game by clearing the board and resetting the buttons to their initial state.
   - `toggle_player()` switches the current player between 'X' and 'O'.
   - `computer()` handles the computer player's move. It generates a random position and makes a move if the position is available.

4. The code creates the main window using Tkinter and sets the title to "Tic-Tac-Toe".

5. It creates the buttons for the game board using a loop. Each button is assigned a command that calls the `handle_click()` function with the corresponding position as an argument.

6. It creates a label to display the current player and places it at the bottom of the window.

7. The initial player is set to 'X'.

8. The game starts by entering the main event loop with `window.mainloop()`, which allows the GUI to be displayed and handles user interactions.

In summary, this code sets up a Tic-Tac-Toe game where the user plays against a computer player. The user can click on the buttons to make moves, and the computer player makes random moves. The game checks for a win or tie and allows the user to reset the game.
