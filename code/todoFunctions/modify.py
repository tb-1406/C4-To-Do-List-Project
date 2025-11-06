#Navigator: Nava
#Driver: Endu

def modify(task, tasks):
    try:
      nummod = int(task) - 1
      content = tasks[nummod]
      newtask = input("Please input the new task:")
      tasks[nummod] = newtask
      print(f"Task: '{content}' has been modified.")
    except:
      print(f"Please provide an actual number.")