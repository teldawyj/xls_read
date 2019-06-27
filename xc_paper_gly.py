import pandas as pd

if __name__ == "__main__":
    # file = "E:\\o\\github_branch\\xls_read\\data\\day170230aresult1.xls"
    file = "E:\\o\\github_branch\\xls_read\\data\\day170230aresult1_test.xls"
    xls = pd.read_excel(file, 0)

    ctrl = xls[xls["path.1"] == "/ctrl"]
    gly = xls[xls["path.1"] == "/ctrl-gly"]

    # std is equal to STDEV.S in EXCEL, (sum(x-x.mean)^2/(n-1))^0.5

    print("ctrl-NR2B ,\tmean = ", ctrl["NR2B MA"].mean(),
          " \tstd = ", ctrl["NR2B MA"].std())

    print("ctrl-GluA1,\tmean = ", ctrl["GluA1-MA"].mean(),
          " \tstd = ", ctrl["GluA1-MA"].std())

    print("gly-NR2B, \tmean = ", gly["NR2B MA"].mean(),
          " \tstd = ", gly["NR2B MA"].std())

    print("gly-GluA1, \tmean = ", gly["GluA1-MA"].mean(),
          " \tstd = ", gly["GluA1-MA"].std())