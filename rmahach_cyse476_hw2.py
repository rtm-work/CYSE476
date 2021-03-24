import matplotlib.pyplot as plt



input1 = int(input("Press 1 for all ASCII, 2 for just letters & numbers: "))
filename = str(input("Input the filename, including the type (ex doi.txt): "))

if input1 == 1:
    allascii = {chr(i):0 for i in range (256)} #Makes a dictionary with all ASCII characters
    file1 = open(filename)
    total = 0
    data = []
    print("Starting...")

    for line in file1: #For each line in the file
        #print(line)
        for character in line: #For each character in a line
            #print(character)
            for x in allascii: #Goes through each entry in the dict for each letter
                #print(x)
                if character == x:#Compares each letter in each line with each entry in the dictionary
                    allascii[x] = allascii[x] + 1


    for x in allascii:
        total = total + allascii[x]

    for x in allascii:
        data.append(allascii[x])

    names = list(allascii.keys())

    for a, b in enumerate(names):
        names[a] = repr(b)



    for x, y in enumerate(data):
        data[x] = y / total

    for a, b in allascii.items():
        print(a, b)
        print("\n")
    #print(names)
    #print(data)
    #print(total)
    #print(allascii.values())
    z = sum(data)
    print(z) #Proves I did this right, output 1 or 0.99999repeating
    plt.ylim(0,1)
    plt.rc('xtick', labelsize=5)
    plt.bar(names, data)
    plt.show()
    

if input1 == 2:
    allascii = {chr(i):0 for i in range (256)} #Makes a dictionary with all ASCII characters
    file1 = open(filename)
    total = 0
    data = []
    names = []
    print("Starting...")

    for line in file1: #For each line in the file
        #print(line)
        for character in line: #For each character in a line
            #print(character)
            for x in allascii: #Goes through each entry in the dict for each letter
                #print(x)
                if character == x:#Compares each letter in each line with each entry in the dictionary
                    if character.isalnum() == 1: #Only counts alphanumeric numbers
                        allascii[x] = allascii[x] + 1


    for x in allascii:
        total = total + allascii[x]

    for x, y in allascii.items():
        if x.isalnum() == 1:
            data.append(allascii[x])

    for x, y in allascii.items():
        if x.isalnum() == 1:
            names.append(x)
    #names = list(allascii.keys())

    for a, b in enumerate(names): #Lets me actually print fricken unprintable characters
        names[a] = repr(b)



    for x, y in enumerate(data): #Sums up all of the counts to get a total count so I can find the percentages later
        data[x] = y / total


    for a, b in allascii.items(): #PProvides the count list
        if a.isalnum() == 1:
            print(a, b)
            print("\n")
    #print(names)
    print(data)
    #print(total)
    #print(allascii.values())
    z = sum(data)
    print(z) #Proves I did this right, output 1 or 0.99999repeating
    plt.ylim(0,0.2)
    plt.rc('xtick', labelsize=5)
    plt.bar(names, data)
    plt.show()