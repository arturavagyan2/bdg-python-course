## C · Protect startup code with a main guard · 14 min
**Goal:** Keep a module reusable without starting its demonstration on import.

Use real files in `practice-project/C/`. Run `python3 main.py`, then `python3 preview.py`. Predict why preview currently prints two messages.

Keep `build_message(label)` reusable. Move the desk demonstration into `run_demo()` and call it only under `if __name__ == "__main__":`. Keep preview.py’s explicit call unchanged.

**Check:** Running main.py prints `Ready: desk`. Running preview.py prints only `Ready: preview`. Importing main defines its functions without printing anything or asking for input. The file is named main.py, while its direct-execution name is the special string __main__.

**Extra (optional):** Make a third small caller that imports build_message and prints a message for "check".
