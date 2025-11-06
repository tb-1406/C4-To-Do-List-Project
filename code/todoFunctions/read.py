# Tiago & Endu
#Navigator: Tiago 


def read(task = [], *args ):
    with open("inst.txt","w") as f:
        for item in task:
            f.write(str(item) + "\n")
    

    with open("inst.txt", "r") as f:
            print(f.read())





