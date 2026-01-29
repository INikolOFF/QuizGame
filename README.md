# Ultimate Quiz Game

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![customtkinter](https://img.shields.io/badge/GUI-customtkinter-informational)
![Status](https://img.shields.io/badge/status-working-brightgreen)

A quiz game built with Python and customtkinter. Has multiple categories, a timer, and tracks your best scores per session.

---

## Features

- 5 categories: General Knowledge, Math, Science, Geography, and Random
- Timer per question — 10, 15, 20, 30 seconds or off
- Best score tracking per category (resets when you close the app)
- Progress bar during the quiz
- Instant feedback after each answer

---

## Requirements

```bash
pip install customtkinter
```

Python 3.x

---

## How to run

```bash
python quiz_game.py
```

---

## How to play

1. Pick a category from the main menu
2. Set the timer if you want one
3. Read each question and click an answer to select it
4. Hit **SUBMIT** to confirm
5. At the end you'll see your score and percentage
6. Play again to beat your best score

---

## Notes

- Best scores are only saved for the current session — closing the app resets them
- Random mode picks 10 questions mixed from all categories
- The timer moves to the next question automatically if it runs out

---

## Known issues

- No persistent score saving between sessions yet
- Only 5 questions per category — more coming later