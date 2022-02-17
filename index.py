
def countChar(word,countLetter = 0,count = 0):
    word = word.lower()
    lst = list(word)
    if lst[countLetter] == "a" or lst[countLetter] == "e" or lst[countLetter] == "i" or lst[countLetter] == "o" or lst[countLetter] == "u":
        count+=1
    countLetter += 1
    if countLetter < len(word):
        countChar(word,countLetter,count)
    else:
        print(f"Number to vowels letters in your phrase is: {count} times.")
        return


countChar("I love python")