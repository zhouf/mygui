# 读取xls文件示例

import xlrd

file = 'D:\\My Documents\\VBA讲课材料\\2019年6月银行余额调节表-电子版\\41-000300040005641.xls'
file = 'D:\\My Documents\\VBA讲课材料\\2019年6月银行余额调节表-电子版\\42.xlsx'
# file = 'R:\\培养方案\\222.xls'

data = xlrd.open_workbook(file)
sheet = data.sheet_by_index(0)
nrows = sheet.nrows
ncols = sheet.ncols

for r in range(nrows):
    print(sheet.cell(r,1).value)