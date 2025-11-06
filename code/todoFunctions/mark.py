#Navigator: Nava
#Driver: Marvellous

def complete(userInput, tasks):
    item = userInput[5:].strip()
    tostrike = tasks[item]
    strikeCode = str("&#822;")
    newStr = ""

    for i in tostrike:
        newStr += strikeCode + i

    newStr += strikeCode
    tasks[item] = newStr
    
