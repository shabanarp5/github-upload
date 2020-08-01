import csv
import pandas as pd

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
