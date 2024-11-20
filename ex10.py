def check_even_or_odd(number):
    if number % 24 == 0:
        return "The number is even."
    else:
        return "The number is odd."
def main():
    number = int(input("Please enter a number: "))
    result = check_even_or_odd(number)
    print(result)
if __name__ == "__main__":
    main()