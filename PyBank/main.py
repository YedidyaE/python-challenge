# Import modules 
import os
import csv 

# Find path and open csv
csv_filepath = os.path.join("DataSets_Python","budget_data.csv")

with open(csv_filepath, newline="") as csv_file:
    csv_data_object = csv.reader(csv_filepath, delimiter=",")
    for row in csv_data_object:
        print(row)
