import os
import csv

pyPOLLSfile = os.path.join('..', 'pyPOLLS','pyPOLLS.csv')

# Set Variables and make dictionary of candidates 
TotalVotes = 0
Candidates = {}
CandidatePercent = {}
CandidateCount = 0
Winner = "" 

with open(pyPOLLSfile,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader, None)
    for row in csvreader:
        
        # Total Votes
        TotalVotes += 1
        if row[2] in Candidates.keys():
            Candidates[row[2]] += 1
        else:
            Candidates[row[2]] = 1

        for key, value in Candidates.items():
            CandidatePercent[key] = round((value/TotalVotes) * 100, 1)

        # Determine winner
        for key in Candidates.keys():
            if Candidates[key] > CandidateCount:
                Winner = key
                CandidateCount = Candidates[key]


print("Election Results")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Total Votes: " + str(TotalVotes))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for key, value in Candidates.items():
    print(key + ": " + str(CandidatePercent[key]) + "% (" + str(value) + ")")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Winner: " + Winner)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

file = open("pyPOLLS Output.text", "w")
file.write("Election Results")
file.write("\n")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file.write("\n")
file.write("Total Votes:" + str(TotalVotes))
file.write("\n")
for key, value in Candidates.items():
    file.write(key + ": " + str(CandidatePercent[key]) + "% (" + str(value) + ") \n")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file.write("\n")
file.write("Winner: " + Winner)
file.write("\n")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file.write("\n")

file.close()