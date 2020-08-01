from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import stopwords

""" Reading Input """

'''val  = input("Enter the text : ") 
print ("Input given :"+ str(val))'''



negativeset=['depress','broke','hurt','sad']

val=open("negative.txt", "r")
flagindicator=''
with open("negative.txt") as f:
  lineList = f.readlines()
  print((lineList))
  print(len(lineList))
  for i in range(len(lineList)):
      if(lineList[i]!='\n'):
          comment=lineList[i]
          commentval=comment.split(' ')
          for ix in range(len(commentval)):
              token=commentval[ix]
              for j in range(len(negativeset)):
                  if(negativeset[j] in token):
                      
                      flagindicator='sad emotion'
                      break
          print("Comment : "+lineList[i]+ " is - "+flagindicator)
          
  
