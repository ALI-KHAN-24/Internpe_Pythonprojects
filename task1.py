import tkinter as tk
from tkinter import messagebox
import random

# Create the game board
board = [' ' for _ in range(9)]

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to check if a player has won
def is_winner(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to handle button click event
def handle_click(position):
    if board[position] == ' ':
        button = buttons[position]
        button.config(text=current_player)
        board[position] = current_player

        if is_winner(current_player):
            messagebox.showinfo("Game Over", "Player " + current_player + " wins!")
            reset_game()
        elif is_board_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            toggle_player()
            computer()  # Call computer player's move

    else:
        messagebox.showerror("Invalid Move", "Position already occupied. Try again.")

# Function to reset the game
def reset_game():
    for i in range(9):
        board[i] = ' '
        buttons[i].config(text=' ')
    toggle_player()

# Function to toggle the current player
def toggle_player():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'
    status_label.config(text="Current Player: " + current_player)

# Function for computer player's move
def computer():
    while current_player == 'O':
        position = random.randint(0, 8)
        if board[position] == ' ':
            button = buttons[position]
            button.config(text=current_player)
            board[position] = current_player
            toggle_player()
            break

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create the buttons
buttons = []
for i in range(9):
    button = tk.Button(window, text=' ', width=10, height=4, command=lambda pos=i: handle_click(pos))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Create the status label
status_label = tk.Label(window, text="Current Player: X", font=('Arial', 12))
status_label.grid(row=3, column=0, columnspan=3)

# Set the initial player
current_player = 'X'

# Start the game
window.mainloop()
