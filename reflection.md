# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

### Bug 1 — New Game Does Not Reset Game State

**Expected behavior:**
Clicking "New Game" should reset the entire game state including attempts, score, history, and the secret number.

**Actual behavior:**
After clicking "New Game", the previous game state remained visible. The history, score, and previous attempts were still present instead of resetting.

**AI Prompt Used in Copilot:**
Look at #file:app.py.
When the "New Game" button is clicked the game state does not fully reset.
Explain how Streamlit session_state might cause old values to persist between runs.

---

### Bug 2 — Hint Logic Appears Reversed

**Expected behavior:**
If the secret number is higher than my guess, the game should tell the player to go higher.

**Actual behavior:**
When the secret number was 74 and I guessed values like 70, 40, and 10, the game repeatedly displayed "Go LOWER!", which is incorrect because those guesses are below the secret number.

**AI Prompt Used in Copilot:**
Look at #file:app.py and #file:logic_utils.py.
When the secret number is 74 and I guess 70 or 40, the game tells me "Go LOWER!"
Explain step-by-step which part of the code could cause this reversed hint logic.

---

### Bug 3 — Difficulty Range Does Not Match Game Instructions

**Expected behavior:**
When selecting Easy difficulty, the range should match the displayed settings and all game logic should use that same range.

**Actual behavior:**
In Easy mode, the sidebar displayed a range of 1 to 20, but the main game prompt still said "Guess a number between 1 and 100." In addition, the secret number generated was 49, which should not be possible in Easy mode.

**AI Prompt Used in Copilot:**
Look at #file:app.py and #file:logic_utils.py.
Easy difficulty says the range is 1 to 20 but the game still uses 1 to 100.
Explain how the difficulty settings might not be correctly connected to the secret number generation.

---

## 2. How did you use AI as a teammate?

**AI tools used:** VS Code Copilot (Inline Chat and Agent Mode), and manual testing.

**Example of correct AI suggestion:**
When I asked Copilot to "Find where guess parsing and validation happen" in Agent Mode, it identified that `parse_guess()` only checked if input was a number, not the range. Before implementing the `validate_guess()` function, I reviewed the function signature and tested boundary cases (guessing 100, 101, 1, 0) to confirm my logic was correct. I specifically made sure the range check compared `guess < low or guess > high` and wrote the test `test_validate_guess_out_of_range_high()` to verify 101 was rejected in a 1–100 range.

**Example of misleading AI suggestion:**
Copilot initially suggested converting decimals like 97.7 to 97 automatically. I tested this approach with inputs like "97.7" and "10.5" in the running app, and realized it silently accepted invalid input without user feedback. I rejected this suggestion because the game should only accept whole numbers. Instead, I modified `parse_guess()` to check for the "." character and return an error message "That is not a whole number." I verified this worked by manually entering "97.7" and seeing the error message appear immediately without consuming an attempt.

---

## 3. Debugging and testing your fixes

**How I decided a bug was really fixed:**
I tested fixes by replicating the original bug behavior, then confirming the error no longer occurred. For example, I tried entering 101 in Normal mode—originally it consumed an attempt; after the fix, it shows "Please guess between 1 and 100." with no game state change.

**Test example using pytest:**
I wrote `test_validate_guess_out_of_range_high()` which calls `validate_guess(101, 1, 100)` and asserts it returns `(False, "Please guess between 1 and 100.")`. Running `python3 -m pytest` confirmed this test passes, ensuring the range validation works correctly. I also manually tested edge cases: guessing 100 (valid), then 101 (invalid), to confirm the boundary is correct.

**AI help with testing:**
Copilot suggested the basic pytest structure, but I reviewed each test to match the actual function signatures. For `test_validate_guess_out_of_range_high()`, I confirmed the function returns a tuple `(bool, str)`, then wrote assertions for both the `ok` flag and the error message. I ran the test while the bug still existed (it failed), implemented the fix, then ran it again to confirm it passed. This "fail first" approach gave me confidence the test was actually catching the real bug.

---

## 4. What did you learn about Streamlit and state?

In Streamlit, every time a user interacts with the app (clicks a button, enters text), the entire script reruns from top to bottom. This means variables defined outside callbacks are reset on every rerun. Streamlit's `session_state` is a special dictionary that persists across reruns—if you store a value in `st.session_state.secret`, it stays the same even after a button click causes a rerun. The key insight is: without `session_state`, the secret number would be regenerated on every rerun, making the game unwinnable. I'd explain this to a friend by saying: "Streamlit is like a grocery store that rebuilds itself every time you pick up an item, but the `session_state` cashier remembers what you've already done."

---

## 5. Looking ahead: your developer habits

**One habit I want to reuse:**
Write tests *while* debugging, not after. When I wrote `test_validate_guess_out_of_range_high()`, it immediately showed me whether my fix worked. I'll use this "test-driven debugging" habit in future labs—it saves time and gives confidence in the fix.

**One thing I'd do differently:**
I would ask AI more targeted questions earlier. Instead of "Explain what's wrong," I would ask "Compare the expected behavior and actual behavior for this specific input." This gets straight to the root cause faster.

**How this project changed my view of AI-generated code:**
I learned that AI-generated code isn't "bad by default"—it's a starting point that requires critical review. When Copilot suggested the `validate_guess()` function structure, I didn't just implement it verbatim; I tested edge cases like 0, 1, 100, 101 manually in the app to ensure the boundaries were correct. I also wrote tests that failed first (before the fix) to prove they were actually testing something. This project showed me I can use AI for speed (getting ideas fast) and brainstorming (naming functions, suggesting test patterns), but I have to be the one verifying correctness through testing and boundary analysis.
