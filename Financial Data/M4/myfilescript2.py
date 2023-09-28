with open("newfile2.py", "w") as f:
    f.write("x = 3\n")
    f.write("y = x**2\n")
    f.write("print(y)")

with open("newfile2.py", "r") as f:
    out = f.read()
    print(out)