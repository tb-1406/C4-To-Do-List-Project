# Tiago & Endu
#Navigator: Tiago 


def read(task = [], *args ):
    with open("inst","w") as f:
        for item in task:
            f.write(str(item) + "\n")
    

    with open("inst", "r") as f:
            print(f.read())





