f = open('newfile.py', 'w')   # Open 'newfile.txt' for writing
f.write('import numpy as np\n')           # Here '\n' means new line
f.write('x = 9\n')
f.write('y = np.sqrt(x)\n')
f.write("print(y)")
f.close()