# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Bugs Found and Fixed:**

1. **Input Validation Bug** — The game accepted invalid guesses like 101 in Normal mode (range 1–100) and decimal values like 97.7. These invalid inputs consumed attempts and were added to history without error feedback. 
   - **Fix:** Created `validate_guess()` function in `logic_utils.py` to check range limits. Updated `parse_guess()` to reject decimals. Restructured `app.py` to validate guesses *before* updating game state (attempts, history, score).

2. **Hint Logic Bug** — The comparison in `check_guess()` was reversed, so "Go Higher" appeared when the guess was too high.
   - **Fix:** Swapped the `>` comparator to correctly return "Too High" when guess exceeds secret.

3. **Difficulty Range Mismatch** — Easy mode displayed "1 to 20" in settings but other parts of the code referenced hardcoded ranges or different values.
   - **Fix:** Ensured `get_range_for_difficulty()` is used consistently throughout and that session state initialization respects the selected difficulty.

**How I Used AI Tools:**
- **VS Code Copilot (Inline Chat):** Asked debugging questions like "Explain step-by-step which part of the code could cause reversed hint logic" to understand the root cause
- **Copilot in Agent Mode:** Ran multi-file exploration to identify where guess parsing and validation happen, helping me centralize logic in `logic_utils.py`

**Testing & Verification:**
Wrote pytest tests to verify fixes:
- `test_validate_guess_within_range()` — Confirms valid guesses (like 97) are accepted
- `test_validate_guess_out_of_range_high()` — Confirms out-of-range guesses (like 101) are rejected in a 1–100 range
- `test_initial_game_state()` — Verifies game state initializes correctly
- `test_guess_too_high()`, `test_guess_too_low()`, `test_winning_guess()` — Validate hint logic

Ran `python3 -m pytest` and confirmed all tests passed.

## ✅ Test Results

All fixes were verified using pytest. Running `python3 -m pytest` executed the complete test suite with **25 tests passing**, confirming that all validation logic, game state initialization, and hint comparisons work correctly. The test suite includes:

- **6 original tests** for core game logic (win/loss/hints, state initialization, range validation)
- **19 new edge-case tests** for robust input validation:
  - Negative numbers, decimals, whitespace, special characters, zero
  - Boundary conditions (0, 1, 100, 101, 999999999999999)
  - Full validation flow from `parse_guess` → `validate_guess` → `check_guess`
  - Graceful error handling without game state corruption

The screenshot below shows the successful test run with all 25 tests passing:

![Pytest Results](images/Screenshot%202026-03-12%20at%208.52.32%20PM.png)

### Advanced Edge-Case Testing

For the optional extension, I used Copilot to identify and generate additional pytest cases for edge-case inputs that could break the game logic. These tests covered cases such as negative numbers, decimal values, values above the allowed range, non-numeric strings, and empty input.

After reviewing the generated tests, I ran the full test suite and confirmed that all tests passed successfully.

![Pytest results](images/Screenshot%202026-03-12%20at%208.52.32%20PM.png)

I used Copilot to propose edge-case scenarios and generate pytest cases, then reviewed the tests manually to confirm they matched the game's actual validation rules.

## 📸 Demo

**What the game does:**
The game is an interactive number-guessing challenge where the player selects a difficulty level (Easy, Normal, or Hard), which determines the range of numbers to guess and the number of allowed attempts. The game generates a secret number, and the player submits guesses. For each guess, the game provides feedback ("Go Higher" or "Go Lower") to guide the player toward the secret number. The player's score increases or decreases based on the guess outcome and attempt number. The game ends when the player either wins (guesses correctly) or runs out of attempts.

**Fixed game features:**
- ✅ Input validation: guesses must be whole numbers within the difficulty range (e.g., 1–100 for Normal mode)
- ✅ Correct hint logic: "Go Higher" when guess is too low, "Go Lower" when guess is too high
- ✅ Proper state reset: clicking "New Game" resets attempts, score, history, and generates a new secret number
- ✅ Pytest tests verify all core logic functions

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
