# Advanced Version: Quiz with Multiple Questions
questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Netherlands": "Amsterdam",
    "Austria": "Vienna",
    "Switzerland": "Bern",
    "Portugal": "Lisbon"
}

score = 0

print("Welcome to the European Capitals Quiz!")
print("You will be asked for the capitals of 9 European countries.")
print("Let's start!\n")

for country, capital in questions.items():
    user_answer = input(f"What is the capital of {country}? ").strip()
    if user_answer.lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {capital}.")
    print()
print(f"Quiz complete! Your score is {score}/{len(questions)}.")