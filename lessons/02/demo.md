# W5 · What does a commit actually record? · 10 minutes
Use a disposable repository. Git stores a project's history on your computer. GitHub hosts a remote copy that another person can access. A repository contains your files and Git's history in a hidden .git folder; do not edit that folder yourself.

A **working tree** is the files you are editing. The **staging area** holds the version of each change selected for the next commit. A **commit** is a recorded snapshot, with an author, message and identifier. Staging lets us inspect whether a script and its instructions belong together before recording them.

Prepare main.py with `print("Museum opens at 10")` and README.md with a run command and the expected line `Museum opens at 10`. Explain that a README is plain text for a person, not Python code. Use your own configured demo identity.

```bash
git init -b main
git status
git add main.py README.md
git diff --cached
git commit -m "Add museum opening notice"
```
Reason through each command: init starts history; status reports file states; add selects saved content; the cached diff previews that selection; commit records it locally. The first commit includes both files, so another reader can run this snapshot.

Change 10 to 11 in both files and save. **Predict:** which files will the next commit include if we stage only main.py?
```bash
git diff
git add main.py
git status
git diff --cached
```
The normal diff shows changes not yet staged; after add, main.py's change appears in the cached diff instead. README.md's change is still unstaged. A commit now would have the new script but the old run example. Git does not know they should match. Finish the selected change:
```bash
git add README.md
git diff --cached
git commit -m "Move museum opening to 11"
git log --oneline
git branch --show-current
```
Run `git show --stat HEAD` to list the files changed by the latest commit; HEAD names your current commit. `git show HEAD` shows its full changes. Both changes are now recorded. log lists commits, newest first; each short identifier names a snapshot. A branch is a movable name pointing to a commit. main now points to the new commit, not to a second copy of your files. We inspect that name today; branch creation, PRs and conflicts return in lesson 21.

**Guided reasoning:** ask what happens if we save another edit after add. It is saved on disk but is not automatically included in the staged version. Use status and both diffs to locate it; add again if that edit belongs in the intended snapshot. Do not introduce reset or history rewriting.

**Application:** G2 records the learner's first script. G3 asks the learner to find and fix a mismatch between a script, its documentation and the selected changes. G6 changes the location independently and verifies the remote snapshot.

Before G2, show the starter .gitignore: .venv/ and venv/ are local environments, __pycache__/ contains generated Python cache, .env and key patterns exclude common secret files. These names are preparation only; we do not create environments or secrets today. Ignore rules reduce accidental additions of untracked files; they do not remove tracked files or guarantee all secrets are excluded.
