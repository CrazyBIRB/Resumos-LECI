import time
import pyautogui

time.sleep(1)  # Wait for 1 second to ensure focus
pyautogui.hotkey('ctrl', 'tab')  # Switch to the next tab in Firefox (if needed)
pyautogui.hotkey('ctrl', 'r')  # Refresh the current tab in Firefox

#Não funciona por agora.