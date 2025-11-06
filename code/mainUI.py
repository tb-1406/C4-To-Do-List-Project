# Team work on this together
import os
from init import *

tasks = []
#function called to check number of tasks

while True:
    os.system('cls')

    print("------------------------------------------------------------------------------------------------------------------------")
    print("")
    if len(tasks) == 0:
        print("\033[33madd [task name]: Add tasks to to-do list\ndelete [task no.]: Delete task item\ndone [task no.]: Mark task as complete\nclear: Remove all tasks\nmod [task no.]: Modify task\nexp [task no.]: Export task\nimp: Import tasks\033[0m\n\n------------------------------------------------------------------------------------------------------------------------\n\n\033[41mNo tasks currently.\033[0m")
    else:
        print("\033[33madd [task name]: Add tasks to to-do list\ndelete [task no.]: Delete task item\ndone [task no.]: Mark task as complete\nclear: Remove all tasks\nmod [task no.]: Modify task\nexp [task no.]: Export task\nimp: Import tasks\033[0m\n\n------------------------------------------------------------------------------------------------------------------------\n")
        for i, task in enumerate(tasks):
            print(f"\033[42m[{i + 1}]\033[0m", task)

    print("")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("")

    cmdInput = input("->  ")
    cmdInput = cmdInput.lower()

    try:   
        if cmdInput.startswith("add "):
            add(cmdInput, tasks)
        elif cmdInput == "clear":
            tasks.clear()
        elif cmdInput.startswith == "done":
            complete(cmdInput, tasks)
        elif cmdInput.startswith == "delete":
            print("test line")
            print(cmdInput)
            delete(cmdInput, tasks)
    except:
        print("Error: Invalid input")
    
    print("")
    print("-----------------------------------------------------------------------------")
    
