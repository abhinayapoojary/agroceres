import pandas as pd
import os

def get_crop_types(crop):
    print("inside crop type" , crop)
    path = os.path.dirname(__file__) + '/csv_files/Agro_market_19_20_20.xlsx'
    df_agro_ts = pd.read_excel(path, header=None, delimiter=r"\s+")
    df_agro_ts.columns = ['Day', 'Month', 'Year', 'Commodity_Name', 'Variety_Name', 'Market_Name', 'Arrivals(Qtls)',
                          'Maximum', 'Minimum', 'Model', 'Purchase By']

    (df_agro_ts['Commodity_Name'].unique())

    df_agro_ts = df_agro_ts[df_agro_ts['Commodity_Name'] == crop]
    df_agro_ts.head(10)

    veg_type_name = (df_agro_ts['Variety_Name'].unique())

    print(veg_type_name)
    return veg_type_name
