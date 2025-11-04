#Navigator: Endu
#Driver: Marvellous

def add(userInput, tasks):
        item = userInput[4:].strip()
        if item:
            tasks.append(item)