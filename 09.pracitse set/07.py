line = 2

with open("log.txt","r") as f:
    line = f.readline()

    if ("python" in line):
        print(f"yes python is present . Line no:{line}")
    
    else:
        print("No python is not present.")

