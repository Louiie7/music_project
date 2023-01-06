from genre import getGenre
from load import load_xlsx, load_csv
df = load_csv("data/data_cleaned.csv")

getGenre(df)