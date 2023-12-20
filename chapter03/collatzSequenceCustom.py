# The Collatz Sequence Chapter 03 Practice Project
# Collatz Sequence logic.
def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        elif number % 2 == 1:
            number = 3 * number + 1
        print(number)

# user input validation try and except clause; added option to input another integer or exit program
while True:
    try:
        user_input = input("Enter an integer (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting program.")
            break  # Exit the loop if the user wants to quit
            
        number = int(user_input)
        collatz(number)
        
        continue_option = input("Do you want to enter another number? (yes/no): ")
        if continue_option.lower() != 'yes':
            print("Exiting program.")
            break  # Exit the loop if the user doesn't want to continue

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
