import openpyxl

book = openpyxl.load_workbook("stats_104102.xlsx")

# 첫 번째 방법
# print(book.get_sheet_names())
# print(book.get_sheet_by_name("Sheet1"))

# 두 번째 방법
sheet = book.worksheets[0]
for row in sheet.rows:
    for data in row:
        print(data.value, end=" ")
    print("", end="\n")