import csv
import pandas as pd
df = pd.read_csv("clean.csv")
print(df.shape)

del df["Luminosity"]

df = df.rename({
    'Radius' : "Radius of the planet"
}, axis = 'columns')

print (list(df))
df.to_csv('main.csv')
