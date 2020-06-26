import pandas as pd
import webbrowser
import os

def prt(merge):
    bang = merge.index.tolist()
    num = len(bang)
    print(num)
    for z in range(num):
        DAY = (merge.loc[bang[z], 'Day'])
        MONTH = (merge.loc[bang[z], 'Month'])
        YEAR = (merge.loc[bang[z], 'Year'])
        COM_NAME = (merge.loc[bang[z], 'Commodity_Name'])
        VAR_NAME = (merge.loc[bang[z], 'Variety_Name'])
        MAR = (merge.loc[bang[z], 'Market_Name'])
        MAX = (merge.loc[bang[z], 'Maximum'])
        MIN = (merge.loc[bang[z], 'Minimum'])
        MOD = (merge.loc[bang[z], 'Model'])
        DIST = (merge.loc[bang[z], 'Distric'])
        LAT = str(merge.loc[bang[z], 'latitude'])
        LON = str(merge.loc[bang[z], 'logitude'])

        return "Date", DAY, MONTH, YEAR,"Crop and its type", COM_NAME, VAR_NAME,"\nMarket Name", MAR, "Max value",MAX, "\nMin value",MIN,"\nModel value", MOD,"\nDistrict", DIST
        webbrowser.open('https://maps.googleapis.com/maps/api/staticmap?zoom=12&size=640x640&maptype=roadmap&markers=size:mid|color:red|' + LAT + ',' + LON + '&key=your_api_key')


def get_result(district):
    path1 = os.path.dirname(__file__) + '/csv_files/market distric of telengana.xlsx'
    df_agro_tsm = pd.read_excel(path1, header=None, delimiter=r"\s+")
    df_agro_tsm.columns = ['Market_Name', 'Distric', 'latitude', 'logitude']
    df_agro_tsm.head(20)

    file = open('agrots.txt', 'r')

    df_agro_ts = file.read()

    merge = pd.merge(df_agro_ts, df_agro_tsm, on='Market_Name')
    merge.head()
    merge = merge[merge['Distric'] == district]
    result = prt(merge)
    merge.head(10)
    return result
