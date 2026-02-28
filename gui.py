import customtkinter as ctk
from main import run_assistant

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Athena AI Assistant")
app.geometry("500x400")

title = ctk.CTkLabel(app, text="ATHENA AI ASSISTANT", font=("Arial", 20))
title.pack(pady=30)

def start():
    run_assistant()

start_button = ctk.CTkButton(app, text="Start Assistant", command=start)
start_button.pack(pady=20)

exit_button = ctk.CTkButton(app, text="Exit", command=app.destroy)
exit_button.pack(pady=10)

app.mainloop()