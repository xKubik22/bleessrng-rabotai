import xlsxwriter
import openpyxl

wb_w = xlsxwriter.Workbook('ZP.xlsx')
ws_w = wb_w.add_worksheet()
ws_w. write('A1', 'Hello world')
wb_w.close()

wb_r = openpyxl.load_workbook('ZP.xlsx')
print(wb_r.active.cell(1,1).value)
