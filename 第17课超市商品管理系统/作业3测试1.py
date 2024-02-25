import openpyxl

book = openpyxl.load_workbook(u"超市管理系统.xlsx")
sheet1 = book["账户"]
sheet2 = book["商品统计"]
sheet3 = book["销售额"]
# 打印表格名
print(sheet1)
# 打印每一列的名
print(book.sheetnames)
# 打印其中一个单元格
print(sheet1["B2"].value)
# 取一列数据并打印
sheet1_line_2 = sheet1["B"]
sheet1_line_3 = sheet1["C"]
num = len(sheet1_line_2)
print(sheet1_line_2)
for i in range(num):
    print(sheet1_line_2[i].value)
    print(sheet1_line_3[i].value)
sheet2_line_2 = sheet2["B"]
a = sheet2_line_2[1].value
print(a)
print(type(a))
book.close()
