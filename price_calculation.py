import xlsxwriter
import openpyxl

def write_object(object_name):
	wb_r.active = 0
	wb_w.active = 0
	ws_w.write(wb_r.active.max_row,0,object_name)


wb_w = xlsxwriter.Workbook('ZP.xlsx')
ws_w = wb_w.add_worksheet()
object_name_list = []
wb_r = openpyxl.load_workbook('ZP.xlsx')
print(wb_r.active.cell(1,1).value)
ws_r = wb_r.active
for i, row in enumerate (ws_r.iter_rows()):
	for cell in row:
		object_name_list.append(wb_r.active.cell(wb_r.active.max_row,1).value)
		write_object(object_name_list[i])
		print(object_name_list)
write_object("Zassssdasdagsddsa")
wb_w.close()