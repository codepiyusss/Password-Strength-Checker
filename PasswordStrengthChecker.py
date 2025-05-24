import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to check password strength
def check_password():
    password = entry.get()
    
    if len(password) < 8:
        strength = "Weak"
        suggestion = "Use at least 8 characters."
    elif not re.search(r"[A-Z]", password):
        strength = "Weak"
        suggestion = "Add at least one uppercase letter."
    elif not re.search(r"[a-z]", password):
        strength = "Weak"
        suggestion = "Add at least one lowercase letter."
    elif not re.search(r"[0-9]", password):
        strength = "Weak"
        suggestion = "Include at least one digit."
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength = "Medium"
        suggestion = "Add special characters to make it stronger."
    else:
        strength = "Strong"
        suggestion = "Great job! Your password looks strong."

    result_label.config(text=f"Strength: {strength}\nSuggestion: {suggestion}")

def draw_gradient(canvas, color1, color2):
    width = 450
    height = 300
    limit = height
    r1, g1, b1 = root.winfo_rgb(color1)
    r2, g2, b2 = root.winfo_rgb(color2)
    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit
    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr//256:02x}{ng//256:02x}{nb//256:02x}'
        canvas.create_line(0, i, width, i, fill=color)

# Toggle password visibility
def toggle_password():
    if entry.cget('show') == '▪':
        entry.config(show='')
        toggle_btn.config(text='🙈 Hide')
    else:
        entry.config(show='▪')
        toggle_btn.config(text='👁️ Show')

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x300")
root.configure(bg='#f0f2f5')
root.resizable(False, False)

canvas = tk.Canvas(root, width=450, height=300, highlightthickness=0)
canvas.place(x=0, y=0)
draw_gradient(canvas, "#a18cd1", "#fbc2eb")

frame = tk.Frame(root, draw_gradient(canvas, "#a18cd1", "#fbc2eb"), bd=5, relief='groove')
frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=250)

title_label = tk.Label(frame, text="🔐 Password Strength Checker", font=("Segoe UI", 14, 'bold'), bg='#ffffff')
title_label.pack(pady=10)

entry = tk.Entry(frame, show="▪", width=28, font=("Segoe UI", 12))
entry.pack(pady=5)

# Toggle button
toggle_btn = tk.Button(frame, text='👁️ Show', command=toggle_password, font=("Segoe UI", 10), bg="#fdc8f5", relief='flat')
toggle_btn.pack(pady=2)

check_button = tk.Button(frame, text="Check Strength", command=check_password, font=("Segoe UI", 12), bg="#0984e3", fg="white", relief='flat')
check_button.pack(pady=10)

result_label = tk.Label(frame, text="", font=("Segoe UI", 11), fg="#2d3436", bg='#ffffff', wraplength=350, justify="center")
result_label.pack(pady=5)

root.mainloop()
