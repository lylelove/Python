def q2000(word,ch):
    # return word.find(ch)
    j = word.find(ch)
    for i in range(j+1):
        temp = word[i]
        word = word.replace(word[i],word[j+1-i])
        word = word.replace(word[j+1-i],temp)
    return word

print(q2000("abcdefg","d"))