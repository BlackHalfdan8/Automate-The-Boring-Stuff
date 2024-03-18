import pprint

print('Enter the text for which you would like to count characters. Type "done" on a new line when finished:')
message = ''
while True:
    line = input()
    if line.strip().lower() == 'done':
        break
    message += line + '\n'

count = {}
for character in message:
    if character == '\n':
        character = 'RETURN'
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)

# Prompt the user to enter more text or quit
while True:
    choice = input("Enter 'more' to add more text or 'quit' to exit: ").strip().lower()
    if choice == 'quit':
        break
    elif choice == 'more':
        print('Enter more text. Type "done" on a new line when finished:')
        while True:
            line = input()
            if line.strip().lower() == 'done':
                break
            message += line + '\n'
        count = {}
        for character in message:
            if character == '\n':
                character = 'RETURN'
            count.setdefault(character, 0)
            count[character] += 1
        pprint.pprint(count)
    else:
        print("Invalid choice. Please enter 'more' or 'quit'.")
