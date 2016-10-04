
import csv
import datetime
import sys
from operator import itemgetter

dateformat_space='%m-%d-%Y'
dateformat_pipe='%m-%d-%Y'
dateformat_comma='%m/%d/%Y'
names_space=(['last','first','unknown','gender','birthdate','color'])
names_pipe=(['last','first','unknown','gender','color','birthdate'])
names_comma=(['last','first','gender','color','birthdate'])

mydata=list()

def loadFile(filename,separator,field_names,dateformat,datalist):
    unknown_exists=False
    if('unknown' in field_names):
        unknown_exists=True
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile,delimiter=separator,fieldnames=field_names,skipinitialspace=True)
        for row in reader:
            row['birthdate']=datetime.datetime.strptime((row['birthdate']).strip(),dateformat)
            if(row['gender'][0]=='F'):
                row['gender']='Female'
            else:
                row['gender']='Male'

            if(unknown_exists):
                row.pop('unknown')
            datalist.append(row)

def sortData(listData,keys,reversed):
    sortedList=list()
    sortedList.extend(listData)
    L=min(len(keys),len(reversed))
    for i in range(0,L):
        sortedList=sorted(sortedList,key=itemgetter(keys[L-1-i]),reverse=reversed[L-1-i])
    return sortedList


def printData(mylist):
    writer=csv.writer(sys.stdout,delimiter=" ",quoting=csv.QUOTE_NONE,escapechar='\\')#,quotechar='')

    for row in mylist:
        writer.writerow((row['last'].strip(),row['first'].strip(),row['gender'].strip(),datetime.datetime.strftime(row['birthdate'],dateformat_comma),row['color'].strip()))



(loadFile('space',' ',names_space,dateformat_space,mydata))
(loadFile('comma',',',names_comma,dateformat_comma,mydata))
(loadFile('pipe','|',names_pipe,dateformat_pipe,mydata))

print("Output 1:")
x=sortData(mydata,keys=['gender','last'],reversed=[False,False])
printData(x)

print("Output 2:")
x=sortData(mydata,keys=['birthdate','last'],reversed=[False,False])
printData(x)

print("Output 3:")
x=sortData(mydata,keys=['last'],reversed=[True])
printData(x)
