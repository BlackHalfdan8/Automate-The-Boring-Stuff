#! python3
# prettifiedStopwatch.py - A simple stopwatch program with a prettier output copied to clipboard.

import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()  # Press Enter to begin
print('Started.')

# Initialize variables.
startTime = time.time()  # Get the first lap's start time.
lastTime = startTime
lapNum = 1
lapTimes = []

# Start tracking lap times.
try:
    while True:
        input()  # Wait for the user to press Enter
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lapTimes.append(f'Lap #{str(lapNum).rjust(2)}: {str(totalTime).rjust(6)}s ({str(lapTime).rjust(5)}s)')
        print(lapTimes[-1], end='')
        lapNum += 1
        lastTime = time.time()  # Reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')

# Format the output to be copied to the clipboard.
formattedOutput = '\n'.join(lapTimes)
pyperclip.copy(formattedOutput)
print('Lap times copied to clipboard.')
