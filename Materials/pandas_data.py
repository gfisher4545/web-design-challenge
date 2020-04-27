import pandas as pd


cities_data = pd.read_csv("cities.csv")
print(cities_data.to_html(buf= "cites_path.txt"))

