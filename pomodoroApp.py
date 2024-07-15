import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        self.default_study_time = 25 * 60  # Default 25 minutes
        self.default_break_time = 5 * 60  # Default 5 minutes

        self.study_time = self.default_study_time
        self.break_time = self.default_break_time

        self.timer_running = False
        self.current_time = 0

        self.create_widgets()
        self.update_timer_label()

    def create_widgets(self):
        self.timer_label = tk.Label(self.root, text="00:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=20)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=20)

        self.settings_button = tk.Button(self.root, text="Settings", command=self.open_settings)
        self.settings_button.pack(side=tk.LEFT, padx=20)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.current_time = self.study_time
            self.update_timer_label()
            threading.Thread(target=self.run_timer).start()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.stop_timer()
        self.current_time = self.study_time
        self.update_timer_label()

    def run_timer(self):
        while self.timer_running and self.current_time > 0:
            time.sleep(1)
            self.current_time -= 1
            self.update_timer_label()
        if self.current_time == 0:
            winsound.Beep(1000, 1000)
            messagebox.showinfo("Pomodoro Timer", "Time's up!")
            self.start_break()

    def start_break(self):
        self.current_time = self.break_time
        self.update_timer_label()
        threading.Thread(target=self.run_timer).start()

    def update_timer_label(self):
        minutes, seconds = divmod(self.current_time, 60)
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")

    def open_settings(self):
        self.settings_window = tk.Toplevel(self.root)
        self.settings_window.title("Settings")

        tk.Label(self.settings_window, text="Study Time (minutes):").pack(pady=5)
        self.study_time_entry = tk.Entry(self.settings_window)
        self.study_time_entry.pack(pady=5)
        self.study_time_entry.insert(0, str(self.study_time // 60))

        tk.Label(self.settings_window, text="Break Time (minutes):").pack(pady=5)
        self.break_time_entry = tk.Entry(self.settings_window)
        self.break_time_entry.pack(pady=5)
        self.break_time_entry.insert(0, str(self.break_time // 60))

        tk.Button(self.settings_window, text="Save", command=self.save_settings).pack(pady=20)

    def save_settings(self):
        try:
            self.study_time = int(self.study_time_entry.get()) * 60
            self.break_time = int(self.break_time_entry.get()) * 60
            self.reset_timer()
            self.settings_window.destroy()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for study and break times.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
