from collections import OrderedDict

import xlwt,json

with open('../../resources/0016/numbers.txt', 'r', encoding='utf-8') as f:
    data = eval(f.read())
    workbook=xlwt.Workbook()
    sheet=workbook.add_sheet('numbers',cell_overwrite_ok=True)
    for row,d in enumerate(data):
        print(type(d))
        for col,d2 in enumerate(d):
            sheet.write(row,col,d2)
    workbook.save('../../resources/0016/numbers.xls')