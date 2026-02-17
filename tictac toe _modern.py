import tkinter as tk
from tkinter import messagebox
import random

# -------------------------
# Game Setup
# -------------------------
root = tk.Tk()
root.title("Modern Tic Tac Toe")
root.geometry("400x520")
root.configure(bg="#121212")
root.resizable(False, False)

current_player = "X"
board = [""] * 9
score_x = 0
score_o = 0
vs_ai = True  # Change to False for 2-player mode


# -------------------------
# Functions
# -------------------------

def check_winner():
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            highlight_winner(combo)
            return board[combo[0]]
    if "" not in board:
        return "Tie"
    return None


def highlight_winner(combo):
    for index in combo:
        buttons[index].configure(bg="#00FFAA")


def ai_move():
    empty_spots = [i for i in range(9) if board[i] == ""]
    if empty_spots:
        move = random.choice(empty_spots)
        make_move(move)


def make_move(index):
    global current_player, score_x, score_o

    if board[index] == "":
        board[index] = current_player
        buttons[index].configure(text=current_player)

        winner = check_winner()

        if winner:
            if winner == "X":
                score_x += 1
                messagebox.showinfo("Game Over", "Player X Wins!")
            elif winner == "O":
                score_o += 1
                messagebox.showinfo("Game Over", "Player O Wins!")
            else:
                messagebox.showinfo("Game Over", "It's a Tie!")

            update_score()
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            turn_label.config(text=f"Turn: {current_player}")

            if vs_ai and current_player == "O":
                root.after(500, ai_move)


def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    turn_label.config(text="Turn: X")
    for button in buttons:
        button.configure(text="", bg="#1E1E1E")


def update_score():
    score_label.config(text=f"Score  X: {score_x}   O: {score_o}")


# -------------------------
# UI Layout
# -------------------------

title = tk.Label(root, text="Tic Tac Toe", font=("Helvetica", 22, "bold"),
                 bg="#121212", fg="#00FFAA")
title.pack(pady=10)

turn_label = tk.Label(root, text="Turn: X", font=("Helvetica", 14),
                      bg="#121212", fg="white")
turn_label.pack()

score_label = tk.Label(root, text="Score  X: 0   O: 0",
                       font=("Helvetica", 12),
                       bg="#121212", fg="#BBBBBB")
score_label.pack(pady=5)

frame = tk.Frame(root, bg="#121212")
frame.pack(pady=20)

buttons = []
for i in range(9):
    button = tk.Button(frame, text="", font=("Helvetica", 24, "bold"),
                       width=5, height=2,
                       bg="#1E1E1E", fg="white",
                       activebackground="#333333",
                       relief="flat",
                       command=lambda i=i: make_move(i))
    button.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(button)

reset_button = tk.Button(root, text="Restart Game",
                         font=("Helvetica", 12, "bold"),
                         bg="#00FFAA", fg="black",
                         relief="flat",
                         command=reset_board)
reset_button.pack(pady=20)

root.mainloop()
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    
    import os
os.system('am start -a android.intent.action.VIEW -d "file:///storage/emulated/0/TicTacToe/index.html"')