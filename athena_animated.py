import customtkinter as ctk
import tkinter as tk
import numpy as np
import sounddevice as sd
import threading
import math
import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("ATHENA AI")
app.geometry("900x650")

title = ctk.CTkLabel(app, text="ATHENA AI SYSTEM", font=("Arial",28))
title.pack(pady=10)

status = ctk.CTkLabel(app, text="STATUS : IDLE")
status.pack()

canvas = tk.Canvas(app,width=600,height=350,bg="#020617",highlightthickness=0)
canvas.pack(pady=20)

center_x = 300
center_y = 170

angle = 0
pulse = 0

core = canvas.create_oval(
center_x-30,center_y-30,
center_x+30,center_y+30,
fill="#00ffff",outline=""
)

wave_points = []

def animate():

    global angle,pulse

    canvas.delete("ring")

    radius = 90
    points = []

    for i in range(0,360,10):

        rad = math.radians(i+angle)
        x = center_x + radius*math.cos(rad)
        y = center_y + radius*math.sin(rad)

        points.append(x)
        points.append(y)

    canvas.create_polygon(
        points,
        outline="#38bdf8",
        fill="",
        width=2,
        smooth=True,
        tags="ring"
    )

    pulse_size = 30 + abs(math.sin(pulse))*10

    canvas.coords(
        core,
        center_x-pulse_size,
        center_y-pulse_size,
        center_x+pulse_size,
        center_y+pulse_size
    )

    pulse += 0.1
    angle += 2

    app.after(30,animate)

animate()

bars = []

def draw_wave(level):

    canvas.delete("wave")

    for i in range(40):

        x = 40 + i*12
        height = level*np.random.uniform(10,60)

        canvas.create_line(
            x,320,
            x,320-height,
            fill="#22d3ee",
            width=3,
            tags="wave"
        )

def mic_stream():

    def callback(indata,frames,time,status):

        volume = np.linalg.norm(indata)*10
        draw_wave(volume)

    with sd.InputStream(callback=callback):

        while listening:
            time.sleep(0.05)

chat = ctk.CTkTextbox(app,width=700,height=180)
chat.pack()

def add_chat(text):

    chat.insert("end",text+"\n")
    chat.see("end")

listening = False

def start_listen():

    global listening
    listening = True

    status.configure(text="STATUS : LISTENING")

    threading.Thread(target=mic_stream,daemon=True).start()

def stop_listen():

    global listening
    listening = False
    status.configure(text="STATUS : IDLE")

controls = ctk.CTkFrame(app)
controls.pack(pady=10)

start_btn = ctk.CTkButton(
controls,
text="START",
command=start_listen
)

start_btn.grid(row=0,column=0,padx=10)

stop_btn = ctk.CTkButton(
controls,
text="STOP",
command=stop_listen
)

stop_btn.grid(row=0,column=1,padx=10)

app.mainloop()