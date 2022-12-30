import requests, time, random, string, termcolor, threading, os
from termcolor import colored, cprint
from datetime import datetime
tries = 0
#threads = 2

# To change the types of usernames go to line 22 and replace with one of these
chars = string.ascii_uppercase
charswithnum = string.ascii_uppercase + string.digits
numonly = string.digits

# How long should the username be?
length = 5

# Sets the colour
print_colour = lambda x: cprint(x, "green")



# Keep Looping to get usernames
while True:
    
    # Get random chars
    user = ''.join(random.choice(charswithnum) for i in range(length))
    
    # Add 1 Try
    tries += 1
    
    # Prints username that is being Tested
    print("Trying", user, "-", tries, "Tries")
    
    # Sleeps
    time.sleep(3)
    
    # Get a request from the roblox API and if it is not avalible then do this loop again
    req = requests.get("https://api.roblox.com/users/get-by-username?username=" + user)
    page = req.text

    # if it is availible then run this code that puts the username into a text file
    if not page.find('{"success":false,"errorMessage":"User not found"}') == -1:
        
        #Gets date
        now = datetime.now()
        dt_string = now.strftime("%d %B %Y %H:%M:%S")

        # Prints the username is not taken in colour
        print_colour("\nUsername is not taken\n")
        print_colour(user)
        print_colour("\nSaved into Usernames.txt")
        print("Found on", dt_string, "\n")

        # Puts the username into Usernames.txt including the timestamp when it was found
        open("Usernames.txt", "a").write(user + ' - Found on ' + dt_string + '\n')

        # Uncomment if you want to exit when you get an availible username
        #exit()
