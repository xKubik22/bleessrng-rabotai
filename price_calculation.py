import openpyxl
from works_indexes import indexes 


def read_price_list():
	try:
		workbook = openpyxl.load_workbook('ZP.xlsx')
	except FileNotFoundError:
		workbook = openpyxl.Workbook()
		workbook.save('ZP.xlsx')

	price_list = []

	if 'Цены' not in workbook.sheetnames:
		workbook.create_sheet("Цены")
		workbook.save('ZP.xlsx')
		print('В файле ZP.xlsx отсутсвовал лист "Цены", который нужно заполнить')
		return None

	worksheet = workbook['Цены']
	for row in worksheet.iter_rows(min_row=0, max_row=worksheet.max_row-1, max_col=worksheet.max_column, min_col=1):
		for cell in row:
			price_list.append(cell.value)

	price_list_done = {price_list[i]: price_list[i+1] for i in range(0, len(price_list) - 1, 2)}

	if len(price_list_done) == 0:
		return None

	price_list_done.pop(None)
	workbook.close()
	return price_list_done


def calculate_price(object_work):
	price_list = read_price_list()
	total_price = 0
	try:
		for key in price_list.keys():
			total_price += int(price_list[key]) * object_work[indexes[key]]
	except AttributeError:
		print('Необходимо заполнить лист "Цены" в файле ZP.xlsx')

	return total_price


if __name__ == "__main__":
	print(calculate_price([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
