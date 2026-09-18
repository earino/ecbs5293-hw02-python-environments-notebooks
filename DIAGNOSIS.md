# Diagnosis notes

**One five-part note per failure you fixed.** This file is laid out with a section for each of
the two failure families. That is the default shape, not a rule — any organisation that gives
every cause its own evidence is fine.

Part 3 must be **raw output you actually ran**, pasted, not a description of it.

**Open this file before you start fixing anything.** Once a repair works, the error that proved
the cause is gone and you cannot get it back without breaking the project again. Paste each
traceback into part 3 the moment you see it; write the rest afterwards.

---

## Note 1 — Environment

1. **What was the symptom?**

2. **What was the actual cause?**

3. **What evidence showed that?**

   This note needs both of these, and you have to say which window each came from:

   - `sys.executable` from `uv run python -c "..."` in the terminal
   - `sys.executable` from a notebook cell

   Then say whether the two paths match, and what that does and does not tell you. Matching
   paths rule out a wrong kernel. They say nothing about what the project *declares* — that
   is a separate question, answered by reading `pyproject.toml`.

   Paste the raw output, plus the traceback lines that started you off:

   ```text

   ```

4. **What did you change?**

5. **How did you verify it worked?**

---

## Note 2 — Notebook state

1. **What was the symptom?**

2. **What was the actual cause?**

3. **What evidence showed that?**

   Paste the raw output, saying which window each line came from — the tracebacks from the
   clean run, and anything you ran to find out what a cell depended on:

   ```text

   ```

4. **What did you change?**

5. **How did you verify it worked?**

   This part carries the **reconciliation**. State both:

   - the script's per-product revenue table and the notebook's per-product revenue, *before*
     the threshold filter, agree to the cent;
   - the products the notebook selects are exactly those above 1,000 in that table.

   Agreement shows the two implementations agree on the numbers. It does not by itself prove
   the shared formula is right — so say what you checked, and no more.
