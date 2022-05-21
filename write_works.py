import openpyxl

def write_object_works(object_info):
	wb_w = openpyxl.load_workbook('ZP.xlsx')
	ws_w = wb_w['Расчет']
	ws_w.cell(row = ws_w.max_row, column = 1)
	ws_w.append(object_info)
	wb_w.save('ZP.xlsx')



if __name__ == "__main__":
	object_info = ['какая-то херь', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]
	write_object_works(object_info)

