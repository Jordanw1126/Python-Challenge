#This will allow me to open up a file
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Initialize a variable to store the total number of votes
    total_votes = 0
    unique_candidates = []
    candidate_votes = {}
    winner = ""
    winning_votes = 0

    # Iterate through each row and count the votes
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

    #Find the candidates that are unique    
        if candidate_name not in unique_candidates:
            unique_candidates.append(candidate_name)

    #Add up the the total number each candidate won
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Find the winner based on the candidate with the most votes
    for candidate, votes in candidate_votes.items():
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes

#Results
print("Election Results")
print("-------------------------")
# Print the total number of votes cast
print(f'Total Votes: {total_votes}')
print("-------------------------")
    # Calculate and print the percentage of votes each candidate won
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f'{candidate}: {percentage:.3f}% ({votes})')
print("-------------------------")
    # Print the winner of the election based on popular vote
print(f"Winner: {winner}")
print("-------------------------")


# Export analysis results to a text file
with open("analysis_vote_results.txt", "w") as file:
    # Write the election results to the file
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f'Total Votes: {total_votes}\n')
    file.write("-------------------------\n")
    # Calculate and write the percentage of votes each candidate won
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f'{candidate}: {percentage:.3f}% ({votes})\n')
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

    # Confirm that the results have been written to the file
print("Election results have been saved to 'analysis_vote_results.txt'.")