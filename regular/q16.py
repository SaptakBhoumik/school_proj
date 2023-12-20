'''
16. WAP to find avg word length
'''
def average_word_length(sentence):
    words = sentence.split()
    if len(words) == 0:
        return 0
    sum=0
    for word in words:
        sum=sum+len(word)
    return sum/len(words)
string=input("Enter the string:-")
print("Average word length:-",average_word_length(string))
