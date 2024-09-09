import pandas as pd
import json

json_data = json.load(open("content/polls-nyt.json"))

json_dataframe = pd.DataFrame(json_data["polls"])

print(json_dataframe.columns)

csv_data = json_dataframe.to_csv("content/polls-nyt.csv", sep=',', encoding='utf-8') 