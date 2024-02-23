import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
window = tk.Tk()
window.title("Simple GUI Example")

# Create and pack a label
label = tk.Label(window, text="Enter your name:")
label.pack()

# Create and pack an entry widget
entry = tk.Entry(window)
entry.pack()

# Create and pack a button with an event handler
button = tk.Button(window, text="keshav", command=on_button_click)
button.pack()

# Start the GUI event loop
window.mainloop()
