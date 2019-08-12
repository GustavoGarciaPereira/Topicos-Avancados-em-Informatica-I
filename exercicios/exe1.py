


print("!")
for i in range(1000, 10000):
    #print(str(i)[0:2])
    #print(str(i)[2:])

    #if int(str(i)[0:2]) + int(str(i)[2:])) ** 2) == i:
    #print("x", int(str(i)[0:2]) + int(str(i)[2:]))
    resto = i % 100
    res = i // 100
    if ((resto + res) ** 2) == i:
        print(i)