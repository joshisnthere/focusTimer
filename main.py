"""
Focus Timer

A pomodoro-style work/break timer that keeps a local log of your sessions
and draws a plain bar chart of focus minutes per day directly on a canvas
-- no charting library needed.
"""

import customtkinter as ctk

import session_log as log

ctk.set_appearance_mode("dark")

BG = "#0b0d10"
PANEL = "#171a1e"
ACCENT = "#6fd3c7"

WORK_MINUTES = 25
BREAK_MINUTES = 5


class FocusTimerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Focus Timer")
        self.geometry("640x560")
        self.configure(fg_color=BG)

        self.mode = "work"
        self.seconds_left = WORK_MINUTES * 60
        self.running = False

        self.time_var = ctk.StringVar(value=self._format(self.seconds_left))
        ctk.CTkLabel(self, textvariable=self.time_var, font=ctk.CTkFont(size=54, weight="bold"),
                     text_color=ACCENT).pack(pady=(30, 4))

        self.mode_var = ctk.StringVar(value="Focus session")
        ctk.CTkLabel(self, textvariable=self.mode_var, text_color="#8a8a8a").pack()

        button_row = ctk.CTkFrame(self, fg_color=BG)
        button_row.pack(pady=20)
        self.toggle_btn = ctk.CTkButton(button_row, text="Start", fg_color="#2a2a30",
                                        command=self._toggle)
        self.toggle_btn.pack(side="left", padx=6)
        ctk.CTkButton(button_row, text="Reset", fg_color="#2a2a30",
                      command=self._reset).pack(side="left", padx=6)

        ctk.CTkLabel(self, text="Last 7 days (focus minutes)", text_color="#8a8a8a").pack(anchor="w", padx=24, pady=(20, 4))
        self.canvas = ctk.CTkCanvas(self, bg=PANEL, height=160, width=580, highlightthickness=0)
        self.canvas.pack(padx=24, pady=(0, 20))
        self._draw_chart()

        self._tick()

    def _format(self, seconds):
        return f"{seconds // 60:02d}:{seconds % 60:02d}"

    def _toggle(self):
        self.running = not self.running
        self.toggle_btn.configure(text="Pause" if self.running else "Start")

    def _reset(self):
        self.running = False
        self.toggle_btn.configure(text="Start")
        self.mode = "work"
        self.seconds_left = WORK_MINUTES * 60
        self.mode_var.set("Focus session")
        self.time_var.set(self._format(self.seconds_left))

    def _tick(self):
        if self.running:
            self.seconds_left -= 1
            if self.seconds_left <= 0:
                self._switch_mode()
            self.time_var.set(self._format(max(0, self.seconds_left)))
        self.after(1000, self._tick)