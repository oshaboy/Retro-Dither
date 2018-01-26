def makePalette(permutations):
    print("[")
    for i0 in range(permutations):
        for i1 in range(permutations):
            for i2 in range(permutations):
                i=[i0,i1,i2]
                print("\t(", end="")
                for j in range(3):
                    intensity = 255 // (permutations - 1) * i[j]

                    print(intensity, end="")
                    if j != 2:
                        print(", ", end="")
                if (i[0] == permutations-1 and i[1] == permutations-1 and i[2] == permutations-1):
                    print(")")
                else:
                    print("),")
    print("]")

def makeMonoPalette(permutations, screenColor):
    print("[")
    for i in range(permutations):

        print("\t(", end="")
        for j in range(3):
            intensity = 255 // (permutations-1) * i
            print(intensity*screenColor[j]//255, end="")
            if j != 2:
                print (", ", end="")
        if (i == permutations-1):
            print(")")
        else:
            print("),")
    print("]")
makePalette((112, 66, 20))

