def read_template(filename):
    with open(filename, 'r') as file:
        template = file.read()
    return template

def complete_mad_libs(template):
    adjective = input('Enter an adjective: ')
    noun1 = input('Enter a noun: ')
    verb = input('Enter a verb: ')
    noun2 = input('Enter another noun: ')

    filled_template = template.replace('ADJECTIVE', adjective) \
                             .replace('NOUN', noun1, 1) \
                             .replace('VERB', verb) \
                             .replace('NOUN', noun2, 1)

    return filled_template

def main():
    filename = 'mad_libs_template.txt'
    template = read_template(filename)
    completed_story = complete_mad_libs(template)
    print(completed_story)
    input("Press Enter to exit...")

if __name__ == '__main__':
    main()
