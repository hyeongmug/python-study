import csv, codecs

filename = "test.csv"
file = codecs.open(filename, "r", "euc-kr")

reader = csv.reader(file, delimiter=",")
for cells in reader:
    print(cells[1], cells[2])