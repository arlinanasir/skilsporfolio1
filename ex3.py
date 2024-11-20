func = {}

func["name"] = input("what is your name: ")
func["hometown"] = input("where your hometown: ")

while True:
    age_input = input("how old are you: ")
    try:
        func["age"] = int(age_input)  
        break
    except ValueError:
        print("Invalid age. Please enter a number.")


print(f"Name: {func['name']}\nHometown: {func['hometown']}\nAge: {func['age']}")