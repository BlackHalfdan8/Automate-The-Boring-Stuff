import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    outcomes = []
    for _ in range(100):
        result = random.choice(['heads', 'tails'])
        outcomes.append(result)
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak_count = 0
    for i in range(1, len(outcomes)):
        # Check if the current outcome is the same as the previous one.
        if outcomes[i] == outcomes[i - 1]:
            streak_count += 1
        else:
            streak_count = 0 # Reset streak count if outcomes are different.
            
        # Check if the streak count has reached 6.
        if streak_count == 6:
            numberOfStreaks += 1
            # We could also reset streak_count here if we are interested in counting overlapping streaks.

# After the loop, print the result.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
