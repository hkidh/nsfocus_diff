

with open('t1.txt', 'r') as t1, open('t2.txt', 'r') as t2:


    f1 = t1.readlines()
    f2 = t2.readlines()

with open('update.txt', 'w') as outfile:
    for line in f1:
        if line not in f2:
#            outfile.write(line)
            print(line.strip())
    print('------------------------------')
    for line in f2:
        if line not in f1:
            print(line)