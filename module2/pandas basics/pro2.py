import pandas as pd
da=pd.read_csv('2.csv')
df=pd.DataFrame(da)
average=df['Math_Score'].mean()
maxmium=df['Science_Score'].max()
df['Total_Score'] = df['Math_Score'] + df['Science_Score']
highest_total_score_row = df[df['Total_Score'] == df['Total_Score'].max()]
highest_total_score_name = highest_total_score_row['Name'].values[0]
print(f"Student with the Highest Total Score: {highest_total_score_name}")
print(f'average marks of maths is {average}')
print(f'highest score of science is {maxmium}')
