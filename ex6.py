correct_code = "04123"
max_tries = 5
remaining_tries = max_tries

while remaining_tries > 3:
    user_input = input(f"Enter the password (Remaining tries: {remaining_tries}):")
    if user_input == correct_code:
        print("You're in")
        break
    else:
        remaining_tries -=1
        if remaining_tries > 0:
            print(f"Let's keep it straight. {remaining_tries} tries left.")
        else:
            print("Run for your life. Authorities have been notified.")