import csv 

#Reads from a csv file and puts them all in a list and returns the list
class ReadFromCSV:
    def extract_from_csv(self,filename):
        with open(filename,'r', encoding='utf-8-sig') as fd:
            #csvFile = csv.reader(fd)
            theList = []
            for lines in fd:
                theList.append(lines)

            return theList
            #fd.read('\n'+submission)


PleaseReadToCSV = ReadFromCSV()

theList = []

theList = PleaseReadToCSV.extract_from_csv('wsbnew.txt')

putCount = 0
callCount = 0


for lines in theList:
    print(lines)

#print(theList[2])

