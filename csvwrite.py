import yfinance as yf
import pandas as pd


#download data
data = yf.download ("PLTR.MX", start="2024-08-25", end="2025-05-12")
print(data.head())
print(data.tail())

#data to dataframe
df=pd.DataFrame(data)

cols= df.columns
for x in range(len(cols)):
	df[cols[x]] = df[cols[x]].astype(float)

df.info()

#save to csv
df.to_csv('pltr.csv')

#Quitar columnas

df_1 = df.drop(columns=['Close','High','Low','Volume'])

df_1.info()

#Guardar limpio

df_1.to_csv('pltr_limp.csv')
