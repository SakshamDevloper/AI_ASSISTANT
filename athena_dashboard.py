import customtkinter as ctk
import tkinter as tk
import numpy as np
import sounddevice as sd
import threading
import math
import time
import random
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("ATHENA AI CORE")
app.geometry("1000x720")

title = ctk.CTkLabel(app, text="ATHENA AI CORE", font=("Orbitron", 34))
title.pack(pady=10)

status = ctk.CTkLabel(app, text="STATUS : IDLE", font=("Arial", 14))
status.pack()

canvas = tk.Canvas(app, width=600, height=350, bg="#020617", highlightthickness=0)
canvas.pack()

center_x = 300
center_y = 170
core_radius = 35

core = canvas.create_oval(
    center_x-core_radius,
    center_y-core_radius,
    center_x+core_radius,
    center_y+core_radius,
    fill="#00ffff",
    outline=""
)

bars = []

def draw_visualizer(level):

    canvas.delete("bars")

    bar_count = 60
    radius = 90

    for i in range(bar_count):

        angle = i * (360/bar_count)
        rad = math.radians(angle)

        bar_height = level * random.uniform(20,80)

        x1 = center_x + radius * math.cos(rad)
        y1 = center_y + radius * math.sin(rad)

        x2 = center_x + (radius+bar_height) * math.cos(rad)
        y2 = center_y + (radius+bar_height) * math.sin(rad)

        canvas.create_line(
            x1,y1,x2,y2,
            fill="#38bdf8",
            width=3,
            tags="bars"
        )

def mic_stream():

    def callback(indata, frames, time_, status_):

        volume = np.linalg.norm(indata)*10
        draw_visualizer(volume)

    with sd.InputStream(callback=callback):
        while listening:
            time.sleep(0.05)

def animate_core():

    glow = random.randint(30,70)

    canvas.itemconfig(core, fill=f"#00{glow:02x}{glow:02x}")

    app.after(120, animate_core)

animate_core()

chat = ctk.CTkTextbox(app, width=850, height=200)
chat.pack(pady=10)

def add_chat(text):

    chat.insert("end", text+"\n")
    chat.see("end")

def type_response(text):

    status.configure(text="STATUS : RESPONDING")

    current = ""

    for char in text:

        current += char
        chat.delete("end-1l","end")
        chat.insert("end","Athena: "+current)
        chat.see("end")

        time.sleep(0.02)

def thinking():

    dots = ["." , ".." , "..."]

    for i in range(6):

        status.configure(text="ATHENA THINKING"+dots[i%3])
        time.sleep(0.4)

def beep():

    if sys.platform == "win32":
        import winsound
        winsound.Beep(800,120)

listening = False

def start_listen():

    global listening
    listening = True

    beep()
    status.configure(text="STATUS : LISTENING")

    threading.Thread(target=mic_stream,daemon=True).start()

def stop_listen():

    global listening
    listening = False

    beep()
    status.configure(text="STATUS : IDLE")

def demo_ai():

    add_chat("You: hello athena")

    thinking()

    response = random.choice([
        "Hello Saksham. How can I assist you today?",
        "Athena online. All systems operational.",
        "Voice interface active."
    ])

    type_response(response)

controls = ctk.CTkFrame(app)
controls.pack(pady=12)

mic_btn = ctk.CTkButton(
    controls,
    text="START LISTENING",
    width=180,
    command=start_listen
)

mic_btn.grid(row=0,column=0,padx=10)

stop_btn = ctk.CTkButton(
    controls,
    text="STOP",
    width=120,
    command=stop_listen
)

stop_btn.grid(row=0,column=1,padx=10)

demo_btn = ctk.CTkButton(
    controls,
    text="TEST AI RESPONSE",
    command=demo_ai
)

demo_btn.grid(row=0,column=2,padx=10)

footer = ctk.CTkLabel(app,text="ATHENA • ADVANCED VOICE INTERFACE",font=("Arial",12))
footer.pack(pady=6)

app.mainloop()