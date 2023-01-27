import string

def is_pangram(sentence):
    # remove punctuation from the sentence
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    # convert the sentence to lowercase
    sentence = sentence.lower()
    # create a set of the alphabet
    alphabet = set(string.ascii_lowercase)
    # check if all the letters of the alphabet are in the sentence
    return set(sentence).issuperset(alphabet)

# test the function
print(is_pangram("The quick brown fox jumps over the lazy dog")) # True
print(is_pangram("Hello World")) # False
