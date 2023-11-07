Quiz_questions = {
    "question1" : {
        "question" : "What is the capital of India",
        "answer" : "New Delhi"
    },
    "question2" : {
        "question" : "What is the capital of Pakistan",
        "answer" : "Islamabad"
    },
    "question3" : {
        "question" : "What is the capital of England",
        "answer" : "London"
    },
    "question4" : {
        "question" : "What is the capital of Peru",
        "answer" : "Lima"
    },
    "question5" : {
        "question" : "What is the capital of Sri Lanka",
        "answer" : "Colombo"
    },
    "question6" : {
        "question" : "What is the capital of China",
        "answer" : "Beijing"
    },
    "question7" : {
        "question" : "What is the capital of Bangladesh",
        "answer" : "Dhaka"
    },
     "question8" : {
        "question" : "What is the capital of Nepal",
        "answer" : "Kathmandu"
    },
     "question9" : {
        "question" : "What is the capital of Germany",
        "answer" : "Berlin"
    },
     "question10" : {
        "question" : "What is the capital of Belgium",
        "answer" : "Brussels"
    }
}


print("Answer the following 10 questions and check your score out of 10 at the end")
score = 0
for keys, values in Quiz_questions.items():
    print(f"Question: {values['question']}")
    answer = input("Answer: ").lower()
    if answer == values['answer'].lower():
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect!")
        score = score

print(f"Your score out of 10 : {score}")

