string=input("enter your introduction")
characterCount=0
wordCount=1
for i in string:
    characterCount=characterCount+1
    if(i==' '):
        wordCount+=1
print(characterCount)
print("number of characters in the string")
print(wordCount)
print("number of words in the string")