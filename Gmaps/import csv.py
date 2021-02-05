import csv

with open('Provincial Parks Small.csv', 'r') as csvfile: 
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
