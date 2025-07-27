import tkinter as tk
import random

# Function to play the game
def play_game():
    user_roll = random.randint(1, 6)
    comp_roll = random.randint(1, 6)

    result = ""
    if user_roll > comp_roll:
        result = "🎉 You Win!"
    elif user_roll < comp_roll:
        result = "😞 You Lose!"
    else:
        result = "😐 It's a Draw!"

    user_label.config(text=f"You rolled: {user_roll}")
    comp_label.config(text=f"Computer rolled: {comp_roll}")
    result_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("Dice Game: You vs Computer")
root.geometry("300x200")
root.maxsize(300,200)
root.minsize(300,200)
root.configure(bg="sky blue")

# Play button
play_button = tk.Button(root,bg="blue", text="Roll Dice 🎲", command=play_game, font=("Arial", 14),relief="raised",borderwidth=9)
play_button.pack(pady=15)

# Labels
user_label = tk.Label(root, text="", font=("Arial", 12),fg="blue")
user_label.pack()

comp_label = tk.Label(root, text="", font=("Arial", 12),fg="blue")
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"),fg="blue")
result_label.pack(pady=10)

root.mainloop()
