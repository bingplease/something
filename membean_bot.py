import keyboard
import pyautogui
import time
import random
import tkinter
time.sleep(3)
pyautogui.click(2000, 400)
time.sleep(3)
pyautogui.click(1350, 900)
while True:
	for i in range(1, int(1000)):
		keyboard.press_and_release('A')
		time.sleep(1)
		keyboard.press_and_release('N')
		time.sleep(1)
	keyboard.press_and_release('X')
	time.sleep(3)
	pyautogui.click(2000, 400)
	time.sleep(3)
	pyautogui.click(1350, 900)
