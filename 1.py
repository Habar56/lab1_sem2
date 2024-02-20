
word = str(input())
sm = 0
big = 0
for i in word:
    if i.isupper():
        big+=1 
    if i.islower():
        sm+=1
        
if big>sm:
    word2 = word.upper()
if sm>big:
    word2 = word.lower()
if sm==big:
    word2 = word
print (word2)

