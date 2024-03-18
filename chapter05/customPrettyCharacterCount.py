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
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
