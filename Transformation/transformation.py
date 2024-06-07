import pandas as pd

def transformation():
    cleandf  = pd.read_csv('dl/clean.csv')
    cleandf['Total_Purchase_Per_User'] = cleandf.groupby('User_ID')['Purchase'].transform('sum')
    cleandf['Product_Share'] = cleandf['Purchase'] / cleandf['Total_Purchase_Per_User']* 100
    finaldf = cleandf[cleandf['City_Category']== 'A']
    return finaldf

