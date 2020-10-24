
# import modules 
import os
import csv


#set path for file
budget_data = os.path.join("Resources", "budget_data.csv")


#set the output for the text file 
text_path = "analysis_output.txt"

                           
#set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = 0
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []


#opencsv file
with open (budget_data, "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    
    #Loop through to find total months 
    for row in csvreader:
        
        #count the total of months
        total_months += 1
        
        
        #calculate th total revenue over the entire period
        total_revenue = total_revenue + int(row['Profit/Losses'])
        
        #calculate the average change in revenue between months over the entire period
        revenue_change = float(row['Profit/Losses'])- previous_revenue
        previous_revenue = float(row['Profit/Losses'])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row['Date']]
        
        
        #the greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0]= row['Date']
         
        #the greatest decrease in revenue (date and amount) over the entire period 
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0]= row['Date']
            revenue_average = sum(revenue_change_list)/len(revenue_change_list)
      
            
   #write changes to csv
    with open(text_path, 'w') as file:
          file.write ('Financial Analysis\n')
          file.write('------------------\n')
          file.write('Total Months: %d\n' % total_months)
          file.write('Total Revenue: $%d\n' % total_revenue)
          file.write('Average Revenue Change $%d\n' % revenue_average)
          file.write('Greatest Increase in Revenue: %s ($%s)\n' % (greatest_increase[0], greatest_increase[1]))
          file.write('Greatest Decrease in Revenue: %s ($%s)\n' % (greatest_decrease[0], greatest_decrease[1]))
        
          
    