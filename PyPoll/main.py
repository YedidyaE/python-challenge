# Import modules 
import os
import csv 

# Find path and open csv
csv_filepath = os.path.join("PyPollDataset", "election_data.csv")

#Declare and initialize variables to store data
total_votes = 0
candidate_options = [] #unique list of candidates
candidate_votes = {} #dictionary of candidates and corresponding votes
winning_candidate = ""
winning_votes = 0
candidate_vote_summary = ""

#Open CSV file

with open(csv_filepath, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    next(csvreader, None)  # skip the headers
    
#Loop through each row to perform the following calculations
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        
        #When the if statement runs on first occurence of candidate name, add it to the candidate options list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            
        #Add the candidate_name as key and set 0 as default value for the candidate_votes dictionary
        #Go through the rows and keep track of the votes for each candidate          
        candidate_votes[candidate_name] = candidate_votes.setdefault(candidate_name, 0) + 1
        
    #Set variables to hold the votes and vote percentages for each of the four candidates
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)* 100
        
        #set condition to determine the greates number of votes and set the winner
        if votes > winning_votes:
            winning_votes = votes
            winning_candidate = candidate_name 
            
        #Go through the rows and append candidate name, vote percentage and actual number of votes for each candidate on a new line    
        candidate_vote_summary = candidate_vote_summary + f"{candidate_name} : {vote_percentage: .3f}% ({votes}) \n"
            

            
            
#Create a variable to hold a multi line string
output = f"""Election Results
------------------------------
Total Votes : {total_votes}
------------------------------
{candidate_vote_summary}
------------------------------
Winner: {winning_candidate}"""
print (output)

#export as a txt  file
file_to_output = "pypoll_output.txt"
with open(file_to_output, 'w') as txt_file:
     txt_file.write(output)
  



            
            


