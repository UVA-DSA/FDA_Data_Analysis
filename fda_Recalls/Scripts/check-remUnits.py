import pandas as pd
import re
import numpy as np

def check_remUnits(filename):
    df = pd.read_excel(filename)
    numlist = ['num1','num2','num3']
    df['num1'] = 0
    df['num2'] = 0
    df['num3'] = 0
    df["diff"] = np.nan
    for i in range(len(df)):
        String = str(df["Quantity in Commerce"][i]).replace(',','')
        String = String.replace('.','').replace('-','').replace(' ','')
        String_Seq = re.findall("\d+",String)
        for i_seq in range(min(3,len(String_Seq))):
            df[numlist[i_seq]][i] = int(String_Seq[i_seq])

        df["diff"][i]= df["Clean Quantity"][i].astype(int) - df['num1'][i]-df['num2'][i]-df['num3'][i]
        if df["Clean Quantity"][i].astype(int) == df['num1'][i] and'OUS' not in String:
            df["diff"][i] = 0
        
    df.to_excel(filename)

if __name__ == "__main__":
    for year in range(2007,2017):
        UniqueFile = "../Unique_Data/unique{}.xls".format(year)
        check_remUnits(UniqueFile)