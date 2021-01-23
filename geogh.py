
import os
import time
from random import choice, randint
import string

# Path to your intended repo
github_path = "https://github.com/stinsonga/GeoGH.git" 
# Name of your textfile in which to store generated text
filename = "blahwork.txt"
commit_message = "Exciting, productive stuff "

def generate_stuff(length = 32, characters = string.ascii_letters + string.digits):
    return ''.join([choice(characters) for i in range(length)])

while True:
    for i in range(randint(1, 32)):
        stuff = generate_stuff(32, string.digits) + generate_stuff(32, string.ascii_letters)
        os.system('echo "'+ stuff + '" >> "' + filename + '")
    os.system('git add ' + filename)
    os.system('git commit -m' + commit_message + randint(1, 100))
    os.system('git push origin master')
    time.sleep(60)

