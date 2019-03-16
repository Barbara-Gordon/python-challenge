import os
import csv

pollpath = os.path.join("Resources", "election_data.csv")

votesDict = {}
candidateset = set()
totalvotes = 0
finalvotes = {}

with open (pollpath, newline ="") as pollcsv:
    pollfile = csv.reader(pollcsv, delimiter = ",")
    
    next(pollfile, None)
    
    for row in pollfile:        
        candidateset.add(row[2])
        totalvotes +=1
        if votesDict.get(row[2]) is False:
            votesDict.update({row[2]: 1})
        else:
            newcount = votesDict.get(row[2],0) + 1
            votesDict.update({row[2]: newcount})
        

for key, value in votesDict.items():
    percentage = value / totalvotes
    percentage = format(percentage, ".2%")
    finalvotes.update({key :(value, percentage)})


winner = max(votesDict, key=votesDict.get)

candidatetext = ""

for key, value in finalvotes.items():
    candidatetext += "{}: {} ({})\n".format(key,value[1], value[0])
    
outputtext = (f"Election Results\n-------------------------\nTotal Votes: {totalvotes}\n-------------------------\n{candidatetext}\n-------------------------\nWinner: {winner}\n-------------------------")

print(outputtext)

output_path = os.path.join("outputfile.txt")

with open(output_path, "w") as textfile:
    textfile.write(outputtext)