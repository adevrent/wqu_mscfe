with open('output.txt', 'a') as fo:
    fo.write('\nThis is the end of the file')

with open('output.txt', 'r') as fo:
    print(fo.read())