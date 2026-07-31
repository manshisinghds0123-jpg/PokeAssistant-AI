import tkinter as tk
from tkinter import scrolledtext
import threading
from assistant import take_command, speak
# ==========================
# Create Window
# ==========================

root = tk.Tk()

root.title("🤖 PokeAssist AI")

root.geometry("700x500")

root.configure(bg="#1E1E2E")

# ==========================
# Title
# ==========================

title = tk.Label(
    root,
    text="🤖 PokeAssist AI",
    font=("Arial", 24, "bold"),
    bg="#1E1E2E",
    fg="white"
)

title.pack(pady=15)

# ==========================
# Status Label
# ==========================

status = tk.Label(
    root,
    text="Status : Ready",
    font=("Arial", 12),
    bg="#1E1E2E",
    fg="lightgreen"
)

status.pack()

# ==========================
# Conversation Box
# ==========================

conversation = scrolledtext.ScrolledText(
    root,
    width=70,
    height=18,
    font=("Consolas", 11)
)

conversation.pack(pady=20)

conversation.insert(tk.END, "Welcome to PokeAssist AI.\n")
conversation.insert(tk.END, "Assistant is ready.\n\n")
conversation.config(state="disabled")
# ==========================
# Buttons Frame
# ==========================

button_frame = tk.Frame(root, bg="#1E1E2E")

button_frame.pack(pady=10)

# ==========================
# Start Button
# ==========================

start_button = tk.Button(
    button_frame,
    text="🎤 Start Listening",
    command=start_listening,
    width=18,
    height=2,
    bg="green",
    fg="white"
)


start_button.grid(row=0, column=0, padx=10)

# ==========================
# Stop Button
# ==========================

stop_button = tk.Button(
    button_frame,
    text="⏹ Stop",
    command=stop_listening,
    width=18,
    height=2,
    bg="red",
    fg="white"
)

stop_button.grid(row=0, column=1, padx=10)

# ==========================
# Exit Button
# ==========================

exit_button = tk.Button(
    button_frame,
    text="❌ Exit",
    width=18,
    height=2,
    bg="gray",
    fg="white",
    command=root.destroy
)

exit_button.grid(row=0, column=2, padx=10)

# ==========================
# Run Window
# ==========================
# ==========================
# Assistant Running Flag
# ==========================

running = False

# ==========================
# Listen Function
# ==========================

def listen():

    global running

    while running:

        status.config(text="🎤 Listening...", fg="yellow")

        command = take_command()
        

        conversation.config(state="normal")
        conversation.insert(tk.END, "You: " + command + "\n")
        conversation.see(tk.END)
        conversation.config(state="disabled")
        if "hello" in command:
         reply = "Hello Mansi."

        elif "how are you" in command:
         reply = "I am doing great."

        elif "open chrome" in command:
         reply = "Opening Chrome"

        elif "open youtube" in command:
         reply = "Opening YouTube"

        elif "open chatgpt" in command or ("chat" in command and "gpt" in command):
         reply = "Opening ChatGPT"

        elif "exit" in command:
         stop_listening()
         return

        else:
            reply = "Command received."

        conversation.config(state="normal")
        conversation.insert(tk.END, "Assistant : " + reply + "\n\n")
        conversation.see(tk.END)
        conversation.config(state="disabled")

        status.config(text="🤖 Speaking...", fg="cyan")

        speak(reply)

        status.config(text="🎤 Listening...", fg="yellow")

    status.config(text="Status : Ready", fg="lightgreen")

# ==========================
# Start Button
# ==========================

def start_listening():

    global running

    if running:
        return

    running = True

    threading.Thread(target=listen, daemon=True).start()

# ==========================
# Stop Button
# ==========================

def stop_listening():

    global running

    running = False

    status.config(text="Stopped", fg="red")
root.mainloop()