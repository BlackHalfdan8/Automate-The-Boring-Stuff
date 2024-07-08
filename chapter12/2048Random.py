from pynput.keyboard import Key, Controller
import time
import random

keyboard = Controller()

def press_key(key):
    keyboard.press(key)
    keyboard.release(key)

def make_random_move():
    moves = [Key.up, Key.down, Key.left, Key.right]
    move = random.choice(moves)
    press_key(move)

try:
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://play2048.co/')

    # Wait for the game to load
    time.sleep(5)

    while True:
        make_random_move()
        time.sleep(0.1)  # Adjust the sleep time as needed
except KeyboardInterrupt:
    print("Game stopped by user.")
except ImportError:
    print("Selenium not installed, proceeding without browser automation.")

    while True:
        make_random_move()
        time.sleep(0.1)  # Adjust the sleep time as needed
