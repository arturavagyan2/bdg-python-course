# HW1 · Group Trip Budget Calculator

**Assigned after lesson 3; covers lessons 1–3.** Release on Saturday after the required concepts have been taught. Due the following Saturday, one week later; your instructor confirms the clock time and where to send the link. This replaces the unassigned book-swap task. There is one first homework, not two.

**Estimated work:** 45–60 minutes, excluding installation/Git authentication problems. Plan, write, run a sample, investigate the prediction and document/submit. Record an unfinished step if you need help rather than spending the entire time reinstalling tools. No paid account is required.

## The program
A group wants to understand a trip's shared costs. Write a Python script that asks for:
1. Number of travelers.
2. Number of nights.
3. Accommodation cost per night **for the whole group**.
4. Transport cost **for the whole trip and whole group**, entered once.
5. Food budget **per person per day**.

Use these assumptions: trip days = nights + 1; all monetary entries use the same currency; costs split equally. Inputs are valid positive numbers; travelers and nights are positive integers. The accommodation amount is not a per-person rate. Do not multiply the transport total by the number of travelers or days.

Calculate and clearly label:
- Total accommodation cost.
- Total food cost.
- Total trip cost, including accommodation, transport and food.
- Cost per person.

Choose your own wording, layout and meaningful variable names. Use only concepts taught through lesson 3: assignments, int/float conversion, input, arithmetic and ordinary print calls. No conditions, loops, functions, collections, imports, try/except, f-strings, round() or fixed currency formatting are required. Normal float output is accepted. You do not need to handle invalid input or travelers = 0 for this assignment.

## One complete sample
User entries appear after prompts; your wording may differ.
```text
Travelers: 4
Nights: 2
Accommodation per night (whole group): 120
Transport (whole trip, whole group): 80
Food per person per day: 15
Total accommodation: 240.0
Total food: 180.0
Total trip: 500.0
Cost per person: 125.0
```
Check the sample by hand: 2 nights give 3 days; accommodation is 2 × 120 = 240; food is 4 × 3 × 15 = 180; total is 240 + 80 + 180 = 500; split among 4 gives 125. This is a test case, not a finished program. Your program must also calculate from different entries rather than print these sample answers.

## Predict, then check
Before running a second case, write your prediction:

> If the number of travelers doubles while all other inputs stay fixed, which costs change and which stay the same?

Use the sample above, then change only travelers from 4 to 8. Run and record what happened to each of the four displayed costs. Explain any difference from your prediction; a changed prediction backed by a real check is useful evidence. The full answer is not supplied here.

## Files and submission
Use one GitHub repository named **Homeworks**. Your submitted snapshot must contain:
```text
Homeworks/
└── HW1/
    ├── main.py
    └── README.md
```
The course assignment lives in homework/hw-01; that name is not your submission-folder name. Copy `starter/HW1` into the root of your own Homeworks repository and complete it. Keep your lesson-2 classroom repository separate. If a root .gitignore is useful, merge the supplied starter rules without removing your existing rules; it is not an extra graded file.

In HW1/README.md include the verified root run command, one example run, your prediction and observed second-run result, and any AI assistance used (or “No AI assistance used”). Explain what you checked yourself. You may also note approximate work time and blockers for support.

Run from the Homeworks repository root with `python3 HW1/main.py` (Windows usually `py HW1/main.py`). Save, run and inspect your work. Commit meaningful changes and push, then submit the **exact final commit URL**, such as `https://github.com/USERNAME/Homeworks/commit/FULL_SHA`. Compare with `git log -1 --format=%H` and check instructor access. No arbitrary number of commits is required. A repository homepage is not a fixed submission. Corrections use a new commit and a new link.

See [submission.md](submission.md) for the exact repository-specific workflow. Do not upload environments, keys or credentials. If remote access is blocked, keep your working files and record the exact non-secret failing step; ask for support and supply the missing remote evidence later.

## Assessment · 10 points
| Evidence | Points |
|---|---:|
| Inputs use appropriate numeric types and all four calculations are correct for different valid entries | 5 |
| Names, labelled output and straight-line code are understandable | 2 |
| README reproduces a run, explains prediction versus observation and discloses AI assistance | 2 |
| Required folder/files and an accessible exact commit link identify the work | 1 |

Optional work is not needed for full marks. No points depend on untaught syntax, polished prose or two-decimal formatting.

**Optional extension:** ask for a souvenir budget per person and include it in total cost and cost per person. Keep all other assumptions. Explain what you tested after the change.
