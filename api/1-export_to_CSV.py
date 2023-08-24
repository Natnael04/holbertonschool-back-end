import csv

# Sample data
data = [
    ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]
]

# Specify the CSV file path
csv_file_path = "USER_ID.csv"

# Open the CSV file for writing
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the data to the CSV file row by row
    for row in data:
        writer.writerow(row)

print("Data exported to CSV successfully.")