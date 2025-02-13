#Q4.to calculate the num of chars in a word
sen=input("enter a sentence:")
def count(sen):
    #condition to count the chars
    words=sen.split()
    dic={w:len(w) for w in words}
    return dic
#print the result
print(count(sen))