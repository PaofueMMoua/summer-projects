import openpyxl
wb = openpyxl.load_workbook('testing.xlsx') 
sheet = wb['Sheet1']
sheet['A1']
sheet['A1'].value
print(sheet['A1'].value)