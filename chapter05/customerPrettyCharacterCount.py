import pprint

print('Enter the sentence(s) for which you would like to have the characters counted.')
message = input()
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
pprint.pprint(count)
