"""
Local storage for completed focus sessions, plus a helper to roll them up
into per-day totals for the chart. Stored as JSON next to this file.
"""

import datetime
import json
import os

LOG_PATH = os.path.join(os.path.dirname(__file__), "sessions.json")


def _load():
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH) as f:
            return json.load(f)
    return []