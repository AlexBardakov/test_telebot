import openpyxl

from datetime import datetime


def date_catalog_refresh():
    ws = openpyxl.load_workbook('Database.xlsx')
    wb = ws.active
    wb.cell(2, 2).value = datetime.now().strftime('%d.%m.%Y')
    ws.save('Database.xlsx')
