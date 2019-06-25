import pandas as pd

if __name__ == "__main__":
    # file = "E:\\o\\github_branch\\xls_read\\data\\day170230aresult1.xls"
    file = "E:\\o\\github_branch\\xls_read\\test\\test.xlsx"
    xls = pd.read_excel(file, 0)
    xlst = xls.T
