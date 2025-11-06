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
        print("add [task name]: Add tasks to to-do list\ndelete [task no.]: Delete task item\ndone [task no.]: Mark task as complete\nclear: Remove all tasks\nmod [task no.]: Modify task\nexp [task no.]: Export task\nimp: Import tasks\n\n------------------------------------------------------------------------------------------------------------------------\n\nNo tasks currently.")
    else:
        print("add [task name]: Add tasks to to-do list\ndelete [task no.]: Delete task item\ncomplete [task no.]: Mark task as complete\nclear: Remove all tasks\nmod [task no.]: Modify task\nexp [task no.]: Export task\nimp: Import tasks\n\n------------------------------------------------------------------------------------------------------------------------\n")
        for i, task in enumerate(tasks):
            print(f"[{i + 1}]", task)

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
        elif cmdInput.startwith == "done":
            complete(cmdInput, tasks)
        elif cmdInput.startwith == "modify":
            modify(cmdInput, tasks)
            
    except:
        print("Error: Invalid input")
    
    print("")
    print("-----------------------------------------------------------------------------")
    
