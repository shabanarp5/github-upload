from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import stopwords

""" Reading Input """

val  = input("Enter the text : ") 
print ("Input given :"+ str(val))


# Tokenization
tokens=sent_tokenize(val)
print("Tokens are :")
print(tokens)


wtokens=word_tokenize(val)
print("Word Tokens are :")
print(wtokens)




# Stopword removal
common_words = open("common_words.txt", "r")

with open("common_words.txt") as f:
  lineList = f.readlines()
  print(lineList)
print(common_words)
cwlist = [line.split('\n') for line in common_words.readlines()]
print(cwlist)


stop_words = cwlist
print(stop_words)



filtered_sentence = [w for w in wtokens if not w in stop_words[0]]

filtered_sentence = [] 
flag=0

for w in wtokens:
    for i in range(len(stop_words)):
        if w!=stop_words[i][0]:
            flag=1
            break
    if(flag==0):
        filtered_sentence.append(w)
  

print(filtered_sentence) 















class Reader:
    """Simplifies the reading of files to extract a list of strings. Simply pass in the name of the file and it will automatically be read, returning you a list of the strings in that file."""

    def __init__(self, name):
        """\"name\" is the name of the file to open. The file should be a series of lines, each line separated with a newline character."""
        self.name = name;

    def open_file(self):
        """Reads the file given by the file name and returns its contents as a list of seperate strings, each string being a line in the file."""
        with open(self.name) as fp:
            contents = fp.read().split()

        fp.close()
        return contents

    def open_file_single_string(self):
        """Reads the file given by the file name and returns its contents as a list of seperate strings, each string being a line in the file."""
        with open(self.name) as fp:
            contents = fp.read()

        fp.close()
        return contents

