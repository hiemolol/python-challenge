import os
import csv

pyBANKfile = os.path.join('..', 'pyBANK', 'pyBANK.csv')

with open(pyBANKfile, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    print("Financial Analysis")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Name rows/make lists -> row 0 is months and row 1 is profit/losses
    Months = []
    ProfitLoss = []

    for row in csvreader:
        Months.append(row[0])
        ProfitLoss.append(int(row[1]))

print(f"Total Months: {len(Months)}")
print(f"Total: ${(sum(ProfitLoss))}")

# Make varible for profit change between months
ProfitChange = []
for i in range(len(ProfitLoss)-1):
    ProfitChange.append(ProfitLoss [i+1]-ProfitLoss[i])

print(f"Average Change: {round(sum(ProfitChange)/len(ProfitChange),2)}")

# Determine Max and min of list
MaxProfit = max(ProfitChange)
MinProfit = min(ProfitChange)

# Find month that corresponds to max and min
MonthMax = ProfitChange.index(max(ProfitChange))+1
MonthMin = ProfitChange.index(min(ProfitChange))+1

print(f"Greatest Increase in Profits: {Months[MonthMax]} (${(MaxProfit)})")
print(f"Greatest Decrease in Profits: {Months[MonthMin]} (${(MinProfit)})")

file = open("pyBank Output.text", "w")

file.write("Financial Analysis")
file.write("\n")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file.write("\n")
file.write(f"Total Months: {len(Months)}")
file.write("\n")
file.write(f"Total: ${(sum(ProfitLoss))}")
file.write("\n")
file.write(f"Average Change: {round(sum(ProfitChange)/len(ProfitChange),2)}")
file.write("\n")
file.write(f"Greatest Increase in Profits: {Months[MonthMax]} (${(MaxProfit)})")
file.write("\n")
file.write(f"Greatest Decrease in Profits: {Months[MonthMin]} (${(MinProfit)})")