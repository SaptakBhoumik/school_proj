'''
12. WAP to count the number of words in a sentence.
'''
def word_count(sentence):
    words = sentence.split()
    return len(words)
string=input("Enter the string:-")
print("Number of words:-",word_count(string))