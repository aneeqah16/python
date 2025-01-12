import csv  # Importing the csv module for reading and writing CSV files

# Data to be written into a CSV file
data = [["name", "email_id", "phone_number"],
        ["aneeqah", "aneeqah@gmail.com", 678786578456],
        ["eman", "eman@gmail.com", 678676785345]
       ]

# Writing data to a CSV file
with open("data.csv", 'w', newline='') as f:  # 'w' for write mode, 'newline=""' to prevent extra new lines
    writer = csv.writer(f)  # Create a CSV writer object
    for i in data:
        writer.writerow(i)  # Write each row of data into the CSV file

# Reading data from the CSV file
with open("data.csv", "r") as f:  # Open in read mode
    read_data = csv.reader(f)  # Create a CSV reader object
    for i in read_data:
        print(i)  # Print each row from the CSV file

# Another set of data to write into a different CSV file
data1 = [[4, 7, 8], [6, 7, 4], [6, 8, 5]]

# Writing data to 'sample.csv'
with open("sample.csv", "w", newline='') as f:
    write = csv.writer(f)  # Create a CSV writer object
    for i in data1:
        write.writerow(i)  # Write each row into the CSV file

# Reading from 'sample.csv'
with open("sample.csv", "r") as f:
    read = csv.reader(f)  # Create a CSV reader object
    for i in read:
        print(i)  # Print each row from the 'sample.csv' file
