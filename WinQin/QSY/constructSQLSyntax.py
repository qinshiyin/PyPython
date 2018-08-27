#-*-coding:utf-8-*-

import xlrd as rd

data=rd.open_workbook(r'D:\AgSilver\Desktop\未解析竞品APP.tmp.xls')

sheet=data.sheet_by_name('Sheet1')

rows=sheet.nrows
cols=sheet.ncols

table=[[] for i in range(rows)]

for r in range(rows):
    for c in range(cols):
        table[r].append(sheet.cell(r,c).value)

sql=[str for i in range(rows)]
for r in range(rows):
    sql[r]='insert into table bx_app_services_dim select'
    for c in range(cols):
        if c==cols-1:
            sql[r] += ' \'' + table[r][c] + '\''
        else:
            sql[r]+=' \''+table[r][c]+'\''+','
    sql[r]+=' from dual;'
    print(sql[r])

print('It\'s OK!')