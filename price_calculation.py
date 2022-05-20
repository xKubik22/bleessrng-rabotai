import openpyxl
import os.path


def create_workbook(name: str):
	book = openpyxl.Workbook()
	book.save(name)
	book.close()


def write_object_in_sheet(object: list, book_name: str = 'ZP.xlsx'):
	if not os.path.isfile(book_name):
		create_workbook(book_name)
	book = openpyxl.load_workbook(book_name)
	sheet = book.active
	sheet.append(object)
	book.save(book_name)
	book.close()



