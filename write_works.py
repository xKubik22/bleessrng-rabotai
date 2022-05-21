import openpyxl
from price_calculation import max_rows


def write_object_works():
	# wb_w = openpyxl.load_workbook('ZP.xlsx')
	# ws_w = wb_w['Расчет']
	last_row = max_rows('Расчет')
	ws_w.cell(row = last_row, column = 1)
	ws_w.append(object_info)
	# wb_w.save('ZP.xlsx')



if __name__ == "__main__":
	wb_w = openpyxl.load_workbook('ZP.xlsx')
	ws_w = wb_w['Расчет']
	object_info = ['какая-то херь', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]
	write_object_works()
	wb_w.save('ZP.xlsx')
