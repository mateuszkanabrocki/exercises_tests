with open('sample.txt', 'r', errors='ignore') as file:
    count = len(['sth' for line in file for letter in line if letter in 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'])  # lines are yield - better memory solution
    # count = len(['sth' for letter in file.read() if letter in 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'])
print(count)