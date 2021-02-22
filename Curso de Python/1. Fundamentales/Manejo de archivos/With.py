'''



'''


import csv

with open('mock_data.csv') as csvfile:
    mock = list(csv.DictReader(csvfile))

print(mock[:3])