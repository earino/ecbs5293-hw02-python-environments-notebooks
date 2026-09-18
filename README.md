# Homework 2 — Python execution, environments, notebooks, and Git checkpoints

**ECBS5293 — Computing for Analytical Work · due the Friday after Session 2, 23:59 (slot on Moodle)**

Budget about 6–7 hours. If you are well past that and still stuck, post on the Moodle forum. That tells us something useful about the assignment, and it is not a mark against you.

## Goal

Two entry points that should both work from a fresh clone:

1. `scripts/report.py` — prints a table of revenue per product.
2. `notebooks/report.ipynb` — lists the *significant* products and writes `output/significant.csv`.

**The policy the notebook must implement:** a product is significant when its 2024 revenue, summed after dropping rows with missing `units`, is **strictly greater than 1,000**. That is the whole specification; nothing else in the repo states it.

## How to get it

In your terminal (Git Bash on Windows, Terminal on macOS), in the folder where you keep course work:

```bash
git clone https://github.com/earino/ecbs5293-hw02-python-environments-notebooks.git
cd ecbs5293-hw02-python-environments-notebooks
```

Commands below run in that terminal, from this folder, unless they say *in a notebook cell*. Open **this folder** in VS Code (*File → Open Folder…*; trust the authors when asked, or the kernel picker lists nothing) to edit files and to run the notebook.

## Start here

In the terminal, from the project folder — the launch you have used since Lab 1:

```bash
uv sync
uv run python scripts/report.py
```

For the notebook: open **this folder** in VS Code, open `notebooks/report.ipynb`, select the `.venv` kernel, then *Restart*, then *Run All*. There is no combined toolbar button — use the Command Palette entry, or Restart followed by Run All. Run All on its own keeps the kernel's memory and proves nothing.

Both entry points fail. That is the assignment.

## What is broken

The setup instructions this project shipped with describe tools it does not use:

```bash
conda activate ds1
pip install pandas
python scripts/report.py
```

**You do not need to run those** — they are what you are correcting, quoted here as an exhibit. Depending on what is installed on your laptop they will give you a different error, or no error at all, and none of them tells you what is actually wrong with the project.

Expect two kinds of failure, **environment** and **notebook state**, and diagnose each with its own evidence. The saved outputs in the notebook are not evidence of anything.

## The order of work

The list below is what you hand in. This is the order to do it in.

**Open `DIAGNOSIS.md` before step 1.** Part 3 of each note has to be filled in while the project is still broken: a repair that works destroys the error that proves it, and you cannot get it back without breaking the project again.

1. `uv sync`, then `uv run python scripts/report.py`. **Paste that traceback into `DIAGNOSIS.md`, Note 1 part 3, before you change anything.**
2. Fix the environment **in the project** — `pyproject.toml`, not your laptop. Re-run the script until it prints the table.
3. Commit. That is repair checkpoint one. The notebook is still broken at this point; that is expected.
4. Open the notebook on the `.venv` kernel. *Restart*, then *Run All*. **Paste that first traceback into Note 2 part 3 before you change a single cell.** Reordering surfaces a *second* error — paste that one too, for the same reason.
5. Fix the notebook. Restart-and-Run-All again, until it runs top to bottom and writes the CSV.
6. **The reconciliation**: check the notebook's per-product numbers against the script's table, and the selection against the policy under *Goal*.
7. Commit. Repair checkpoint two. `git status` should now say *nothing to commit, working tree clean*.
8. Do the recovery exercise (below) and write `RECOVERY.md`.
9. Finish the notes: complete `DIAGNOSIS.md` — the raw evidence is already pasted in, so this is parts 1, 2, 4 and 5 — write `AI_USE.md`, and rewrite this README's *Start here* and *What is broken* sections. Commit.
10. Follow `SUBMITTING.md` — commit everything, save the git log, make the zip. Record the video. Upload both to Moodle.

Steps 8 to 10 come last on purpose: the recovery exercise needs something committed to recover *to*, and the archive contains only what you have committed.

## What you must submit (all on Moodle)

In the repo, committed:

1. The repaired project: `uv sync && uv run python scripts/report.py` prints the table; the notebook passes Restart-and-Run-All and writes the CSV.
2. **`pyproject.toml`** declaring everything the code needs — the fix lives in the project, not on your laptop.
3. **`README.md`** with correct, minimal setup and run instructions (`uv` only) — replace the *Start here* and *What is broken* sections with what actually works. Leave `SUBMITTING.md` alone; it is not yours to rewrite.
4. **At least two meaningful commits** with messages that say what they fixed (one after the environment fix, one after the notebook fix). The starter's own commit and the *Add git log* commit below do not count; the two are your repair checkpoints, and the first may well contain a still-broken notebook — it records the environment fix. `git status` after your last commit should say *nothing to commit, working tree clean*; an empty `git diff` alone is not that check.
5. **`DIAGNOSIS.md`** — a five-part note per failure you fixed. The file is already laid out with a section for each, and each part says what evidence it needs. Any organisation that gives every cause its own evidence is fine.
6. **`RECOVERY.md`** — the Git recovery exercise (below).
7. **`AI_USE.md`**.

### The recovery exercise

You practised this at the end of Lab 4. Once everything works and is committed: **break it on purpose**. Delete half the cells of the notebook, or overwrite `scripts/report.py` with a single line. Save it; do **not** `git add` it (`git restore <file>` undoes saved edits that are not staged; the reset section below has the longer command for staged ones). Now get the working version back **without re-downloading anything**, using Git alone — `git status` to see what changed, `git restore <file>` to bring back the committed version (that is the one you practised; `git log` then `git checkout <commit> -- <file>` reaches an *older* commit, and you do not need it here). Then prove it: run the script / Restart-and-Run-All. Write in `RECOVERY.md`: what you broke, the exact commands that brought it back, and what you ran to confirm. This is the skill the syllabus promises — recover a broken working tree without re-cloning — and it is why you commit *before* you experiment.

Then make the archive. The commands are in **`SUBMITTING.md`**, in this folder — four short steps, each with a sentence on what it does. They live in their own file so that rewriting `README.md` cannot delete the instructions you need at the very end.

Read the first step before you start: `git archive` packs **exactly what you have committed**, so anything still uncommitted is silently missing from your zip.

Upload to the Homework 2 slot on **Moodle**:

8. `hw2-submission.zip` (in the folder above the project)
9. A **60–90 second video** showing Restart Kernel and Run All succeeding on a fresh kernel, then explaining what was broken in the setup and in the notebook, what you changed, and how you verified. Start by saying "Homework 2" and the repo name.

## Rules

- Open the notebook with the project's `.venv` kernel selected in VS Code, and verify it with `import sys; print(sys.executable)` in a cell. A global or Anaconda kernel is one possible cause of an import failure; a kernel inside `.venv/` that still cannot import something points at what the project declares.
- `.gitignore` already keeps `.venv/`, `output/` and notebook checkpoint files out of the repo. Do not force them back in with `git add -f`.
- AI may explain; you must be able to explain, on video, without notes.

## Hints, if stuck

1. `ls` — no `requirements.txt`, no `environment.yml`. What declares dependencies here? What tool reads it?
2. The traceback names the module. Now find out *which* Python went looking for it: run `import sys; print(sys.executable)` under `uv run` and again in a notebook cell. Two different paths means a kernel problem. The **same** path twice means the Python is right and the project is not declaring what the code imports — so compare the `import` lines at the top of each file against `pyproject.toml`.
3. In the notebook, a clean run raises `NameError`. First ask whether that name is defined *lower down the page* — if so, the cells are in the wrong order. Once the order is right, a name that is defined **nowhere** means the cell was deleted, and you have to write it, from the policy stated under *Goal*.

## Grading

See the rubric on the course site.

## If you got lost: how to reset

Both of these **destroy work**. Read before running.

**Discard uncommitted changes (destructive)** — throw away edits and new files; keep your commits:

```bash
git restore --staged --worktree .    # every tracked file back to the last commit, staged or not
git clean -fd                        # and remove new, untracked files
```

> ⚠️ Permanently deletes uncommitted changes — staged or not — and any new untracked files.

**Full reset to the starter state (destructive)** — back to exactly what you cloned; throws away your commits too:

```bash
git reset --hard origin/main
git clean -fdx
```

> ⚠️ Discards your local commits and uncommitted changes. The `-x` also removes ignored files — `output/`, the `.venv/` environment — so the folder truly matches a fresh clone (`uv sync` rebuilds the environment in a minute). Without `-x`, leftover generated files can hide the very failure the lab wants you to meet again.
