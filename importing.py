import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd

dff = pd.read_json("pokemonJSON.json")
print(dff)

df = pd.read_csv("pokemon_150.csv")
# print(df.to_string())
