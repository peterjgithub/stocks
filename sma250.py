import csv
with open('/Users/peter/GitHub/stocks/us-sp500.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in myreader:
        print(', '.join(row))
