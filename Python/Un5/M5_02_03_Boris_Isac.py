import openpyxl
from openpyxl.styles import Font


file = openpyxl.load_workbook("02_Excel_data.xlsx")#open file

bold = Font(bold=True)#define Font options

olimpSheet = file["Olimpiadas"]#select sheet

selectedCells = ["A1","B1", "C1", "D1"]#All cells to bolt

for obj in selectedCells:#Bolt=True every Cells from selectedCells
    olimpSheet[obj].font = bold

for row in olimpSheet.rows:
    for collumn in row:
        #coordinate, value, bold
        print("{} {:>15}".format(collumn.coordinate, collumn.value), collumn.font.b)

file.save("02_Excel_data.xlsx")#save changes
file.close()#close file