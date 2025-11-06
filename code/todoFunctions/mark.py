#Navigator: Nava
#Driver: Marvellous

def complete(userInput, tasks):
    index = int(userInput[5:].strip()) - 1
    tostrike = str(tasks[index])
    strikeCode = str("&#822;")
    newStr = ""

    for i in tostrike:
        newStr += strikeCode + i

    newStr += strikeCode
    tasks[index] = newStr
    
