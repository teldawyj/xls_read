import xlrd as rd


class Xls:

    def __init__(self, file=None, sheet_num = 1):
        self.file = rd.open_workbook(filename=file)
        self.sheet = self.file.sheet_by_index(sheet_num-1)
        self.data = []
        self.data_t = []
        print("n_row = ", self.sheet.nrows, "\nn_col = ", self.sheet.ncols)
        self.sheet_data = self.sheet._cell_values
        # self.type = self.sheet._cell_types
        for i in range(self.sheet.nrows):
            for j in range(self.sheet.ncols):
                self.data[i][j] = self.sheet_data[i][j]
                self.data_t[i][j] = self.sheet_data[j][i]