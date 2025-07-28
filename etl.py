# we are making some changes to cicd soon
print("this is a new script to load data")
df=pd.Dataframe('click')
df.reset_index(drop=True)
df.join(df1, on='key')
df.tocsv('df2.csv')
