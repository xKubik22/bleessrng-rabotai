import xlsxwriter
import openpyxl

def write_object(object_name):
	wb_r.active = 0
	object_name_list = [object_name]
	print(wb_r.active.max_row)
	ws_r.append(object_name_list)

wb_r = openpyxl.load_workbook('ZP.xlsx')
ws_r = wb_r.active
write_object("Zassssdasdagsddsa")

wb_r.save('ZP.xlsx')



