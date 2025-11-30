import pandas as pd

df = pd.read_csv("studenci.csv")

df["rok_urodzenia"] = 2025 - df["wiek"]


print(df)



# print(f"Średnia: {df["wiek"].mean():.2f}")
# print(f"Mediana: {df["wiek"].median():.2f}")
# print(f"Min: {df["wiek"].min():.2f}")
# print(f"Max: {df["wiek"].max():.2f}")
# print(f"Suma: {df["wiek"].sum():.2f}")
#

