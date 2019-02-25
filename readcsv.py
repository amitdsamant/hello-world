import csv
import pyodbc


with open('data/testdata.csv') as f:
    header = f.readline()
    data=[tuple(line) for line in csv.reader(f)]

    reader = csv.DictReader(f)
    print(reader)
    for row in reader:
        print('here')
        print(row)

print(data)

#cursor.executemany("insert into tablename(name, id) values (?, ?)", params)