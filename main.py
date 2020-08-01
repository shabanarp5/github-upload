import csv
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from sklearnmetrics import score
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

termjfreq=0
caljfreq=0

termsfreq=0
calsfreq=0

termafreq=0
calafreq=0

termdfreq=0
caldfreq=0

termdfereq=0
caldfereq=0


NNS=0
NN=0
NNP=0
VB=0

data = pd.read_csv('EmotionWords.csv')
#print(data)
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



termjfreq=len(Joydataset)

termsfreq=len(Saddataset)

termdfreq=len(Disgustdataset)

termdfereq=len(Feardataset)
termafreq=len(Angerdataset)

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

#print(newdata)
print(len(newdata))


for i in range(0,len(newdata)):
        val=newdata[i].lower()
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
        print(cwlist)


        stop_words = cwlist
        #print("------------------3")
        #print(stop_words)



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

        #Pos Tagger
        tagged = nltk.pos_tag(finalized_words)
        print(tagged)

        for i in range(len(finalized_words)):
                if tagged[i][1]=="NNS":
                        NNS=NNS+1
                if tagged[i][1]=="NN":
                        NN=NN+1
                if tagged[i][1]=="NNP":
                        NNP=NNP+1
                if tagged[i][1]=="VB":
                        VB=VB+1       

        
        #print(tagged[0][1])
        print("****************************************")


        # Emotion recognizer
        emotion='Neutral'
        for fnword in finalized_words:
            print(fnword)
            
            
            for i in range(len(Feardataset)):
                    if fnword==Feardataset[i]:
                            emotion='Fear'
                            caldfereq=caldfereq+1
                            break;
        
            for i in range(len(Saddataset)):
                    if fnword==Saddataset[i]:
                            emotion='Sad'
                            calsfreq=calsfreq+1
                            break;
                        
            for i in range(len(Joydataset)):
                    if fnword==Joydataset[i]:
                            emotion='Joy'
                            caljfreq=caljfreq+1
                            break;
        
            
            for i in range(len(Angerdataset)):
                    if fnword==Angerdataset[i]:
                            emotion='Anger'
                            calafreq=calafreq+1
                            break;
        
            for i in range(len(Disgustdataset)):
                    if fnword==Disgustdataset[i]:
                            emotion='Disgust'
                            caldfreq=caldfreq+1
                            break;
        print(val)
        if " not " in val:
                if emotion=="Sad":
                        emotion="Joy"
                if emotion=="Joy":
                        emotion="Sad"
        print(val +" : "+emotion)
            
        #val  = input("Hit enter to continue")

''' if(NNS > NN and NNS > VB and NNS >NNP):
        #print('noun plural desks tags are more in emotion decision')
        
elif(VB > NN and VB > NNS and VB >NNP):
        #print('Verb tags are more in emotion decision')
        
elif(NN > VB and NN > NNS and NN >NNP):
        #print('Noun tags are more in emotion decision')
        
elif(NNP > NN and NNP > NNS and NNP >VB):
        #print('Proper Noun tags are more in emotion decision')
        
else:
        print('All tags have same priority') '''

calafrq=str((calafreq/termafreq)*100)
caldfeq=str((caldfreq/termdfreq)*100)
caljfrq=str((caljfreq/termjfreq)*100)
calfreq=str((calsfreq/termsfreq)*100)
caldfreq=str((caldfereq/termsfreq)*100)

print("Anger % : "+str(score.calafreq()))
print("Disgust % : "+str(score.caldfreq()))
print("Joy % : "+str(score.caljfreq()))
print("Sad % : "+str(score.calsfreq()))
print("Fear % : "+str(score.caldfereq()))
print("****************************************")
print("Percentage % : "+str(score.acc()))
print("****************************************")
