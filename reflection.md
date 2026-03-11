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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
