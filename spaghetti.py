with open("Spaghetti.txt","r") as f:
    content = f.read()
    words = content.split()
    word_frequency = {}

    for word in words:
        if word in word_frequency:
            word_frequency[word] +=1
        else:
            word_frequency[word] =1
    words_sorted = sorted(word_frequency, key=word_frequency.get)
    result = words_sorted[len(words_sorted)-1]

    print(result)