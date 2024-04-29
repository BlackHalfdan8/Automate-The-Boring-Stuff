import random
import time

def generate_question():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    return num1, num2

def ask_question(num1, num2, question_num):
    attempts = 0
    while attempts < 3:
        start_time = time.time()
        user_answer = input(f"Question {question_num}: What is {num1} times {num2}? ")
        end_time = time.time()

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if end_time - start_time > 8:
            print("You've exceeded the time limit for this question.")
            return None

        if user_answer == num1 * num2:
            return user_answer
        else:
            print("Incorrect answer. Please try again.")
            attempts += 1

    print("You've reached the maximum number of attempts for this question.")
    return None

def main():
    num_questions = 10
    num_correct = 0

    for question_num in range(1, num_questions + 1):
        num1, num2 = generate_question()
        user_answer = ask_question(num1, num2, question_num)

        if user_answer is not None:
            print("Correct!")
            num_correct += 1

    print(f"You got {num_correct} out of {num_questions} questions correct.")

if __name__ == "__main__":
    main()
