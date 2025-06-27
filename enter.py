import random
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["a) Karachi", "b) Islamabad", "c) Lahore"],
        "answer": "b"
    },
    {
        "question": "Who developed Python?",
        "options": ["a) Guido", "b) Elon", "c) Bill"],
        "answer": "a"
    },
]
print(random.choice(questions))