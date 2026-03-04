import customtkinter as ctk
import threading
import random
import math
import tkinter as tk

from assistant.speech import take_command
from assistant.commands import execute_command

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("ATHENA AI")
app.geometry("900x650")

title = ctk.CTkLabel(app, text="ATHENA AI SYSTEM", font=("Orbitron", 30))
title.pack(pady=10)

status = ctk.CTkLabel(app, text="STATUS: IDLE", font=("Arial", 14))
status.pack()

canvas = tk.Canvas(app, width=400, height=250, bg="#0f172a", highlightthickness=0)
canvas.pack(pady=20)

center_x = 200
center_y = 120
radius = 40

orb = canvas.create_oval(
    center_x - radius,
    center_y - radius,
    center_x + radius,
    center_y + radius,
    fill="#00ffff",
    outline=""
)

wave_lines = []


def animate_waves():
    canvas.delete("wave")

    for i in range(30):

        x = i * 15
        height = random.randint(10, 60)

        canvas.create_line(
            x,
            200,
            x,
            200 - height,
            fill="#38bdf8",
            width=3,
            tags="wave"
        )

    app.after(120, animate_waves)


animate_waves()

chat = ctk.CTkTextbox(app, width=650, height=200)
chat.pack(pady=10)


def add_chat(text):
    chat.insert("end", text + "\n")
    chat.see("end")

mic_frame = ctk.CTkFrame(app)
mic_frame.pack(pady=15)


def listen():

    status.configure(text="STATUS: LISTENING")

    command = take_command()

    if command:

        add_chat("You: " + command)

        status.configure(text="STATUS: PROCESSING")

        execute_command(command)

        status.configure(text="STATUS: IDLE")


def mic_pressed():
    threading.Thread(target=listen).start()

mic_button = ctk.CTkButton(
    mic_frame,
    text="ACTIVATE ATHENA",
    width=220,
    height=50,
    command=mic_pressed
)

mic_button.pack()

footer = ctk.CTkLabel(app, text="ATHENA AI • Voice Interface", font=("Arial", 12))
footer.pack(pady=10)

app.mainloop()