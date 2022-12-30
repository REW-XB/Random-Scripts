import pyautogui
import time
import random
import os
num = 0


# You need a text file try this for spamming random words
# https://raw.githubusercontent.com/dwyl/english-words/master/words.txt


# Loop
while True:
    time.sleep(0.2)
    
    # Press / to enter chat
    pyautogui.write('/') 
    time.sleep(0.2)

    # Opens the the text file and gets a random line
    lines = open('textdoc.txt').read().splitlines()
    myline =random.choice(lines)

    # Adds one to num This shows how many lines you chatted
    num+=1

    # This is made on linux so if your on windows replace this with "cls"
    os.system("clear")

    # Prints some info
    print(myline)
    print(num, "words chatted")

    # Write the Line
    pyautogui.write(myline, interval=0.15)
    time.sleep(1.5)

    # Press enter to send the message
    pyautogui.press('enter')
    print("-----")

