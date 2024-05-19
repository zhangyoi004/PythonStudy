from collections import OrderedDict

import xlwt,json


with open('../../resources/0015/city.txt', 'r', encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=OrderedDict)
    workbook=xlwt.Workbook()
    workbook.add_sheet('city',cell_overwrite_ok=True)
    for i,(key,value)in enumerate(data.items()):
        workbook.get_sheet(0).write(i,0,key)
        workbook.get_sheet(0).write(i,1,value)
    workbook.save('../../resources/0015/city.xls')

    # data = eval(f.read())
    # for key, value in data.items():
    #     print(key, value)