
import pandas as pd
new_df = df.copy()
def prettify(cls, n, df):
    for index, records in df.iloc[n].iterrows():
        for cols in df.columns:
            records[cols] = cls[cols][0][records[cols]]
        new_df

