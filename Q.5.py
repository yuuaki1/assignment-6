def sort_words(sentence):
    # split the sentence into words
    words = sentence.split("-")
    # sort the words
    words.sort()
    # join the sorted words with a hyphen
    sorted_sentence = "-".join(words)
    # print the sorted sentence
    print(sorted_sentence)

# test the function
sort_words("green-red-yellow-black-white")
