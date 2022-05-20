import xlsxwriter
import openpyxl

# def write_object(object_name):
# 	wb_r.active = 0
# 	object_name_list = [object_name]
# 	print(wb_r.active)
# 	ws_r.append(object_name_list)

def calculate_total_price():
	object_name_list = wb_r.sheetnames
	price_list_done = read_price_list_done()
	print(object_name_list)
	
	
	if 'Цены' in object_name_list:
		wb_r.active = 2
		print(wb_r.active)
		price_list  = [ws_r.cell(row=i,column=2).value for i in range(1,18)]
	else:
		wb_r.create_sheet("Цены")
	print(ws_r.max_column,ws_r.max_row)
	print(price_list_done)
	print(price_list,wb_r.active)

def read_price_list_done():
	object_name_list = wb_r.sheetnames
	price_list_done = []
	if 'Расчет' in object_name_list:
		wb_r.active = 1
		work_column = ws_r.max_column
		work_row = ws_r.max_row
		for row in ws_r.iter_rows(min_row= work_row, max_row=work_row, max_col=work_column, min_col=2):
			for cell in row:
				price_list_done.append(cell.value)	
	else:
		wb_r.create_sheet("Расчет")
	return 	price_list_done	

	# for column in range(1,wb_s.max_column)
	# total_cost

wb_r = openpyxl.load_workbook('ZP.xlsx')
ws_r = wb_r.active
#write_object("Zassssdasdagsddsa")
calculate_total_price()
wb_r.save('ZP.xlsx')




