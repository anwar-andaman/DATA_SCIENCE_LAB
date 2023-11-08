# program to handle data using pandas
import pandas as pd
data=pd.read_csv('myData.csv')
print(data)
print("\nhead:\n",data.head())
print("\ntail:\n",data.tail())
print("With Duplicates*********************************************************************")
b=data.duplicated().any()
print(data)
print("After Dropping Duplicates*********************************************************************")
c=data.drop_duplicates()
print(c)
print("After converting to Dates*********************************************************************")
data['Date']=pd.to_datetime(data['Date'])
print(data)
print("Selecting specific value- fourth row, column Calories*********************************************************************")
b=data.loc[3,'Calories']
print(b)

print("cleaning empty cells*********************************************************************")
new_df = data.dropna()
print(new_df.to_string())

print("Remove all rows with NULL values*********************************************************************")
new_df.dropna(inplace = True)
print(new_df.to_string())
