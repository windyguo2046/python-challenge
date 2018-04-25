import os
import csv

csvpath = os.path.join('raw_data', 'budget_data_2.csv')

lengths = 0
total_revenue = 0
revenue = []
revenue_change = []
months = []


with open(csvpath,newline="") as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
     csvreader = csv.reader(csvfile, delimiter = ",")
     print(csvreader)

     next(csvreader, None)

     for row in csvreader:
        lengths = lengths + 1
        total_revenue = total_revenue + int(row[1])
        months.append(row[0])
        revenue.append(row[1])
        
months.pop(0)

for i in range(len(revenue)-1):
    revenue_change.append (int(revenue[i+1])-int(revenue[i]))

greatest_increase = max(revenue_change)
gi_month = months[revenue_change.index(greatest_increase)]
greatest_decrease = min(revenue_change)
gd_month = months[revenue_change.index(greatest_decrease)]
avg_revenue_change = sum(revenue_change)/len(revenue_change)

# print (str(len(months)),str(len(revenue_change)))
print("Financial Anlysis")
print("-------------------")
print("Total Months: ", str(lengths))
print("Total Revenue: ", str(total_revenue))
print("Average Revenue Change: ", str(avg_revenue_change))
print("Greatest Increase in Revenue: ", gi_month, " ($", str(greatest_increase), ")")
print("Greatest Decrease in Revenue: ", gd_month, " ($", str(greatest_decrease), ")")





        

        