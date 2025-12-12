def ask(question, correct_answer):
    answer = input(question + " ")
    if answer.lower() == correct_answer.lower():
        print("Correct! ✔️")
        return True
    else:
        print("Wrong! ❌")
        return False


score = 0
questions = [
    ("What is the capital of France?", "Paris"),
    ("How many legs does a spider have?", "8"),
    ("What is 5 + 7?", "12")
]

print("🎮 Welcome to the Mini Quiz Game!")

for q, ans in questions:
    if ask(q, ans):
        score += 1

print(f"\n🏆 You scored {score} out of {len(questions)}!")