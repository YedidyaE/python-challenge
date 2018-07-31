# Import modules 
import os
import csv 

# Find path and open csv
csv_filepath = os.path.join("PythonDataSet", "budget_data.csv")

with open(csv_filepath, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    for row in csvreader:
        print(row)
