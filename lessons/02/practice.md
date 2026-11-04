# Lesson 02 · Git practice
Use files and a terminal for this lesson. Keep this guide open beside your editor/terminal. Work in your own repository, outside the instructor's course-material directory. Commands are explained in [workflow.md](workflow.md); your file starters are in [starter-project](starter-project/README.md). Record predictions and blockers in your own notes, without secrets.

The progression is W5 worked example → G2 guided snapshot → G3 investigation → G6 independent change and delivery. Setup and authentication checkpoints support that progression. No paid account is required. Extensions are optional.

## G1 · Know which tools and account you are using · 15 minutes

**Objective:** Distinguish a commit author label from authentication.

**Already taught:** Lesson 1 terminal/file habits; opening save–commit–push explanation.

Use workflow.md §1 to check Git, set your own author name/email and verify GitHub sign-in. Record the Git version and whether account access works. Do not put passwords or keys in notes. Explain to a partner why configuring an email does not log you into GitHub.

**Expected result:** a working git command and the intended author identity; account access confirmed or a precise blocker recorded. If Git installation takes more than 10 minutes, switch to fallback F1 below while the instructor helps.

**Optional extension:** Before changing anything else, use the read-back commands to confirm what Git will attach to a commit.

## G2 · Keep your first working script · 10 minutes

**Objective:** Make a local snapshot containing a runnable script and enough information to run it.

**Already taught:** W5 demonstration, including README and ignore rules; workflow.md §2 commands.

Create your own python-course repository outside the course-material folder using workflow.md §2. Use the starter-project folder as scaffolding: copy classwork/lesson-02 into your repository, then replace main.py with your working invitation from lesson 1. Do not put classroom work in Homeworks/HW1. If lesson 1 is unfinished, use the already-taught workshop demonstration and identify it as demonstration code in the README.

Write the actual command (from your repository root) and observed output in classwork/lesson-02/README.md. Copy the supplied .gitignore to the repository root, preserving existing rules. Run the script, check status, stage the three intended files, inspect the cached diff and commit. Look at log and the current branch.

**Expected result:** the saved script runs, the README matches it and the first commit contains the intended files. No Python environments, caches or credentials are included. You can point to your commit in log; a commit identifier will differ from your partner's.

**Optional extension:** Explain why GitHub cannot show this commit yet, even if you are signed in.

## G3 · Investigate an incomplete snapshot · 15 minutes

**Objective:** Use both diffs to decide whether a commit would describe one consistent revision.

**Already taught:** G2; status, diff, add, diff --cached, commit and log from W5.

The event now starts at 18:00. Change the time in your script and run it. Read your README: which example is now out of date? Update it too.

Stage only main.py first (use its full path). Before committing, inspect status and both diffs. In your notes predict: if you commit now, which time will the saved snapshot's README show? Is that a useful revision to give a reader?

Complete the selection so the script and README agree, inspect it, then make the second commit with a message describing the real change. Use log and `git show --stat HEAD` to see its files; workflow.md §3 explains this inspection command.

**Expected result:** both files describe 18:00 in the second snapshot. You can explain why an unstaged saved edit would have been left out. Check the work yourself before a partner reviews your prediction.

**Optional extension:** After staging a new temporary wording change, edit that same line again. Compare both diffs to explain the two versions. Restore the previous committed wording in the editor and stage it again; check status is clean. Do not commit an inconsistent experiment.

## G4 · Connect your account safely · 18 minutes

**Objective:** Authenticate with a key and distinguish authentication from author identity.

**Already taught:** GitHub sign-in; local/remote and public/private-key explanation; workflow.md §4.

Follow §4 one step at a time, reusing a working key if you have one. Add only the public key to GitHub, then check SSH authentication. Do not print, photograph, submit or copy the private key into the repository. Verify the host fingerprint with the official reference before accepting a new connection.

**Expected result:** SSH identifies the intended account, or you record the failed step and non-secret error for help. At the 12-minute mark, anyone still blocked continues local G6 work or F2 while the instructor triages. Do not spend the remaining lesson repeatedly generating keys.

**Optional extension:** Explain how the author email and SSH key have different jobs. A successful SSH test does not push any code.

## G5 · Check the copy another person receives · 17 minutes

**Objective:** Distinguish local history from a remote copy and verify a fresh clone.

**Already taught:** G2–G4; local/remote, push, pull and clone explanation; workflow.md §5.

Create the empty GitHub repository and connect origin using §5. Push the commits, then pull. “Already up to date” is a valid result when the two histories already match; it does not mean pull is another push.

Clone into a second folder named python-course-check, read its README and run the script there. Compare its latest commit identifier with the original repository and GitHub. Return to the original folder before continuing.

**Expected result:** the clone's output matches its README and the pushed snapshot; origin names the intended remote. If authentication is blocked, do F2 and keep this remote checkpoint marked incomplete.

**Optional extension:** Without editing, point to the two different local folders. Explain why saving a file in one does not immediately edit the other.

## G6 · Deliver a corrected location · 25 minutes

**Objective:** Independently prepare, inspect and submit one consistent, reproducible revision.

**Already taught:** All preceding checkpoints; README/.gitignore recap and exact-commit demonstration.

New information: the event has moved to Community room. The 18:00 start time and other invitation details stay the same. Work from your original repository.

Without copying a command sequence from a partner, plan which files must change, make the change, run and check it, select a consistent snapshot, commit and send it to GitHub. You may consult the command reference in workflow.md. Open the exact commit page and compare its full identifier with your local history.

In the check clone, pull the new commit and run the file again. Use this copy to verify that the submission includes the updated location and matching instructions. Return to your original repository. Exchange exact commit links with a partner; have them identify the location change from the diff and check that the instructor can access the repository.

**Expected result:** a new location revision, a working clone with the same output, and a link to that fixed snapshot. Your partner should not need to guess which version to review. Corrections after submission use new commits and links. If GitHub is blocked, finish and inspect the local revision, record its SHA and leave remote verification pending; a local SHA alone is not a submitted GitHub link.

**Optional extension:** Write a brief troubleshooting note for someone who runs from the wrong folder, based on the actual working command. Commit and submit a new link if you include it.

## F1 · Git not ready: investigate a supplied snapshot · 10 minutes
This is an illustrative fixture, not a live terminal transcript. Use paper or a text file.

The last commit has a script and README both saying `Start: 17:00`. You save changes to both files so both now say `Start: 18:00`. After staging only the script, status reports:
```text
Changes to be committed:
  modified: classwork/lesson-02/main.py
Changes not staged for commit:
  modified: classwork/lesson-02/README.md
```
Predict the content of each file in a commit made now. Identify the missing selection step. Explain why running the local script cannot prove that the next commit's README is correct. Write the command you would use to inspect the selection. When Git is available, reproduce this state in G3 and compare with your prediction; paper work does not replace the real commit.

**Optional extension:** explain what changes if you save another edit to main.py after staging it.

## F2 · Authentication blocked: local clone and independent work · 10–25 minutes
Finish G3 and the local change/inspection part of G6. To practice cloning without a server, start in the parent of your original python-course folder, using a destination that does not already exist:
```bash
git clone ./python-course python-course-local-check
cd python-course-local-check
git log --oneline
python3 classwork/lesson-02/main.py
```
Windows: use py for Python. Run the README's command and compare output with the original. Return with `cd ../python-course`. This copy's origin is a local path, not GitHub. It demonstrates that committed files can be copied; it does not prove SSH access, push or a remote submission. Record the blocked authentication step for the instructor and complete G4–G5 and G6's remote check with support.

**Optional extension:** make an uncommitted text edit in the original folder and predict whether a new local clone would contain it. Use the editor to restore the wording afterwards. Do not delete a repository to repeat this experiment.
