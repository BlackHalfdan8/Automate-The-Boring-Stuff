print('Please enter a list of values.')
user_values = input().split(',')

def comma_code(values):
    if len(values) == 1:
        return values[0]
    elif len(values) == 2:
        return values[0] + ' and ' + values[1]
    else:
        for i in range(len(values) - 1):
            print(values[i], end=", ")
        print('and ' + values[-1])

comma_code(user_values)
