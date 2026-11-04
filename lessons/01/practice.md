# Lesson 01 · Student practice
Use **one** route: the notebook or the matching script project. The tasks and objectives are the same; do not complete both sets. Work individually before comparing with a partner. Hints are available from the instructor; you do not need to guess new syntax.

In a notebook, edit a code cell and press Shift+Enter to run it. An earlier output stays visible until you rerun. In a script, edit, save, then run the file. Lines beginning with # are comments for the reader; Python ignores them. Put predictions and observations in the “My notes” cells or in notes.md. Do not paste terminal commands into Python code.

The instructor demonstrates W1 before A, W2 before B, and W3 before C. D1 happens in the AI discussion; D2 follows it. Finish with independent task E. Times include checking your result. Extensions are optional, not extra requirements.
## A · An invitation a visitor can use · 10 minutes

**Learning objective:** Turn a short request into readable output, without copying the demonstration.

**Already taught:** Save/run a file; print(), quoted text, parentheses and line order; worked example W1.

The reading club meets at the Library hall at 17:00. Visitors should bring a book. Make a small script that prints an invitation containing those facts. Choose labels and an order that help someone decide where to go and what to bring. There is no required number of print calls.

Start with the empty coding area. Write the output you intend in your notes first, then turn it into Python. Save and run it. For the script route, run the same saved file from both the editor and terminal. Notebook users also save their code as invitation.py in the practice-project folder and run that file in both ways.

**Expected behavior:** a reader can identify the event, location, time and what to bring; both file runs agree. Python should not ask the visitor any questions. Ask a partner to find each fact using only the output.

**Optional extension:** Change the meeting time. Before running, identify exactly which line should change and which output should stay the same.

## B · Text that looks like a calculation · 8 minutes

**Learning objective:** Distinguish showing written text from asking Python to add numbers.

**Already taught:** W2: quoted text is printed literally; unquoted whole numbers joined by + are added.

Read the two starter lines without running them. Predict each output in your notes and explain whether Python will add anything. Run the code and compare it with your prediction.

There are now five people in the first group and three in the second. Change the program so the first line shows the new written calculation and the second line calculates its total. Do not type a precomputed total into the second print call.

**Expected behavior:** the first line still contains a plus sign; the second is a number. Both refer to the new group sizes. Explain what the quotation marks changed.

**Optional extension:** Can you make the two lines disagree by changing only one character? Predict the disagreement, run it, then restore a consistent version.

## C · It crashes — and then it is still wrong · 12 minutes

**Learning objective:** Repair a syntax error and separately check whether successful output contains the right information.

**Already taught:** W3: read the final error message, match quotes/parentheses, save and rerun. # begins a comment for humans.

The lost-property desk actually closes at 18:00. The starter has both a Python-writing mistake and an out-of-date closing time.

1. Run the starter as supplied. Record the final error type and the line Python points to. A traceback is diagnostic information, not your intended output.
2. Repair only the writing mistake first. Run again. Does the output now meet the desk’s request?
3. Update the closing time and run again. Record why a successful run alone was not enough.
4. Save a working copy. Deliberately remove one quotation mark, predict what will happen, and run once. Restore it and rerun successfully before finishing.

**Expected behavior:** the final saved file runs without an error and clearly gives the correct desk and closing time. Your notes distinguish the punctuation repair from the information correction. Exact error wording may vary by Python version.

**Optional extension:** Swap the two complete print lines. Predict and check the output order. Choose the order you find easier to read and explain why.

## D · Check a claim, not a confident tone · 14 minutes

**Learning objective:** Distinguish a written rule from learned behavior and use direct evidence to check a claim about Python.

**Already taught:** AI discussion; W2 text versus numbers; running the exact code in question.

**D1 · Discuss/investigate · 4 minutes during the AI discussion.** A written rule flags every message containing the word “free”. Consider (a) a genuine hotel confirmation saying “Free parking with your booking”, and (b) a scam saying “Claim your cash prize”. For each, state what the rule does and why that helps or fails. Suggest one useful labelled training example for a learned spam filter. Can you know a trained model’s answer without testing that model?

**D2 · Verify · 10 minutes.** This is an invented, deliberately questionable AI-style response, not a real model transcript:

> “`print("7 + 2")` prints the number 9. Python always calculates sums inside print.”

Before running anything, write whether you agree and why. Type the exact claimed code into the coding area and run it. Record the code, observed output and your decision about the claim. Then remove only the quotation marks, predict the effect and run again. Explain why this second run does not prove the original claim correct.

**Expected behavior:** your notes separate the claim from two observations and use those observations to justify a decision. The supplied statement may be wrong; do not change code merely to make the statement appear right. No AI account or paid service is needed.

**Optional extension:** Write a misleading claim about a different print example and ask a partner to propose a check. Label your claim synthetic; record which exact code would test it.

## E · A useful sign for the quiet room · 18 minutes

**Learning objective:** Combine literal information with a calculated quantity in an independently planned script.

**Already taught:** Tasks A–D: print(), quoted text, simple +, output order, save/run/check. No variables or input needed.

A librarian wants a sign for the quiet room. Quiet reading starts at 16:00 in Room 2. There are six chairs near the windows and four by the door. Visitors need the total seating capacity, not a list of where the chairs stand.

Plan an output that answers: Where is quiet reading? When does it start? How many seats are there altogether? Write the script from the empty coding area. Ask Python to calculate the capacity from the two counts. Put a clear label beside or on the line before the calculated result, using only the print syntax already taught.

Save and run; compare the output with each fact in the request. Ask a partner to read the output without the instructions. Then the librarian adds two chairs by the door: change the relevant count, predict what should change, and rerun. Leave the final version describing the updated room.

**Expected behavior:** the final output gives the location, starting time and correctly labelled updated capacity. It still calculates from the two counts. The time and location stay unchanged. No fixed layout or print quota is required. This is a static sign: it does not count people entering the room.

**Optional extension:** The librarian changes the time too. Make the change and describe which facts must be checked again. Explain why this script cannot report how many seats are free right now.

For executable starters, open [practice.ipynb](practice.ipynb) or [the script project](practice-project/README.md).
