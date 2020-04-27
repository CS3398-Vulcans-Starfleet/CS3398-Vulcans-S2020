import subprocess
#try:
import pyautogui, time
#except ImportError:
#	subprocess.call("pip install pyautogui")

#Program used to automate using the calculator
#take screenshot of the buttons we want it to find on the screen 
# > tell it to find where buttons reside > 
# > click area that corresponds to the button  
time.sleep(3)

#locateCenterOnScreen looks for a match to the screenshots (.png) 
#must save the screenshots in the same directory as the program
print("...What is 1+1?")
pyautogui.click(pyautogui.locateCenterOnScreen('1key.png'))
time.sleep(0.5)
pyautogui.click(pyautogui.locateCenterOnScreen('pluskey.png'))
time.sleep(0.5)
pyautogui.click(pyautogui.locateCenterOnScreen('1key.png'))
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(1)
print("...What is 20 x 5?")
pyautogui.press('2')
time.sleep(0.3)
pyautogui.press('0')
time.sleep(0.5)
pyautogui.click(pyautogui.locateCenterOnScreen('multkey.png'))
time.sleep(0.5)
pyautogui.press('5')
time.sleep(0.5)
pyautogui.press('enter')
