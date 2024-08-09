import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #Initialize variables
    total_month = 0
    net_total = 0
    previous_profit_loss = 0
    changes_in_profit_loss = []
    greatest_increase = 0
    greatest_increase_date = ""
    greatest_decrease = 0
    greatest_decrease_date = ""
    

    
    # Read each row of data after the header
    for row in csvreader:
        total_month = total_month + 1
        net_total = net_total + int(row[1])
        
        #Calculate changes is profit/losses
        if total_month > 1:
            change = int(row[1]) - previous_profit_loss
            changes_in_profit_loss.append(change)
            
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        #update previous profit/loss
            previous_profit_loss = int(row[1])

         # Calculate the sum of changes and the count of changes
            sum_changes = 0
            count_changes = 0

            for change in changes_in_profit_loss:
                sum_changes += change
                count_changes += 1

        # Calculate the average change
                if count_changes > 0:
                    average_change = sum_changes / count_changes
                else:
                    average_change = 0
       



#print the final results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_month}")
print(f"Net Total Profit/Loss: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})") 

# Export analysis results to a text file
with open("analysis_results.txt", "w") as file:
    file.write("Total Months: " + str(total_month) + "\n")
    file.write("Net Total Proft/Loss: " + str(net_total) + "\n")
    file.write("Average Change: " + str(average_change) + "\n")
    file.write("Greatest Increase In Profits: " + str(greatest_increase) + "\n")
    file.write("Greatest Decrease In Profits: " + str(greatest_decrease) + "\n")

        #Results have been exported to a text file
    print("Analysis results have been exported to analysis_results.txt")