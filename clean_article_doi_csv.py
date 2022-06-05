import pandas as pd

df = pd.read_csv('D:/TH_Koeln/WS21-22/Bachelorarbeit/python_scripts/venv_scrapy-requests/get_DOIs/get_DOIs/article_DOIs.csv') 
print(df) # Der Dataframe hat 1.380 Zeilen Stand 29.03.2022, 17:44 Uhr

# DOIs, die gemeinsam in einer Zeile stehen werden am komma getrennt und jede DOI wird in eine eigene Zeile geschrieben
df=df.assign(doi=df.doi.str.split(",")).explode('doi')
print(df) # Der Dataframe hat nun 23.321 Zeilen

# Doppelte DOIs werden entfernt
df = df.drop_duplicates(subset='doi', keep='first')
print(df) # Der Dataframe hat nun 17.006 Zeilen

df.to_csv('cleaned_article_DOIs.csv')