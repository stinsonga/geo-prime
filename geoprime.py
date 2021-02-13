
import os
import string
import time
from random import choice, randint

# Name of branch
branch = "master"
# Name of your textfile dump in which to store generated text
filename = "example"
# Base commit message
commit_message = "Exciting stuff "
# Percent chance to clear dump file on each run of the loop. Set to zero to disable
clear_dump = 0
# How long to sleep between runs - base time
sleep_timer = 60
# Select generated language
language = "javascript"

# Our text generator:
def generate_stuff(length = 32, characters = string.ascii_letters + string.digits):
    return ''.join([choice(characters) for i in range(length)])

# Set file extension based on language
def return_file_format():
    if(language == "python"):
        return ".py"
    elif(language == "java"):
        return ".java"
    elif(language == "javascript"):
        return ".js"
    else:
        return ".py"

# Get generated function based on language
def get_generated_function():
    if(language == "python"):
        return generate_python_fun()
    elif(language == "java"):
        return generate_java_fun()
    elif(language == "javascript"):
        return generate_javascript_fun()
    else:
        return generate_python_fun()

# Generate a Python fynction
def generate_python_fun():
    return ("def my_function%s(): \n\t#%s" % get_function_body())

# Generate a Java function that returns void
# TODO: Create a full class per file
def generate_java_fun():
    return ("public void my_function%s(){ \n//%s\n}" % get_function_body())

# Generate a Javascript function
def generate_javascript_fun():
    return ("function my_function%s(){ \n//%s\n}" % get_function_body())

def get_function_body():
    return (generate_stuff(3, string.digits), (generate_stuff(32, string.digits) + generate_stuff(32, string.ascii_letters)))

# This is where the work happens.
# The loop runs until we stop it
while True:
    # Create working directory if it isn't there (uncomment on first use)
    # TODO: check for the directory's existence and run this if needed
    #os.system('mkdir work')

    # Generate filename
    write_file = filename+generate_stuff(4, string.ascii_letters)+return_file_format()
    # Randomly decide whether or not to remove existing dump file:
    if(randint(0,99) < clear_dump):
        print("Clearing dump file:")
        os.system('rm %s' % write_file)

    # Write to dump file
    for i in range(randint(1, 64)):
        # Generate function. Body will be a commented string TODO: eventually add random calls to standard library functions?
        stuff = get_generated_function()
        # Write to file
        os.system('echo "%s" >> work/%s' % (stuff, write_file))
    # Add/commit and push changes to Github
    os.system('git add work/%s' % write_file)
    os.system('git commit -m "%s"' % (commit_message + generate_stuff(8, string.ascii_letters)))
    # A brief pause seems to help mitigate scenarios where we get false 'everything up to date' results
    time.sleep(2)
    os.system('git push origin %s' % branch)
    sleepy_time = randint(1, 120) * sleep_timer
    print("Done, sleeping for %d seconds" % sleepy_time)
    time.sleep(sleepy_time)
