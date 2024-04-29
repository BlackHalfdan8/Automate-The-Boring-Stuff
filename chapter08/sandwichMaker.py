import pyinputplus as pyip

sandwich_menu = {
    'bread': {'white': 1.50, 'wheat': 1.75, 'multigrain': 2.00},
    'protein': {'chicken': 3.00, 'turkey': 3.50, 'ham': 4.00, 'roast beef': 4.50},
    'toppings': {'lettuce': 0.50, 'tomato': 0.75, 'onion': 0.50, 'pickles': 0.75},
    'condiments': {'mayo': 0.25, 'mustard': 0.25, 'ketchup': 0.25, 'ranch': 0.50}
}

order = []
total_cost = 0.0

for category, options in sandwich_menu.items():
    print(f"\nSelect {category}:")
    for option, price in options.items():
        print(f"{option} - Cost: ${price:.2f}")
    print("Type 'done' to finish this category.")
    while True:
        choice = pyip.inputMenu(list(options.keys()) + ['done'], numbered=True)
        if choice == 'done':
            break
        else:
            order.append(choice)
            total_cost += options[choice]
            print(f"Added {choice} - Cost: ${options[choice]:.2f} | Total Cost: ${total_cost:.2f}")

print("\nYour sandwich includes:")
for item in order:
    print("- " + item)

print("\nTotal cost: $%.2f" % total_cost)
