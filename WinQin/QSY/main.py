#-*-coding:utf-8-*-

import xlwt as wt
import xlrd as rd
import numpy as np
import datetime as dt


data=rd.open_workbook(r'D:\AgSilver\Desktop\移动反制数据落地汇总2.xls')
sheet=data.sheet_by_index(1)

table=np.zeros((11,10))

res=[str() for i in range(11)]

for i in range(data.nsheets):
    if i>7:
        sheet=data.sheet_by_index(i)
        for r in range(11):
            for c in range(10):
                table[r][c]=table[r][c]+sheet.cell(r+3,c+1).value
            res[r]=str[r]+sheet.cell(r+3,10).value



workbook=wt.Workbook()
sheet=workbook.add_sheet('0831-0911',cell_overwrite_ok=True)
for r in range(11):
    for c in range(10):
        sheet.write(r,c,table[r][c])
name=dt.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
workbook.save('D:\AgSilver\Desktop\\'+name+'.xls')

print('It\'s OK！')



import numpy as np
import matplotlib.pyplot as plt

points=np.arange(-1,1,0.01)
(x,y)=np.meshgrid(points,points)
points=np.sqrt(x**2+y**2)
plt.imshow(points)
plt.colorbar()
plt.show()



