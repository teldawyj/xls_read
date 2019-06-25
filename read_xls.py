import xlrd as rd


class Xls:

    def __init__(self, file=None, sheet_num = 1):
        self.file = rd.open_workbook(filename=file)
        self.sheet = self.file.sheet_by_index(sheet_num-1)
        self.data = []
        print("n_row = ", self.sheet.nrows, "\nn_col = ", self.sheet.ncols)
        self.data = self.sheet._cell_values
        self.type = self.sheet._cell_types