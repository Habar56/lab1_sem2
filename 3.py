print("000".isdigit())
word =(input())
word2=""
def sum(string):
    summ=0
    for i in string:
        summ += int(i)
    return summ
if word.isdigit():
    print(sum(word))

else:
    for i in range(len(word)):
        if word[i].isdigit():
            word2+=word[i]
    print(sum(word2))
