import pandas as pd
import os

def get_crop_district(crop_type):
    print("inside crop distrits" , crop_type)
    path = os.path.dirname(__file__) + '/csv_files/Agro_market_19_20_20.xlsx'

    df_agro_ts = pd.read_excel(path, header=None, delimiter=r"\s+")
    df_agro_ts.columns = ['Day', 'Month', 'Year', 'Commodity_Name', 'Variety_Name', 'Market_Name', 'Arrivals(Qtls)',
                          'Maximum', 'Minimum', 'Model', 'Purchase By']

    df_agro_ts = df_agro_ts[df_agro_ts['Variety_Name'] == crop_type]
    df_agro_ts.head(10)

    with open('agrots.txt', 'w') as textfile:
        textfile.write(df_agro_ts)

    # uploaded = files.upload()
    path1 = os.path.dirname(__file__) + '/csv_files/market distric of telengana.xlsx'
    df_agro_tsm = pd.read_excel(path1, header=None, delimiter=r"\s+")
    df_agro_tsm.columns = ['Market_Name', 'Distric', 'latitude', 'logitude']
    df_agro_tsm.head(20)

    merge = pd.merge(df_agro_ts, df_agro_tsm, on='Market_Name')
    merge.head()
    # prt()

    distic_name = (merge['Distric'].unique())

    print(distic_name)
    return distic_name
