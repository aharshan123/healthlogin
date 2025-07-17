from xlrd import *

def usn_pwd():
    file = open_workbook(r"C:\Users\DELL\Desktop\pythonsel\testproject\heathmrs\healthmrs\testdata.xlsx")
    sheet = file.sheet_by_name('login')
    d = []
    for line in range(1,sheet.nrows):
        values = sheet.row_values(line)
        d.append(values)
    return d



