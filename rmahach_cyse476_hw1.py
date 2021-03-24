#start = input("1: word -> pattern.\n")
start = int(input("1: Word -> pattern\n2: pattern -> words\n"))
if start == 1:
    input1 = input("Please enter the word\n")
    list = []
    for char in input1: #Appends the input into a list
        list.append(char)

    x = 0
    for a, b in enumerate(list): 
        if str(b).isalpha() == 1: #Ensures each string in the list is a letter, not a number
            x = x + 1 
        #print(x)
        #print(a,b)
    
        for c, d in enumerate(list):
            if str(b).isalpha() == 1:  #More letter vs number checks just in case
                if str(d).isalpha() == 1:
                    if b == d:  #If the letters are the same...
                        list[a] = x #Replaces them with the number in the counter
                        list[c] = x
    string = ""
    for a in list:
        string += str(a) #Puts things back into a string to print
    print(string)

#Everything up to here works. Everything after, god only knows.

if start == 2: #For code -> wordlist
    input2 = str(input("Please enter the pattern, starting from 1\n"))
    inputlist = []
    wordlist = []
    

    for char in input2:
        inputlist.append(char) #Puts input2 number pattern into a list
    file1 = open("words_alpha.txt")

    for word in file1: #Reads the 'words.txt' file and puts all the words into a list
        word1 = word.rstrip("\n") #Removes \n before
        wordlist.append(word1)    #Appending word to list
    #print(wordlist)

    
   
    templist = []
    #templist.append(word) #Now templist has each word in a different 'slot'
    templist = wordlist.copy()
    list2 = []
    str2 = ""
        

    for a in templist: #For each full word in the templist
        dumbass_list = list(a) #Okay so you finally have a word -> [ w, o, r, d ]
        x = 0
        #print(x)
        #print(dumbass_list) #- dumbass_list has each word split into a [ w, o, r, d]-like list, confirmed works
        for a, b in enumerate(dumbass_list): #For each LETTER in each word in dumbass list
            if str(b).isalpha() == 1:         #If there is actually a letter there
                x = x + 1                      #Increment counter. Prevents increment if we run into a number that was changed from a previous cycle
                for c, d in enumerate(dumbass_list): #Goes through the entire word for each letter
                    if str(b).isalpha() == 1:  #As it goes through the word once for each eltter, it
                        if str(d).isalpha() == 1: #checks for
                            if b == d:  #Similar letters
                                dumbass_list[a] = x #And if the letters are the same
                                dumbass_list[c] = x #It replaces them with the current counter #
        
        for f in dumbass_list:
            str2 += str(f)
            
        list2.append(str2)  
        str2 = ""
        
    for a, b in enumerate(list2): #Returns word candidates that match the pattern
        if input2 == b:
            print(wordlist[a])
        

    #print(templist)
    #print(dumbass_list)
    #print(list2)
    #print(str2) #problem here
    #print(wordlist)
    