def prt():
    bang= merge.index.tolist()
    num = len(bang)
    print(num)
    for z in range (num):
        DAY = ( merge.loc[bang[z],'Day'])
        MONTH =( merge.loc[bang[z],'Month'])
        YEAR =( merge.loc[bang[z],'Year'])
        COM_NAME =( merge.loc[bang[z],'Commodity_Name'])
        VAR_NAME = ( merge.loc[bang[z],'Variety_Name'])
        MAR = ( merge.loc[bang[z],'Market_Name'])
        MAX = ( merge.loc[bang[z],'Maximum'])
        MIN = ( merge.loc[bang[z],'Minimum'])
        MOD = ( merge.loc[bang[z],'Model'])
        DIST = ( merge.loc[bang[z],'Distric'])
        LAT = str( merge.loc[bang[z],'latitude'])
        LON = str( merge.loc[bang[z],'logitude'])
        print(DAY,MONTH,YEAR,COM_NAME,VAR_NAME,MAR,MAX,MIN,MOD,DIST,LAT,LON)
        webbrowser.open('https://maps.googleapis.com/maps/api/staticmap?zoom=12&size=640x640&maptype=roadmap&markers=size:mid|color:red|'+LAT+','+LON+'&key=AIzaSyAnyLkZp1r7mBv99wE3stsTv0tzuUcF3Bw')
        
       
import pandas as pd
import plotly.express as px
import webbrowser

path = './Agro_market_19_20_20.xlsx'
df_agro_ts = pd.read_excel(path,header=None,delimiter=r"\s+")
df_agro_ts.columns = ['Day','Month','Year','Commodity_Name','Variety_Name',	'Market_Name','Arrivals(Qtls)','Maximum','Minimum','Model','Purchase By']

veg_name=(df_agro_ts['Commodity_Name'].unique())
x=(len(veg_name))
print(x)

print("Select crop number")
for i in range(x):
  print(i+1,'.',veg_name[i])

y = int(input())
z = str(veg_name[y-1])
print(z)
df_agro_ts = df_agro_ts[df_agro_ts['Commodity_Name']==z]
df_agro_ts.head(10)

veg_type_name=(df_agro_ts['Variety_Name'].unique())
xa=(len(veg_type_name))
print(xa)

print("Select crop type number")
for j in range(len(veg_type_name)):
  print(j+1,'.',veg_type_name[j])

r = int(input())
s = str(veg_type_name[r-1])
print(s)
df_agro_ts = df_agro_ts[df_agro_ts['Variety_Name']==s]
df_agro_ts.head(10)

#uploaded = files.upload()
path1 = './market distric of telengana.xlsx'
df_agro_tsm = pd.read_excel(path1,header=None,delimiter=r"\s+")
df_agro_tsm.columns = ['Market_Name','Distric','latitude','logitude']
df_agro_tsm.head(20)

merge=pd.merge(df_agro_ts,df_agro_tsm,on='Market_Name')
merge.head()
# prt()

distic_name=(merge['Distric'].unique())
xa=(len(distic_name))
print(xa)

print("Select distric name")
for j in range(len(distic_name)):
  print(j+1,'.',distic_name[j])

q = int(input())
u = str(distic_name[q-1])
print(s)
merge = merge [merge ['Distric']==u]
prt()
merge.head(10)
