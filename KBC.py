questions = [
    "What is founder of the pakistan?",
    "What is the capital of the pakistan?",
    "What is the name of our country?",
    "What is the boiling point of water?",
    "What is the PH scale number of water"
]

correct_answers = [
    "Quaid e Azam",
    "Islamabad",
    "Pakistan",
    "100 C",
    7
]

for i in questions:
    print(i)

user_answers = [input("Question 1: "),
                input("Question 2: "),
                input("Question 3: "),
                input("Question 4: "),
                int(input("Question 5: "))]

total_points = 0

for i, user_answer in enumerate(user_answers):
    if user_answer == correct_answers[i]:
        print("Question", i+1, ": Correct! You earn 10 Points.")
        total_points += 10
    else:
        print("Question", i+1, ": Incorrect!")

print("Total Points You Earned:", total_points)

if total_points == 50:
    print("Congratulations! You passed the Test.")
else:
    print(correct_answers)
