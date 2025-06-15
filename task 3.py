import tkinter as tk
from time import time, strftime

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.start_time = None
        self.running = False
        self.elapsed_time = 0

        self.label = tk.Label(root, text="00:00:000", font=("Arial", 40))
        self.label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.update_display()

    def update_display(self):
        if self.running:
            elapsed = time() - self.start_time + self.elapsed_time
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            milliseconds = int((elapsed * 1000) % 1000)
            self.label.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:03}")
        self.root.after(50, self.update_display)

    def start(self):
        if not self.running:
            self.start_time = time()
            self.running = True

    def pause(self):
        if self.running:
            self.elapsed_time += time() - self.start_time
            self.running = False

    def reset(self):
        self.start_time = None
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="00:00:000")

root = tk.Tk()
app = Stopwatch(root)
root.mainloop()
