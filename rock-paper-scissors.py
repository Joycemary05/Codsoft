


import tkinter as tk
import random
import time
import winsound

root = tk.Tk()
root.title("Lavender & Pink Rock-Paper-Scissors")
root.geometry("400x500")
root.configure(bg="#F3E5F5")
root.resizable(False, False)

hands = {
    "rock": "✊",
    "paper": "🖐️",
    "scissors": "✌️"
}

choices = ["rock", "paper", "scissors"]
user_score = 0
comp_score = 0


def play_sound(type="click"):
    try:
        if type == "win":
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
        elif type == "lose":
            winsound.MessageBeep(winsound.MB_ICONHAND)
        elif type == "tie":
            winsound.MessageBeep(winsound.MB_OK)
        else:
            winsound.Beep(800, 100)
    except:
        pass  


label_info = tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Arial", 14, "bold"), bg="#F3E5F5", fg="#C2185B")
label_info.pack(pady=10)

label_user = tk.Label(root, text="You: ❓", font=("Arial", 30), bg="#F3E5F5", fg="#BA68C8")
label_user.pack(pady=5)

label_comp = tk.Label(root, text="Computer: ❓", font=("Arial", 30), bg="#F3E5F5", fg="#F06292")
label_comp.pack(pady=5)

label_result = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#F3E5F5", fg="#C2185B")
label_result.pack(pady=10)

label_score = tk.Label(root, text="You: 0 | Computer: 0", font=("Arial", 12), bg="#F3E5F5", fg="#AD1457")
label_score.pack(pady=10)


def play(choice):
    global user_score, comp_score
    label_result.config(text="")
    play_sound("click")

    
    for _ in range(3):
        label_user.config(text="You: 🤜")
        label_comp.config(text="Computer: 🤛")
        root.update()
        time.sleep(0.3)
        label_user.config(text="You: 🤛")
        label_comp.config(text="Computer: 🤜")
        root.update()
        time.sleep(0.3)

    
    comp_choice = random.choice(choices)
    label_user.config(text=f"You: {hands[choice]}")
    label_comp.config(text=f"Computer: {hands[comp_choice]}")

    if choice == comp_choice:
        result = "🤝 It's a tie!"
        play_sound("tie")
    elif (choice == "rock" and comp_choice == "scissors") or \
         (choice == "scissors" and comp_choice == "paper") or \
         (choice == "paper" and comp_choice == "rock"):
        result = "✅ You win!"
        user_score += 1
        play_sound("win")
    else:
        result = "❌ You lose!"
        comp_score += 1
        play_sound("lose")

    label_result.config(text=result)
    label_score.config(text=f"You: {user_score} | Computer: {comp_score}")


def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    label_user.config(text="You: ❓")
    label_comp.config(text="Computer: ❓")
    label_result.config(text="")
    label_score.config(text="You: 0 | Computer: 0")
    play_sound("click")


frame_buttons = tk.Frame(root, bg="#F3E5F5")
frame_buttons.pack(pady=20)

btn_style = {
    "font": ("Arial", 12, "bold"),
    "width": 10,
    "bg": "#F8BBD0",
    "fg": "#6A1B9A",
    "activebackground": "#F48FB1",
    "activeforeground": "#6A1B9A"
}

tk.Button(frame_buttons, text="Rock ✊", command=lambda: play("rock"), **btn_style).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Paper 🖐️", command=lambda: play("paper"), **btn_style).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Scissors ✌️", command=lambda: play("scissors"), **btn_style).grid(row=0, column=2, padx=5)


btn_reset = tk.Button(root, text="🔄 Reset", command=reset_game, font=("Arial", 12, "bold"),
                      bg="#E1BEE7", fg="#6A1B9A", activebackground="#CE93D8", activeforeground="#6A1B9A")
btn_reset.pack(pady=15)


root.mainloop()
