from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import stopwords

""" Reading Input """

'''val  = input("Enter the text : ") 
print ("Input given :"+ str(val))'''



happyset=['Satisfied','pleased','happy','glad']

val=open("positive.txt", "r")
flagindicator=''
with open("positive.txt") as f:
  lineList = f.readlines()
  print((lineList))
  print(len(lineList))
  for i in range(len(lineList)):
      if(lineList[i]!='\n'):
          comment=lineList[i]
          commentval=comment.split(' ')
          for ix in range(len(commentval)):
              token=commentval[ix]
              for j in range(len(happyset)):
                  if(happyset[j] in token):
                      
                      flagindicator='Happy emotion'
                      break
          print("Comment : "+lineList[i]+ " is - "+flagindicator)
          
  
