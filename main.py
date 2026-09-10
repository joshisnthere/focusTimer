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