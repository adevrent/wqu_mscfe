with open("newfile.txt", "r") as f:
    file = f.readlines()
    with open("output.txt", "w") as fo:
        for i, line in enumerate(file):
            fo.write(f"Line {i}: {line} \n")

with open('output.txt', 'r') as fo:
    print(fo.read())