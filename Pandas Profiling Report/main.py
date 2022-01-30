import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv(r'C:\Users\Aamash\Desktop\Data Analysis  And Scrapping Projects\Weather Data Analysis By Aamash Khan\Weather Data.csv')
print(df)
#Generate a report
profile=ProfileReport(df)
profile.to_file(output_file="Weather.html")
