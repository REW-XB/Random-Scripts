import time
import os
import pyautogui
totallinenum = 0
linenum = 0
repeatnum = -1
countdownnum = 5

# This script chats text files line by line


# put a file here
a_file = open("beemovie.txt")
lines = a_file.readlines()


# countdown for script
while countdownnum > 0:
    os.system("clear")
    print("Put your mouse over the ROBLOX Window")
    print(countdownnum, "Seconds Left")

    time.sleep(1)
    countdownnum -= 1


# loop and chat
while True:
    # add one for repeat number
    repeatnum += 1
    linenum = 0
    for line in lines:
     # chatting
     # If your on windows replace this with cls
     os.system("clear")

     # add one to linenum
     linenum += 1
     
     # add one to totallinenum
     totallinenum+=1


     # Print stats
     print(line, "\nTotal Lines", totallinenum, "\nYour on line", linenum, "\nTotal Repeats", repeatnum)

     time.sleep(0.2)

     # enter chat
     pyautogui.write('/') 
     time.sleep(0.2)

     # write the line
     pyautogui.write(line, interval=0.15)
     pyautogui.press('enter')
     time.sleep(0.2)


     
