import pandas as pd

# reads in csv as pandas df
df = pd.read_csv('D:/TH_Koeln/WS21-22/Bachelorarbeit/python_scripts/venv_scrapy-requests/get_DOIs/get_DOIs/article_DOIs.csv') 
print(df) # the dataframe has 1,380 lines As of 03/29/2022, 5:44 p.m.

# DOIs that are on the same line are separated by a comma and each DOI is written on a separate line
df=df.assign(doi=df.doi.str.split(",")).explode('doi')
print(df) # the dataframe now has 23,321 lines

# removes duplicate DOIs
df = df.drop_duplicates(subset='doi', keep='first')
print(df) # the dataframe now has 17,006 lines

# saves dataframe to csv
df.to_csv('cleaned_article_DOIs.csv')