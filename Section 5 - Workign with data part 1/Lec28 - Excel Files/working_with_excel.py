import pandas as pd
import openpyxl

xlsfile=pd.ExcelFile("Lec_28_test.xlsx")
dframe=xlsfile.parse("Sheet1")
print(dframe)
