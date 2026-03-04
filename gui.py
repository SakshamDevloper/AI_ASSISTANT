import customtkinter as ctk
import threading

from assistant.speech import take_command
from assistant.speak import speak
from assistant.commands import execute_command

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("700x550")
app.title("Athena AI Assistant")

title = ctk.CTkLabel(app, text="ATHENA AI ASSISTANT", font=("Arial", 28))
title.pack(pady=15)

status_label = ctk.CTkLabel(app, text="Status: Idle", font=("Arial", 16))
status_label.pack(pady=5)

chat_box = ctk.CTkTextbox(app, width=600, height=300)
chat_box.pack(pady=20)

def add_chat(text):
    chat_box.insert("end", text + "\n")
    chat_box.see("end")

def listen():

    status_label.configure(text="Status: Listening...")

    command = take_command()

    if command:

        add_chat("You: " + command)

        status_label.configure(text="Status: Thinking...")

        result = execute_command(command)

        status_label.configure(text="Status: Idle")

def mic_thread():
    threading.Thread(target=listen).start()

mic_button = ctk.CTkButton(
    app,
    text="🎤 Speak",
    width=200,
    height=50,
    command=mic_thread
)

mic_button.pack(pady=15)

exit_button = ctk.CTkButton(
    app,
    text="Exit",
    width=120,
    command=app.destroy
)

exit_button.pack(pady=10)

app.mainloop()