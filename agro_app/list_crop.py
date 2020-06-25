import pandas as pd
import os

def list_crop():
    path = os.path.dirname(__file__) + '/csv_files/Agro_market_19_20_20.xlsx'
    df_agro_ts = pd.read_excel(path, header=None, delimiter=r"\s+")
    df_agro_ts.columns = ['Day', 'Month', 'Year', 'Commodity_Name', 'Variety_Name', 'Market_Name', 'Arrivals(Qtls)',
                          'Maximum', 'Minimum', 'Model', 'Purchase By']

    veg_name = (df_agro_ts['Commodity_Name'].unique())
    return veg_name
