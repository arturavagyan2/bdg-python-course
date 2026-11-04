# Lesson 01 · Set up and run Python
Goal: Python 3.12+ and one working editor. Follow these steps with your instructor. Complete setup before independent practice where possible.

## What the tools do
The editor changes a text file. Python runs the saved instructions in that file. The terminal accepts commands, such as the command that starts Python. The Python extension helps VS Code find and run Python; installing that extension alone does not install Python.

A file path says where a file lives. The terminal starts from a current folder; paths below are relative to the course root unless stated otherwise. Do not type prompt characters such as `$` or `>>>` into a command. The `python3 --version` command asks the installed program its version; it does not run your script. PATH is the list of folders searched when you type a program name. `command -v python3` shows which program that search found on Ubuntu.

## Ubuntu
In a terminal:
```bash
python3 --version
command -v python3
```
If Python is missing:
```bash
sudo apt update
sudo apt install python3
python3 --version
```
If the version is below 3.12, ask the instructor to prepare a compatible classroom environment. Do not replace the system Python with an unverified download.
Install VS Code using its [official Linux guide](https://code.visualstudio.com/docs/setup/linux), or use an existing PyCharm installation. In VS Code, install the Microsoft Python extension. Choose Open Folder and open the course directory. Increase the editor and terminal font size until you can read them comfortably; keep the file and terminal visible together. Use Ctrl+Shift+P → Python: Select Interpreter and select the interpreter you checked in the terminal. Choose Terminal → New Terminal.

## Windows
Install Python 3.12+ from the [official Python site](https://www.python.org/downloads/windows/), following the installer instructions. Reopen your terminal and check:
```powershell
py --version
```
If `py` is unavailable, try `python --version` and record the command that works. PATH is the list of directories the terminal searches for commands. If a command is not found, check the installation and PATH, then open a new terminal.
Select the same interpreter in VS Code. In PyCharm, use Settings → Project → Python Interpreter, then the script's Run command.

## Run the same file in two ways
Save `lessons/01/demo/hello.py`. In VS Code choose **Run Python File in Terminal**. Then, from the course root:
```bash
python3 lessons/01/demo/hello.py
```
On Windows use `py lessons/01/demo/hello.py`. Both runs should print `Hello, World!`. The interpreter reads and executes the saved `.py` instructions.

| What you see | What to check |
|---|---|
| `>>>` instead of a normal terminal prompt | You are inside interactive Python. Enter `exit()`, then run the terminal command. |
| File not found | Check your current directory, filename and `.py` extension. |
| Old output | Save the edited file and run it again. |
| Different editor and terminal behavior | Check that both use the intended interpreter and file. |
| SyntaxError after copying | Check straight quotation marks and matching parentheses. |

## Notebook: prepared environment or script fallback
The instructor prepares Jupyter using the root README commands. Open `teaching.ipynb`, select a Python 3 kernel and use Shift+Enter. Change a message and run its cell again. An old output remains until you rerun the cell.
If setup takes more than five minutes, use `demo/notebook-demo.py` for the same run/edit/rerun demonstration and use the practice project. Formal environment and package-management instruction remains lesson 13.

References: [VS Code Python](https://code.visualstudio.com/docs/languages/python/), [running Python](https://code.visualstudio.com/docs/python/run), [Python on Unix](https://docs.python.org/3.12/using/unix.html). Source review: 15 October 2026. Installation is not performed automatically by these materials.

## If setup is blocking practice
After the instructor's setup timebox, switch to a prepared classroom computer or pair with a learner whose Python works. Be the driver: type, save and run your own changes on that machine; keep a separate folder with your name. Use the script route if only Jupyter is blocked. If no runtime is available, predict the output on paper, mark the punctuation error and explain the intended fix. These are useful interim tasks but do not count as a verified run. Keep your files and a note of the exact command/error for a support session. Do not spend the entire practice block reinstalling.

If ready early, run hello.py from both routes, deliberately edit without saving and explain what the terminal runs; then save and rerun. Check the interpreter path and write the actual command you used so a partner can repeat it. No additional packages are needed for these scripts.
