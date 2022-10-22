import time
import pyautogui

#Wait for setup
time.sleep(4)

#Press x to start the minigame
pyautogui.keyDown(key="x")
time.sleep(0.1)
pyautogui.keyUp(key="x")
print("Basketball minigame started")

 

#Basketball loop
while True:
    pyautogui.keyDown(key="x")
    time.sleep(0.35)
    pyautogui.keyUp(key="x")


    #Wait for basketball to come back
    time.sleep(2)
    
