##Assignment(3)-Pandas

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r'C:\Users\MOG MOG\Downloads\archive (2)\shopping_trends.csv')

pd.set_option('display.max_columns',None)


# print(df.head())
# print()
# print(df.tail())
# print()
# print(df.info())
# print()
# print(df.describe())
# print()
# print(df.describe(include='O'))
# print()
# print(df.duplicated().sum())
# print()
# print(df.isna().sum())

# print((df['Purchase Amount (USD)'].mean()).round(2))

expensive_thing =df['Purchase Amount (USD)'].max()
# print(expensive_thing)

index_expensive_thing=df[df['Purchase Amount (USD)']==expensive_thing ]
# print(index_expensive_thing)

counts_size=df['Size'].value_counts()
# print(counts_size)

item_purchased=index_expensive_thing['Item Purchased'].value_counts()
# print(item_purchased)

# sns.histplot(df,x='Item Purchased',bins=10,color='blue',kde=False)
# plt.xticks(rotation=70)
# plt.show()

Location=df['Location'].value_counts()
# print(Location)

Season=df['Season'].value_counts()
# print(Season)

# Season.plot.pie(autopct='%1.1f%%',figsize=(6,6),title='season distribution ')
# plt.show()


Payment_Method=df['Payment Method'].value_counts()
# print(Payment_Method)

# Payment_Method.plot.pie(autopct='%1.1f%%',figsize=(6,6),title='Payment Method ')
# plt.show()

Shipping_Type=df['Shipping Type'].value_counts()
# print(Shipping_Type)

# Shipping_Type.plot.pie(autopct='%1.1f%%',figsize=(6,6),title='Shipping Type distribution ')
# plt.ylabel('')
# plt.show()

Color=df['Color'].value_counts()
# print(Color)

# Color.plot.pie(autopct='%1.1f%%',figsize=(10,10),title='Color Distribution')
# plt.ylabel('')
# plt.show()

pivot=df.pivot_table(index='Item Purchased',values='Purchase Amount (USD)',aggfunc=['max','min','mean'])
# print(pivot)
#######
most_review_rating=df['Review Rating'].max()
# print(most_review_rating)

df['Promo Code Used']=df['Promo Code Used'].map({'Yes':1,'No':0})
df['Subscription Status']=df['Subscription Status'].map({'Yes':1,'No':0})
# print(df)


df['Discount && Promo Code']=df['Discount Applied']
# print(df)

with pd.ExcelWriter('Assignment(3)_pandas.xlsx') as writer:
    df.to_excel(writer,sheet_name='main_table')
    pivot.to_excel(writer,sheet_name='pivot')
    item_purchased.to_excel(writer,sheet_name='item_purchased counts')
    Color.to_excel(writer,sheet_name='Color counts')
    Shipping_Type.to_excel(writer,sheet_name='Shipping_Type counts')
    Location.to_excel(writer,sheet_name='Location counts')
    Payment_Method.to_excel(writer,sheet_name='Payment_Method counts')
    Season.to_excel(writer,sheet_name='Season counts')
    
    