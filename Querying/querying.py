import pandas as pd

def get_people_above_30k(finaldf):
    return finaldf[finaldf['Total_Purchase_Per_User']>=30000].drop_duplicates('User_ID')

def get_repartion_F_H(finaldf):
    return finaldf[finaldf['Total_Purchase_Per_User']>=30000].drop_duplicates('User_ID')[['Gender','Age']].value_counts()


