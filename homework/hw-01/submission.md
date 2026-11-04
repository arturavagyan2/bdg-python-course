# HW1 · Submit a fixed version
Use the existing lesson-2 Git/SSH setup; this guide changes the destination to **Homeworks**, not the classroom python-course repository.

1. On GitHub create an empty repository named Homeworks, with visibility/instructor access that permits review. If you already have it, use your existing local copy and inspect its status/remote rather than initializing or adding origin again.
2. For a new local folder, create Homeworks outside the course materials. From that folder run `git init -b main`. Copy the course's starter/HW1 here and work in HW1/main.py and HW1/README.md. Use your own already-configured Git identity. On Windows use Git Bash for these Git commands.
3. From the Homeworks root, after saving and running:
```bash
python3 HW1/main.py
git status
git add HW1/main.py HW1/README.md
git commit -m "Add group trip budget calculator"
```
Use a meaningful message describing your actual change; no commit-count quota applies. On Windows replace python3 with your verified py command. Inspect selected files before committing.

For a new local repository connected to a new empty GitHub repository, replace USERNAME with your account:
```bash
git remote add origin git@github.com:USERNAME/Homeworks.git
git remote -v
git push -u origin main
```
If origin already exists, inspect it; do not add a duplicate. Existing configured copies normally use `git push`. If rejected, ask for help instead of force-pushing. SSH keys/authentication steps remain in lessons/02/workflow.md in the course materials; never copy private keys into this repository.

Finally run `git log -1 --format=%H`. Open that commit's page on GitHub; match the full SHA and confirm instructor access. Submit its exact /Homeworks/commit/FULL_SHA URL using the channel announced by your instructor. Later corrections use new commits/links. Account problems remain support issues: keep local work and report the exact non-secret blocker.
