import xlsxwriter
import openpyxl

# def write_object(object_name):
# 	wb_r.active = 0
# 	object_name_list = [object_name]
# 	print(wb_r.active)
# 	ws_r.append(object_name_list)

def read_price_list():
	read_price_list = []
	price_list_done = {}
	if 'Цены' in wb_r.sheetnames:
		wb_r.active = wb_r['Цены']
		for row in ws_r.iter_rows(min_row= 0, max_row=ws_r.max_row, max_col=ws_r.max_column, min_col=1):
			for cell in row:
				read_price_list.append(cell.value)	
	else:
		wb_r.create_sheet("Цены")
	price_list_done = {read_price_list[i]: read_price_list[i+1] for i in range(0, len(read_price_list) - 1,2)}
	return price_list_done
	
def calculate_price():
	object_work = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17']
	price_list = read_price_list()
	print(price_list)
	for key in price_list.keys():
		total_price += price_list[key] * object_work[key]
	# print(total_price)



wb_r = openpyxl.load_workbook('ZP.xlsx')
ws_r = wb_r.active
read_price_list()
calculate_price()
wb_r.save('ZP.xlsx')




# def read_price_list():
# 	object_name_list = wb_r.sheetnames
# 	price_list_done = []
# 	if 'Расчет' in object_name_list:
# 		wb_r.active = wb_r['Расчет']
# 		print(wb_r.active)
# 		work_column = ws_r.max_column
# 		work_row = ws_r.max_row
# 		print(work_column,work_row)
# 		for row in ws_r.iter_rows(min_row= work_row, max_row=work_row, max_col=work_column, min_col=2):
# 			for cell in row:
# 				price_list_done.append(cell.value)	
# 	else:
# 		wb_r.create_sheet("Расчет")
# 	print(price_list_done)
	 		

	# for column in range(1,wb_s.max_column)
	# total_cost
 # if 'Расчет' in object_name_list:
	# 	wb_r.active = 1
	# 	print(wb_r.active)
	# 	work_column = ws_r.max_column
	# 	work_row = ws_r.max_row
	# 	for row in ws_r.iter_rows(min_row= work_row, max_row=work_row, max_col=work_column, min_col=2):
	# 		for cell in row:
	# 			price_list_done.append(cell.value)			
	# else:
	# 	wb_r.create_sheet("Расчет")
	
	# print(price_list_done,wb_r.active)