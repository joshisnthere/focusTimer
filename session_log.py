"""
Local storage for completed focus sessions, plus a helper to roll them up
into per-day totals for the chart. Stored as JSON next to this file.
"""

import datetime
import json
import os