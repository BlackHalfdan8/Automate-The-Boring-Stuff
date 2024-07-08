from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def press_key(key):
    keyboard.press(key)
    keyboard.release(key)

moves = [Key.up, Key.right, Key.down, Key.left]

try:
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://play2048.co/')

    # Wait for the game to load
    time.sleep(5)

    while True:
        for move in moves:
            press_key(move)
            time.sleep(0.1)  # Adjust the sleep time as needed
except KeyboardInterrupt:
    print("Game stopped by user.")
except ImportError:
    print("Selenium not installed, proceeding without browser automation.")

    while True:
        for move in moves:
            press_key(move)
            time.sleep(0.1)  # Adjust the sleep time as needed
