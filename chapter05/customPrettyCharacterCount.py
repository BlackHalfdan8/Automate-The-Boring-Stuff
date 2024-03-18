import pprint
import sys

print('Enter the text for which you would like to count characters:')
message = sys.stdin.read()
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
