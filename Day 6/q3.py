# Input sentence from user
sentence = input("Enter Sentence Here: ")

# sentence -> split it into words
words = sentence.split(" ")

# Create an empty dictionary to store words
word_dict = {}

# update the dictionary values with each word iterations
for i in words:
    if i in word_dict:
        # incremelntig the count
        word_dict[i] += 1
    else:
        # add counting
        word_dict[i] = 1

# Print the word frequencies
for word, frquence in word_dict.items():
    print(f"{word}: {frquence}")