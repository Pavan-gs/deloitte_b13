# we are making some changes to cicd soon
print("this is a new script to load data")
df1=pd.Dataframe('click')
df1.reset_index(drop=True)
df1.join(df1, on='key')
df1.tocsv('df2.csv')
# just one last comment
