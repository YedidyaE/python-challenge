# Import modules 
import os
import csv 

# Find path and open csv
csv_filepath = os.path.join("PyBankDataset", "budget_data.csv")

#Declare and initialize variables to store data
total_months = 0
net_total = 0
changes = []
current_value = None
previous_value = None
current_change = None
min_change = 99999999 #initialize with a big number
max_change = 0
min_month = ""
max_month = ""


#Open CSV file

with open(csv_filepath, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    next(csvreader, None)  # skip the headers
    
 
 #Loop through each row to perform the following calculations
    for row in csvreader:
        #find total months by going down the rows
        total_months = total_months + 1
        current_value = int(row[1])
       
        #find total by adding the monetary value in each row
        net_total = net_total + current_value
        
        #Go through list calculating the changes and appending each change to the list
        if previous_value is not None:
                    current_change = current_value - previous_value 
                    changes.append(current_change)
                    
        previous_value = current_value
        
        #Set if conditions to find the max and min changes by comparing to current change
       
        if (current_change is not None and current_change > max_change):
                     max_change = current_change
            #find corresponding month value for maximum change
                     max_month = row[0] 
        if (current_change is not None and current_change < min_change):
                     min_change = current_change
            #find corresponding month value for minimum change
                     min_month = row[0]
                
#find average change between months
    average_change =  sum(changes)/len(changes)    

#create a variable to hold a multi line string
output = f"""Financial Analysis
------------------------------
Total Months : {total_months}
Total : ${net_total}
Average Change : $ {round(average_change, 2)}
Greatest Increase in Profits : ${max_change} ({max_month})
Greatest Decrease in Profits : ${min_change} ({min_month})"""
print (output)

#export the output as a txt file

file_to_output = "pybank_output.txt"
with open(file_to_output, 'w') as txt_file:
    txt_file.write(output)
  
    