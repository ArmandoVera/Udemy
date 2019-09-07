import csv 
import os

#udemy_csv = "./resources/web_starter.csv"
udemy_csv = os.path.join(".","resources","web_starter.csv")


title = []
price =[]
subscribers =[]
reviews =[]
reviews_percent =[]
lenght =[]


with open(udemy_csv, "r") as cvsfile:
    csvreader = csv.reader(cvsfile, delimiter = ",")
    for row in csvreader:
        #add title
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        percent = round(int(row[6])/ int(row[5]),2)
        reviews_percent.append(percent)
        new_lenght = row[9].split(" ")
        lenght.append(float(new_lenght[0]))






    #test = next(csvreader)
    
#print(lenght)

cleanCsv = zip(title,price,subscribers,reviews,reviews_percent,lenght)
outputfile = os.path.join("webFinal.csv")
with open(outputfile, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Title","Course Price","Subscribers","Reviews","Percent of Riviews","Lenght of Course"])
    writer.writerows(cleanCsv)
