import pandas as pd 
df = pd.DataFrame({'artist':['A','B','C','C','C','A','B'],'venue':['Z','X','Y', 'Y','Z','X','Z'],'date':pd.to_datetime(['2024-01-10','2024-01-15','2024-01-20','2024-02-05','2024-02-20','2024-02-25','2024-03-01'])}) 
df['year_month']=df['date'].dt.to_period('M') 
artists=df[['artist']]
venues=df[['venue']]
cross=artists.merge(venues,how='cross') 
grouped=(df.groupby(['year_month','artist','venue']).size().rename('count').reset_index()) 
all_months=df[['year_month']].drop_duplicates() 
full_index=all_months.merge(cross,how='cross') 
full_data=(full_index.merge(grouped,on=['year_month','artist','venue'],how='left').fillna(0)) 
pivot=full_data.pivot_table(index='year_month',columns=['artist','venue'],values='count',fill_value=0) 
pivot.columns=['_'.join(col).strip() for col in pivot.columns.values]
print(pivot) 