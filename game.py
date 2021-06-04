# simple gameflow 

import turtle

Lines_new = list()

file = open("input.txt")
Lines = file.readlines()

for i in Lines:
    print(i.strip('\n'))
    Lines_new.append(int(i.strip('\n')))


for k in Lines_new:
    for m in Lines_new:
        if (k + m == 2020):
            print(k, m, k+m)
