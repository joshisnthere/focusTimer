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