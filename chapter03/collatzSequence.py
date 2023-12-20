# The Collatz Sequence Chapter 03 Practice Project
# Collatz Sequence logic.
def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        elif number % 2 == 1:
            number = 3 * number + 1
        print(number)

# user input validation try and except clause
while True:
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)
        break # Break the loop if the input is successfully converted
    except ValueError:
        print("Invalid input.  Please enter a valid integer.")

collatz(number)
