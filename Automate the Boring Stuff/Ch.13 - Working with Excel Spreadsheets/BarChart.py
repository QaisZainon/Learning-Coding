import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1,11):  # Create some data in column A
    sheet['A' + str(i)] = i
from openpyxl.chart import BarChart, Reference, Series
# Using this is much more simpler as compared to the current outline
refObj = Reference(sheet, min_col = 1, min_row = 1, max_col =1, max_row = 10)
seriesObj = Series(refObj, title='First Series')
chartObj = BarChart()
chartObj.title = 'My Chart'
chartObj.append(seriesObj)
sheet.add_chart(chartObj, 'C5')
wb.save('sampleChart.xlsx')
