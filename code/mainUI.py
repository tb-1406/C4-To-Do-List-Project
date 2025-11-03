# Team work on this together


tasks = []
#function called to check number of tasks

while True:
    print("-----------------------------------------------------------------------------")
    print("")
    if len(tasks) == 0:
        print("No tasks currently. To add tasks, type 'add [task name]'")
    else:
        for i, task in enumerate(tasks):
            print(f"[{i + 1}]", task)

    print("")
    print("-----------------------------------------------------------------------------")
    print("")

    cmdInput = input("->  ")

    try:   
        if cmdInput.lower().startswith("add "):
            item = cmdInput[4:].strip()
            if item:
                tasks.append(item)
    except:
        print("Error: Invalid input")
    
    print("")
    print("-----------------------------------------------------------------------------")
    
