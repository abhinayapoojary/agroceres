import pandas as pd
import matplotlib.pyplot as plt
import os

def process_mandal(mandal):
    path1 = os.path.dirname(__file__) + '/csv_files/adilabad_kharif_2016-17_2.csv'
    df1 = pd.read_csv(path1)

    path2 = os.path.dirname(__file__) + '/csv_files/adilabad_kharif_2017-18_0.csv'
    df2 = pd.read_csv(path2)

    path3 = os.path.dirname(__file__) + '/csv_files/adilabad_kharif_2018-19_0.csv'
    df3 = pd.read_csv(path3)

    path4 = os.path.dirname(__file__) + '/csv_files/adilabad_rabi_2016-17.csv'
    df4 = pd.read_csv(path4)

    path5 = os.path.dirname(__file__) + '/csv_files/adilabad_rabi_2017-18.csv'
    df5 = pd.read_csv(path5)

    path6 = os.path.dirname(__file__) + '/csv_files/adilabad_rabi_2018-19.csv'
    df6 = pd.read_csv(path6)

    df_1 = df1.append(df2, ignore_index=True)
    df_2 = df2.append(df3, ignore_index=True)
    df_3 = df3.append(df4, ignore_index=True)
    df_4 = df4.append(df5, ignore_index=True)
    df_5 = df5.append(df6, ignore_index=True)

    print(df_5)

    df_crop_min = df_5.groupby(['crop'])['actual_area'].min().reset_index()
    df_crop_min = df_crop_min.sort_values(by='crop')
    df_crop_max = df_5.groupby(['crop'])['actual_area'].max().reset_index()
    df_crop_max = df_crop_max.sort_values(by='crop')

    df_crop_max = df_crop_max[df_crop_max['actual_area'] != 0]
    print(df_crop_max)

    df_5 = df_5[df_5['mandal_name'] == mandal]
    print(df_5.head(10))

    df_crop = df_5.groupby('crop')['actual_area'].mean()
    df_crop = pd.DataFrame(df_crop).reset_index()

    print(df_crop)

    result = pd.merge(df_crop, df_crop_max, on='crop')
    print(result)

    result['percentage_growth'] = (result['actual_area_x'] / result['actual_area_y']) * 100.00
    print(result)

    global lt1
    lt1 = result["percentage_growth"]
    global lt2
    lt2 = result["crop"]

    plt.bar(lt2, lt1, color=['green'])
    plt.xticks(rotation=90)
    plt.title('Growth map')
    plt.subplots_adjust(bottom=0.3)
    plt.savefig(os.path.dirname(__file__) + '/graphs/mandal_graph.png')
    # plt.show()
