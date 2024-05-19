import csv

with open('precipitation_data.csv', 'r') as file:
    reader = csv.reader(file)
    print(reader)
    next(reader)  # Skip header row
    for row in reader:
        print(row)
