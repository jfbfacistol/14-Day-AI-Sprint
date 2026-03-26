# Day 5: Local Automation
# Challenge: The Scenario: The CSV Extraction
# Your manager just emailed you a CSV file containing the latest Makati and Quezon City office listings. 
# You need to write a script that opens this file locally, reads the data line by line, and prints it out, completely bypassing Excel.

with open('properties.csv','r') as file_object:
    content = file_object.readlines()
    cleaned_content = content[1:]
    

print("--- INITIATING LOCAL DATA EXTRACTION ---")

for cleaned_list in cleaned_content:
    cleaned_value = cleaned_list.strip()
    print(f"Processing Row: {cleaned_value}")    
        
print("--- EXTRACTION COMPLETE ---")