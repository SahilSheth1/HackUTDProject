import pandas as pd

filePath = ("HackUTD-2023-HomeBuyerInfo.csv")

df = pd.read_csv(filePath)
df.head()