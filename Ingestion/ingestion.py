import pandas as pd

def ingestion():
    df= pd.read_csv('walmart.csv')
    df.to_csv('dl/clean.csv',index=False)
    


    
