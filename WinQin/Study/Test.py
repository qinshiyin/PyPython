#encoding:utf-8
#!usr/bin/env python

import xlrd as xr
import xlwt as xw


#打开数据集
data=xr.open_workbook(u"D:\AgSilver\Desktop\练习用坐标数据.xlsx")

#table=data.sheets()[0]             #通过索引获取
#table=data.sheet_by_index(0)       #通过索引获取
table=data.sheet_by_name("Sheet1")  #通过名称获取

rows=table.nrows
cols=table.ncols

x=[[] for i in range(rows-1)]

for r in range(rows-1):
    for c in range(cols-1):
        x[r].append(table.cell(r+1,c+1).value)
        print("%-f"%x[r][c],end='\t')
        #print x[r][c],'\t',
    #print
    print()
        

book=xw.Workbook(encoding='utf-8',style_compression=0)
sheet=book.add_sheet(sheetname='Sheet123',cell_overwrite_ok=True)
for r in range(rows-1):
    for c in range(cols-1):
        sheet.write(r+1,c+1,x[r][c])

#book.save(u"D:\AgSilver\Desktop\练习用坐标数据.xls")



