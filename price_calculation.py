import xlsxwriter
import openpyxl
import os.path


def create_workbook(name: str):
	book = openpyxl.Workbook()
	book.save(name)
	book.close()


def write_object_in_sheet(object_name: str, book_name: str = 'ZP.xlsx'):
	if not os.path.isfile(book_name):
		create_workbook(book_name)
	book = openpyxl.load_workbook(book_name)
	sheet = book.active
	sheet.append(tuple(object_name))
	book.save(book_name)


for i in range(5):
	write_object_in_sheet(str(i))

# wb_w = xlsxwriter.Workbook('ZP.xlsx')
# ws_w = wb_w.add_worksheet()
# object_name_list = []
# wb_r = openpyxl.load_workbook('ZP.xlsx')



