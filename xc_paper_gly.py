import pandas as pd
from scipy import stats

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

    #ttest equals T.TEST(a,b,2,3) in EXCEL which is two tail ,two sample unequal variance)

    ctrl_val = list(ctrl["GluA1-MA"])
    gly_val = list(gly["GluA1-MA"])
    print(stats.ttest_ind(ctrl_val, gly_val, equal_var=False))
    print(stats.ttest_ind([1,1,1.2], [20,20,19.9], equal_var=False))
