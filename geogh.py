
import os
import string
import time
from random import choice, randint

# Path to your intended repo - not really used yet
github_path = "https://github.com/stinsonga/GeoGH.git" 
# Name of your textfile dump in which to store generated text
filename = "blahwork.txt"
# Base commit message
commit_message = "Exciting stuff "
# Percent chance to clear dump file on each run of the loop
clear_dump = 10
# How long to sleep between runs
sleep_timer = (randint(1, 120) * 60)

# Our text generator:
def generate_stuff(length = 32, characters = string.ascii_letters + string.digits):
    return ''.join([choice(characters) for i in range(length)])

# Loop runs until we stop it
while True:

    # Randomly decide whether or not to remove existing dump file:
    if(randint(0,99) < 10):
        print("Clearing dump file:")
        os.system('rm %s' % filename)

    # Write to dump file
    for i in range(randint(1, 32)):
        stuff = generate_stuff(32, string.digits) + generate_stuff(32, string.ascii_letters)
        # os.system('echo "'+ stuff + '" >> "' + filename)
        os.system('echo "%s" >> %s' % (stuff, filename))
    # Add/commit and push changes to Github
    os.system('git add ' + filename)
    os.system('git commit -m "%s"' % (commit_message + generate_stuff(4, string.ascii_letters)))
    os.system('git push origin master')
    print("Done, sleeping for %d seconds" % sleep_timer)
    time.sleep(sleep_timer)

