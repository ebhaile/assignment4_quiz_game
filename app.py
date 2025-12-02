import random
import time

QUESTIONS = {
    "technology": [
        ("What does CPU stand for?", "central processing unit"),
        ("What company created the iPhone?", "apple"),
        ("What does RAM stand for?", "random access memory"),
        ("What programming language is used to style web pages?", "css"),
    ],
    "science": [
        ("What planet is known as the Red Planet?", "mars"),
        ("What gas do plants breathe in?", "carbon dioxide"),
        ("What is H2O more commonly known as?", "water"),
        ("What force keeps us on Earth?", "gravity"),
    ],
    "history": [
        ("Who was the first president of the United States?", "george washington"),
        ("The Great Wall is located in which country?", "china"),
        ("World War II ended in what year?", "1945"),
        ("Who was known as the 'King of Pop'?", "michael jackson"),
    ],
}

def choose_category():
    print("\nChoose a category:")
    for c in QUESTIONS.keys():
        print(f"- {c.title()}")
    while True:
        pick = input("Enter category: ").strip().lower()
        if pick in QUESTIONS:
            return pick
        print("❌ Invalid category. Try again.")

def ask_question(q, answer):
    print("\n❓ " + q)
    user = input("Your answer: ").strip().lower()
    if user == answer:
        print("✔ Correct!")
        return True
    else:
        print(f"❌ Wrong — the correct answer was: {answer.title()}")
        return False

def play_quiz():
    print("\n=== QUIZ MASTER ===")
    category = choose_category()
    questions = QUESTIONS[category][:]
    random.shuffle(questions)

    score = 0

    for q, ans in questions:
        if ask_question(q, ans):
            score += 1
        time.sleep(0.4)

    print(f"\n🏆 Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 PERFECT SCORE!")
    elif score > len(questions) // 2:
        print("🔥 Great job!")
    else:
        print("🙂 Keep practicing!")

def main():
    while True:
        play_quiz()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye, Quiz Master!")
            break

if __name__ == "__main__":
    main()
