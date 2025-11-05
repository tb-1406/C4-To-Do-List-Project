#Navigator: Nava
#Driver: Marvellous

def complete(userInput, tasks):
    result = ''
    item = userInput[5:].strip()
    if item:
        try:
            for c in tasks[item]:
                result = result + c + '\u0336'
            tasks[item] = result
        except:
            print("ERROR: Invalid input")