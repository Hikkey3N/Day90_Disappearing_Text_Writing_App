import tkinter as tk
from text_box import TextBox
import time

############################## GLOBAL VARIABLES ##############################
BG_COLOR = "#EA738D"

def on_key_pressed(event):
    # Check if the pressed key is a printable character or a tab
    if event.char and (event.char.isprintable() or event.char == '\t'):
        tb.reset_timer()
        print("A printable character or Tab was pressed:", event.char)

# Create the main window
root = tk.Tk()
root.geometry("1200x1000")
root.configure(bg=BG_COLOR)
tb = TextBox(root)


# Bind the key press event to the on_key_pressed function for the text box widget
tb.textbox.bind("<Key>", on_key_pressed)

# Start the Tkinter event loop
root.mainloop()
