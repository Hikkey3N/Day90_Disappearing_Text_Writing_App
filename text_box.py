import tkinter as tk
import time

class TextBox:
    def __init__(self, master):
        self.master = master
        self.elapsed_time = 0
        self.timer_running = False
        self.timer_event = None     

        self.timer_label = tk.Label(self.master, text="Elapsed Time: 0 seconds")
        self.timer_label.pack(padx=10, pady=10)

         # Create a Label widget with the specified text, font, and color
        self.info_label = tk.Label(self.master, text="If you don't type anything within 5 seconds, the text will automatically disappear",
                                    font=("Helvetica", 20), fg="black", bg="#EA738D")
        self.info_label.pack(pady=20)

        # Create a textbox widget with the specified text, font, and color
        self.textbox = tk.Text(self.master, width=80, height=30, font=("Helvetica", 16))
        self.textbox.pack(pady=20)

    def start_timer(self):
        # Start the timer if not already running
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        # Update the timer label with the elapsed time if the timer is running
        if self.timer_running:
            if self.elapsed_time == 0:
                self.textbox.config(foreground="black")
            if self.elapsed_time == 3:
                self.textbox.config(foreground="blue")
            if self.elapsed_time == 4:
                self.textbox.config(foreground="orange")
            if self.elapsed_time == 5:
                self.textbox.config(foreground="red")

            if self.elapsed_time == 6:
                self.textbox.delete('1.0', tk.END)
                self.reset_timer()

            else:
                self.timer_label.config(text=f"Elapsed Time: {self.elapsed_time} seconds")
                self.elapsed_time += 1
                # Schedule the update_timer function to be called again after 1000 milliseconds (1 second)
                self.timer_event = self.master.after(1000, self.update_timer)

            
    
    def reset_timer(self):
        # Stop the timer and reset the elapsed time
        self.timer_running = False
        self.elapsed_time = 0
        self.timer_label.config(text="Elapsed Time: 0 seconds")
        # Cancel any pending timer events
        if self.timer_event:
            self.master.after_cancel(self.timer_event)
            
        self.start_timer()