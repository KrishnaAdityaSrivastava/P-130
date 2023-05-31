import pandas as pd
import csv

data = pd.read_csv("final.csv")

del data["Star_name"]

data = data.dropna()

data.to_csv("data.csv")

