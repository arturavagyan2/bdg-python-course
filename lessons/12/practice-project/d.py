# ## D · Make a small session card with standard tools · 10 min
# **Goal:** Use random, datetime, os and pathlib without installing packages.
# 
# Complete a session card for the supplied names and date. Choose one helper with random.choice. Set follow_up to seven days after start using timedelta. Set folder to the last part of the current working directory using `Path(os.getcwd()).name`.
# 
# Write `session_card(names, start)` returning a dictionary with `helper`, `follow_up` (converted to text) and `folder`. names is non-empty. Keep printing outside. The imports and input data are supplied. No files should be created or changed.
# 
# **Check:** Follow-up is `2026-12-05`. The helper must be one of the supplied names; any of them is a correct random result. Folder must describe your actual working directory, so it may differ between laptops. A path object describes a location; it does not open a file.
# 
# **Extra (optional):** Use a start date near the end of December and check the year transition.

import random
from datetime import date, timedelta
import os
from pathlib import Path

names = ["Ali", "Bo", "Nora"]
start = date(2026, 11, 28)
# Define session_card, then print one returned record.
