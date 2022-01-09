wordsFile = open("words.txt", "r")
words = []

for x in wordsFile:
    words.append(x.strip())
    #print(x.strip())

print("syntax: \nletters in correct position with _ for unknown letters, known letters, wrong letters")
print("possible first guesses: panic, morel, study")
print("please enter 'exit' when done.")
print(len(words))

while True:
    querry = input()
    if querry == "exit":
        print("goodbye ;)")
        exit()
    elif querry == "print":
        print(words)
        continue
    elif querry == "reset":
        words.clear()
        wordsFile = open("words.txt", "r")
        for y in wordsFile:
            words.append(y.strip())
        print("wordsList reset!")
        print(len(words))
        continue
        

    querry = querry.split(" ")

    #delete words with forbidden letters
    x = len(words)
    x = x - 1
    for wordIndex in range(len(words)):
        #add exception for querry[2] == out of bounds
    
        for letter in querry[2]:
            if x - wordIndex >= len(words):
                break
            elif letter in words[x - wordIndex]:
                words.pop(x - wordIndex)
                break
    
    #delete words who dont contain known letters
    x = len(words)
    x = x - 1
    for wordIndex in range(len(words)):
        for letter in querry[1]:
            if x - wordIndex >= len(words):
                break
            elif letter not in words[x - wordIndex]:
                words.pop(x - wordIndex)
                break
    
    #delete words with letters in the wrong position
    x = len(words)
    x = x - 1
    for wordIndex in range(len(words)):
        for y in range(5) :
            if querry[0][y] == "_":
                continue
            elif words[x - wordIndex][y] != querry[0][y]:
                words.pop(x - wordIndex)
                break


    print(len(words))