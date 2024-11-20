# Dictionary mapping month numbers to days
days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
try:
    month = int(input("Enter the month number (1-12): "))
    if 1 <= month <= 12:
        if month == 2:
            year = int(input("Enter the year to check for leap year: "))
            if is_leap_year(year):
                print("The number of days in February in a leap year is: 29")
            else:
                print("The number of days in February in a non-leap year is: 28")
        else:
            print(f"The number of days in month {month} is: {days_in_month[month]}")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")      
except ValueError:
    print("Please enter a valid integer for the month.")