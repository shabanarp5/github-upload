import csv
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import stopwords

data = pd.read_csv('EmotionWords.csv')
print(data)
print(len(data))

Joydataset=[]
Saddataset=[]
Angerdataset=[]
Disgustdataset=[]
Feardataset=[]

#for i in range(len(data)):
    #print(data(0))

fn = 'EmotionWords.csv'
with open(fn, 'r') as csvfile:
    # creating a csv reader object 
    csvreader = csv.reader(csvfile)  

    # extracting each data row one by one 
    for row in csvreader:
            if row[1]=='sadness':
                    Saddataset.append(row[0])        
            if row[1]=='joy':
                    Joydataset.append(row[0])      
            if row[1]=='anger':
                    Angerdataset.append(row[0])   
            if row[1]=='fear':
                    Feardataset.append(row[0])   
            if row[1]=='disgust':
                    Disgustdataset.append(row[0])

    csvfile.close()

f = open("SadData.txt", "a")

for i in range(len(Saddataset)):
    f.write(Saddataset[i]+"\n")

f.close()




f = open("JoyData.txt", "a")

for i in range(len(Joydataset)):
    f.write(Joydataset[i]+"\n")

f.close()




f = open("Angerdataset.txt", "a")

for i in range(len(Angerdataset)):
    f.write(Angerdataset[i]+"\n")

f.close()




f = open("Feardataset.txt", "a")

for i in range(len(Feardataset)):
    f.write(Feardataset[i]+"\n")

f.close()




f = open("Disgustdataset.txt", "a")

for i in range(len(Disgustdataset)):
    f.write(Disgustdataset[i]+"\n")

f.close()

'''    try:
        #print(rows[1][1])
        for row in rows[1:]:
            # parsing each column of a row
            if row[0][0]!="":
                query="";
                    query="insert into staging_product_master values (";
                    for col in row: 
                        query =query+"'"+col+"',"
                    query =query[:-1]
                    query=query+");"
                print("query :"+str(query), flush=True)
                cursor.execute(query)
                connection.commit()
        except:
            print("An exception occurred")
        csvfile.close()'''



#data = pd.read_csv('Book1.csv')
#print(data)
#print(len(data))
#print(data[2])

newdata=[]
fn = 'Book1.csv'
with open(fn, 'r') as csvfile:
    # creating a csv reader object 
    csvreader = csv.reader(csvfile)  

    # extracting each data row one by one 
    for row in csvreader:
            newdata.append(row[0])

    csvfile.close()

print(newdata)
print(len(newdata))


for i in range(0,len(newdata)):
        val=newdata[i]
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
          #print("------------------1")
        #print(common_words)
        cwlist = [line.rstrip('\n') for line in common_words.readlines()]
        #print("------------------2")
        #print(cwlist)


        stop_words = cwlist
        #print("------------------3")
       # print(stop_words)



        filtered_sentence = [w for w in wtokens if not w in stop_words[0]]


        filtered_sentence = [] 
        #flag=0
        for w in wtokens:
            if w not in stop_words:
                filtered_sentence.append(w)

        '''for w in wtokens:
            for i in range(len(stop_words)):
                if w!=stop_words[i][0]:
                    flag=1
                    break
            if(flag==0):
                filtered_sentence.append(w)'''
        mylst = set(filtered_sentence)
        finalized_words = list(mylst)
        #print(filtered_sentence)
        print("****************************************")
        print("Finalized Words:")
        print(finalized_words)
        print("****************************************")
        for fnword in finalized_words:
            print(fnword)

        val  = input("Hit enter to continue")


