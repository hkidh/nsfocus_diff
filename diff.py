

with open('hk1.txt', 'r') as t1, open('hk2.txt', 'r') as t2:
    tp1 = []
    tp2 = []
    for line in t1:
        tp1.append(line.strip())
    print(tp1)
    for line in t2:
        tp2.append(line.strip())
    print(tp2)
    for line in tp1:
        if line not in tp2:
            print(line)
    for line in tp2:
        if line not in tp1:
            print(line)
#     for line1 in t2:
#         tp2 = line1.strip()

# print(tp1)


            


    # print('-------------------')    
    # for line1 in t2:
    #     tp2 = line1.strip()
    #     print(tp2)


    

# with open('t1.txt', 'r') as t1, open('t2.txt', 'r') as t2:
#     for line in t2:
#         if t2 not in t1:
#             print(line)
    # f1 = t1.readlines()
    # print(f1)
    # f2 = t2.readlines()

# with open('update.txt', 'w') as outfile:
#     for line in f1:
#         if line not in f2:
# #            outfile.write(line)
#             print(line.strip())
#     print('------------------------------')
#     for line in f2:
#         if line not in f1:
#             print(line)