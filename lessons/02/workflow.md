# Lesson 02 · Git workflow
Use these commands with your instructor, one checkpoint at a time. Replace `USERNAME`, `YOUR_NAME` and the email placeholder with your own values. Do not change another person's Git identity.

## 1 · Installation and identity
Ubuntu: `sudo apt install git`. Windows: install [Git for Windows](https://git-scm.com/download/win), then use Git Bash for the filesystem and SSH commands below.
```bash
git --version
git config --global user.name "YOUR_NAME"
git config --global user.email "YOUR_EMAIL"
git config --global --get user.name
git config --global --get user.email
```
Find your privacy/noreply address in GitHub Settings → Emails. Create a GitHub account and verify sign-in before practice. Git identity labels a commit's author; it is separate from authentication.

## Command reading guide
`cd` changes the current folder; `mkdir` creates one. `mkdir -p classwork/lesson-02` creates the nested classroom folders in Ubuntu or Git Bash; you can create the same folders in the editor instead. A slash separates folders in a path. Replace placeholders; do not type the prompt symbols shown by your terminal.

| Command | Question it answers / action |
|---|---|
| git status | What is new, changed or staged here? |
| git diff | What saved changes have not been staged? |
| git add PATH | Select the current saved content at this path for the next snapshot. |
| git diff --cached | What changes would the next commit record? |
| git commit -m "message" | Record the staged snapshot locally, with a reason. |
| git log --oneline | Which commits exist in this local history? |

Saving does not stage a file. Staging does not commit it. Committing does not send it to GitHub. An empty normal diff can mean changes are staged; check status and the cached diff before concluding nothing changed.

## 2 · Local repository and first commit
Create your solution repository outside the instructor's course-material directory. If `python-course` already exists, do not initialize blindly; check `git status` and ask for help.
```bash
mkdir python-course
cd python-course
git init -b main
mkdir -p classwork/lesson-02
```
Create `classwork/lesson-02/main.py` in your editor by copying your working lesson-1 invitation. If unfinished, use the taught workshop demonstration and say so in the README. Create `classwork/lesson-02/README.md` with the real run command and output, and copy the root `.gitignore` from starter-project, preserving any existing rules.
```bash
python3 classwork/lesson-02/main.py
git status
git add classwork/lesson-02/main.py classwork/lesson-02/README.md .gitignore
git diff --cached
git commit -m "Add first Python script"
git log --oneline
git branch --show-current
```
Windows: replace `python3` with `py`. Working tree means your current files; staging means the changes selected for the next snapshot; a commit records that snapshot. A branch is a movable name pointing to a commit. We use `main` now; branch creation, PRs and conflict practice return in lesson 21.

## 3 · A change and a second commit
For G3, change the start time to 18:00, run the script, and update the README's expected output to match. In the investigation, stage main.py alone first; predict the next snapshot and then select the missing README change. The sequence below shows the complete selection:
```bash
git diff
git add classwork/lesson-02/main.py classwork/lesson-02/README.md
git diff --cached
git commit -m "Clarify script and run instructions"
git log --oneline
git show --stat HEAD
```
`git show --stat HEAD` lists files changed by the latest commit; HEAD names your current commit. To inspect its full changes, use `git show HEAD`. The two diffs preview uncommitted changes; show inspects a recorded commit.

Before add, the change is unstaged. The cached diff shows what the next commit will record. Later corrections should be new commits.

## 4 · SSH authentication
Reuse an existing working SSH key where possible. List existing public-key filenames with `ls ~/.ssh/*.pub`. If a new key is needed, follow the [official GitHub guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). For example:
```bash
ssh-keygen -t ed25519 -C "YOUR_GITHUB_NOREPLY_EMAIL" -f ~/.ssh/bdg_course_ed25519
```
If that filename already exists, do not overwrite it. Use the existing key or choose a new filename. Set a passphrase. In Ubuntu or Git Bash:
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/bdg_course_ed25519
cat ~/.ssh/bdg_course_ed25519.pub
```
Use `ssh-add -l` to list the keys loaded in the agent when diagnosing a key problem.

Add only the `.pub` content to GitHub Settings → SSH and GPG keys → New SSH key. The private key has no `.pub` suffix. Never display it or place it in a repository.
Before accepting a first connection, compare its fingerprint against [GitHub's official fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints). Do not accept a mismatch.
```bash
ssh -T git@github.com
```
A successful response confirms authentication but says shell access is unavailable; this test can return exit code 1. For Permission denied, check the agent, public key and correct account. Do not copy a private key to fix authentication.

## 5 · Remote repository
On GitHub, create an empty `python-course` repository, without an automatically generated README, .gitignore or license. Choose visibility that lets the instructor view your submission. Do not embed credentials in URLs.
```bash
git remote add origin git@github.com:USERNAME/python-course.git
git remote -v
git push -u origin main
git pull --ff-only
```
A remote is a named address of another repository; origin is the conventional name for this connection. Here that address is on GitHub. Push sends commits; pull fetches and integrates changes. If origin already exists, inspect `git remote -v` instead of adding it again. If push is rejected, ask for help; do not force-push.
Clone creates a new local copy. From the parent directory, use a different destination name:
```bash
cd ..
git clone git@github.com:USERNAME/python-course.git python-course-check
cd python-course-check
git log --oneline
python3 classwork/lesson-02/main.py
```
On Windows use `py` for the last command. Return to your working repository with `cd ../python-course`. If authentication cannot be resolved during class, finish local commits and use fallback F2 in practice.md, record the blocker and get support. The remote submission is still incomplete.

## 6 · Exact commit link
```bash
git log -1 --format=%H
```
On GitHub, open the repository's commit history and open your latest submission commit. Submit the real URL in the form `https://github.com/USERNAME/python-course/commit/FULL_SHA`. Check that its SHA matches your terminal and the instructor has access. A repository home-page URL does not identify a fixed snapshot. Corrections use new commits and new links; preserve the previous submission.

Read assignments from the instructor’s course repository. Keep classroom practice in your python-course repository. HW1 is first assigned after lesson03; use a separate repository named Homeworks containing HW1/main.py and HW1/README.md. Read [the HW1 brief](../../homework/hw-01/assignment.md) and [submission workflow](../../homework/hw-01/submission.md) for the run/example/prediction/AI-disclosure requirements and exact commit URL. Later homework folders will be announced with their briefs; do not create21 empty assignments.
