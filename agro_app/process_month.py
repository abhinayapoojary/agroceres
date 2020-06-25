import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import os

def plot_graph():
    plt.bar(l1, l2)
    plt.xticks(rotation=90)
    plt.title('Growth map')
    plt.subplots_adjust(bottom=0.3)
    plt.savefig(os.path.dirname(__file__) + '/graphs/season_graph.png')
    plt.show()

def out_rabi(df_3):
    bang = df_3.index.tolist()
    num = len(bang)
    global l1
    l1 = df_3['Crop']
    global l2
    l2 = df_3['percentage_rabi_growth']
    print(num)
    for z in range(num):
        CROP = (df_3.loc[bang[z], 'Crop'])
        AREA = (df_3.loc[bang[z], 'Area Rabi'])
        AREA_TOL = (df_3.loc[bang[z], 'Area Total'])
        PROD = (df_3.loc[bang[z], 'Production Rabi'])
        PROD_TOL = (df_3.loc[bang[z], 'Production Total'])
        YEILD = (df_3.loc[bang[z], 'Yeild Rabi'])
        YETLD_TOL = (df_3.loc[bang[z], 'Yeild Total'])
        PER = (df_3.loc[bang[z], 'percentage_rabi_growth'])
        print(CROP, PER)
    plot_graph()

def out_karif(df_3):
    bang = df_3.index.tolist()
    num = len(bang)
    print(num)
    global l1
    l1 = df_3['Crop']
    global l2
    l2 = df_3['percentage_karif_growth']
    for z in range(num):
        CROP = (df_3.loc[bang[z], 'Crop'])
        AREA = (df_3.loc[bang[z], 'Area Kharif'])
        AREA_TOL = (df_3.loc[bang[z], 'Area Total'])
        PROD = (df_3.loc[bang[z], 'Production Kharif'])
        PROD_TOL = (df_3.loc[bang[z], 'Production Total'])
        YEILD = (df_3.loc[bang[z], 'Yeild Kharif'])
        YETLD_TOL = (df_3.loc[bang[z], 'Yeild Total'])
        PER = (df_3.loc[bang[z], 'percentage_karif_growth'])
        print(CROP, PER)
    plot_graph()

def process_month(month, day):
    result = ""
    day = int(day)
    month = int(month)
    
    path1 = os.path.dirname(__file__) + '/csv_files/cash_crop.csv'
    df1 = pd.read_csv(path1)

    path2 = os.path.dirname(__file__) + '/csv_files/Cereals_Millets.csv'
    df2 = pd.read_csv(path2)

    path3 = os.path.dirname(__file__) + '/csv_files/oil_seed.csv'
    df3 = pd.read_csv(path3)

    path4 = os.path.dirname(__file__) + '/csv_files/Pulses.csv'
    df4 = pd.read_csv(path4)

    df_1 = df1.append(df2, ignore_index=True)
    # df_1.reset_index(drop=True)
    df_2 = df_1.append(df3, ignore_index=True)
    # df_1.append(df3, ignore_index=True)
    df_3 = df_2.append(df4, ignore_index=True)
    # df_2.append(df4, ignore_index=True)

    # df_3.to_csv('dum.csv')

    df_3 = df_3.replace('N', 0)
    df_3['percentage_karif_growth'] = (df_3['Yeild Kharif'] / df_3['Yeild Total']) * 100.00
    df_3['percentage_rabi_growth'] = (df_3['Yeild Rabi'] / df_3['Yeild Total']) * 100.00

    lst_rabi = [4, 3, 2, 1, 0]
    lst_karif = [3, 2, 1, 0]

    if month == 10:
        rem_day = 31 - day
        result = "Optimum result within:", lst_rabi[0], " month", rem_day, "  days"
        df_3.drop(["Area Kharif", "Production Kharif", "Yeild Kharif", "percentage_karif_growth"], axis=1, inplace=True)
        df_3 = df_3[df_3['percentage_rabi_growth'] >= 10]
        out_rabi(df_3)
    if month == 11:
        rem_day = 31 - day
        result = "Optimum result within:", lst_rabi[1], " month", rem_day, "  days"
        df_3.drop(["Area Kharif", "Production Kharif", "Yeild Kharif", "percentage_karif_growth"], axis=1, inplace=True)
        df_3 = df_3[df_3['percentage_rabi_growth'] >= 10]
        out_rabi(df_3)
    if month == 12:
        rem_day = 31 - day
        result = "Optimum result within:", lst_rabi[2], " month", rem_day, "  days"
        df_3.drop(["Area Kharif", "Production Kharif", "Yeild Kharif", "percentage_karif_growth"], axis=1, inplace=True)
        df_3 = df_3[df_3['percentage_rabi_growth'] >= 10]
        out_rabi(df_3)
    if month == 1:
        rem_day = 31 - day
        result = "Optimum result within:", lst_rabi[3], " month", rem_day, "  days"
        df_3.drop(["Area Kharif", "Production Kharif", "Yeild Kharif", "percentage_karif_growth"], axis=1, inplace=True)
        df_3 = df_3[df_3['percentage_rabi_growth'] >= 10]
        out_rabi(df_3)
    if month == 2:
        rem_day = 31 - day
        result = ("Optimum result within:", lst_rabi[4], " month", rem_day, "  days")
        df_3.drop(["Area Kharif", "Production Kharif", "Yeild Kharif", "percentage_karif_growth"], axis=1, inplace=True)
        df_3 = df_3[df_3['percentage_rabi_growth'] >= 10]
        out_rabi(df_3)
    if month == 3:
        result = "Recommend not to seed or plant, start from July"
    if month == 4:
        result = "Recommend not to seed or plant, start from July"
    if month == 5:
        result = "Recommend not to seed or plant, start from July"
    if month == 6:
        result = "Recommend not to seed or plant, start from July"
    if month == 7:
        rem_day = 31 - day
        result = "Optimum result within:", lst_karif[0], " month", rem_day, "  days"
        df_3.drop(["Area Rabi", "Production Rabi", "Yeild Rabi", "percentage_rabi_growth"], axis=1, inplace=True)
        df_3 = df_3[df_3['percentage_karif_growth'] >= 10]
        out_karif(df_3)
    if month == 8:
        rem_day = 31 - day
        result = "Optimum result within:", lst_karif[1], " month", rem_day, "  days"
        df_3.drop(["Area Rabi", "Production Rabi", "Yeild Rabi", "percentage_rabi_growth"], axis=1, inplace=True)
        df_3 = df_3[df_3['percentage_karif_growth'] >= 10]
        out_karif(df_3)
    if month == 9:
        rem_day = 31 - day
        result = "Optimum result within:", lst_karif[2], " month", rem_day, "  days"
        df_3.drop(["Area Rabi", "Production Rabi", "Yeild Rabi", "percentage_rabi_growth"], axis=1, inplace=True)
        df_3 = df_3[df_3['percentage_karif_growth'] >= 10]
        out_karif(df_3)
    if month == 10:
        rem_day = 31 - day
        result = "Optimum result within:", lst_karif[3], " month", rem_day, "  days"
        df_3.drop(["Area Rabi", "Production Rabi", "Yeild Rabi", "percentage_rabi_growth"], axis=1, inplace=True)
        df_3 = df_3[df_3['percentage_karif_growth'] >= 10]
        out_karif(df_3)

    print(result)

    return result