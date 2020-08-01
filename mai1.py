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
	    rows.append(row)
	    print(row)

    csvfile.close()

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
