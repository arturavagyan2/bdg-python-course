## E · Split the workshop desk into a package · 30 min
**Goal:** Refactor a working project into related modules and preserve its behavior.

Use real files in your copy of `practice-project/E/`. Run the working main.py and try Show, Total, an unknown choice and Exit before editing.

Move line_cost and order_total into `workshop/costs.py`. Move show_order into `workshop/display.py`, importing the shared line_cost there. Keep `workshop/__init__.py` empty or comment-only. In main.py, import the needed functions, put the menu and its data inside `main()`, and use a main guard to start it only when run directly. Pass data through parameters.

**Check:** `python3 main.py` still shows `soup 2 6` and `bread 1 2`; Total prints 8; an unknown choice says `Unknown choice`; 0 exits. Importing main or the package modules must not start the menu. With an empty order, Show says `No items` and total is 0. Keep calculation, display and menu responsibilities separate.

Work in steps: costs module (8 min), display/imports (8), guarded main and comparison checks (8), Git (6). Run from the E folder. Then, from your own repository root, inspect and submit the refactoring:
```bash
git status
git add classwork/lesson-12
git diff --cached
git commit -m "Split workshop desk into modules"
git push
```
Use that staging path only if this copy is at classwork/lesson-12; otherwise use your actual classwork path. Submit the exact commit link. Do not upload files through GitHub’s website. If authentication is blocked, keep the local commit and get help with the push.

**Extra (optional):** Import order_total from a separate check.py and calculate a different one-item order.
