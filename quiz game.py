print("Welcome to the Quiz!")
score = 0

question1 = str(input("What is the capital of France? "))
if question1 == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Paris.")

question2 = input("What is 5 + 7? ")
if question2 == "12":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 12.")

print(f"Quiz over! Your score: {score}/2")
