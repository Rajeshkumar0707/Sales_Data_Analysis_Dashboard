import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('sheet.csv',header=1)
#top 5 rows
print('top 5 rows')
print(df.head())
#dataframe info
print('dataframe info')
print(df.info())
#column names
print('column names')
print(df.columns)
#null value sum
print('sum of null values')
print(df.isnull().sum())
#data types
print('data types')
print(df.dtypes)
# duplicate removes

df = df.drop_duplicates()
# missing values

df = df.dropna()
#summary statistics
print('summary statistics')
print(df.describe())

#fix date column

df['Order_Date']=pd.to_datetime(df['Order_Date'], errors='coerce')
#drop Orderdate

df=df.dropna(subset=['Order_Date'])
# creating Profit column

df['Profit'] = df['Sales'] - df['Cost']
# Adding Year & Month columns

df['Year'] = df['Order_Date'].dt.year   
df['Month'] = df['Order_Date'].dt.month
# final converting Cleaned data to csv
print('converting cleaned data to csv')
df.to_csv('sales_sheet.csv', index=False)
print(df)

df=pd.read_csv('sales_sheet.csv')
engine =create_engine('mysql+pymysql://root:root@localhost:3306/salesdb')
df.to_sql(name='sales_data',con=engine,if_exists='replace',index=False)