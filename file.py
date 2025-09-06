import sys

all = []

with open("randoms+20.txt", "r") as file:
    for f in file:
       all.append(int(f.rstrip()))

for n in range(0, len(all)):
    min_value = sys.maxsize
    pos = 0
    for i in range(n, len(all)):
        if min_value > all[i]:
            pos = i
            min_value = all[i]
    if min_value < all[n]:
        all[pos] = all[n]
        all[n] = min_value
       

with open("randoms_sorted+20.txt", "w+") as file:
    for number in all:
        file.write(str(number) + "\n")