"""
print pattern:
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3

"""


for x in range(1,4):
    for y in range(1,4):
        print(x,y)
    print()


#ignore 2 2

print("Next pattern.....")

for x in range(1,4):
    for y in range(1,4):
        if x==2 and y==2:
            continue
        print(x,y)
    print()


