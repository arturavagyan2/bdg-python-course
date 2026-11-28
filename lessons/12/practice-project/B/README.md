## B · Move one function into a module · 14 min
**Goal:** Create a custom module and use both import styles.

Use real files in your copy of `practice-project/B/`. Run `python3 main.py` before editing: it prints 6.

Move the `line_cost` definition into costs.py. In main.py, use `import costs` and call the function through that module. In check.py, use `from costs import line_cost` and print a call for price 5 and quantity 0. Keep printing out of costs.py.

From the B folder run `python3 main.py`, then `python3 check.py`.

**Check:** Outputs are 6 and 0. The definition exists once, in costs.py. Running the module file itself should display nothing. Use the same interpreter for both files. A notebook cell does not save costs.py.

**Extra (optional):** Change check.py to test quantity 2 as well.
