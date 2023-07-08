# importing the modules
import pandas as pd
import re
  
# read specific columns of csv file using Pandas
df = pd.read_csv("ONSPD_MAY_2023_UK.csv", usecols = ['pcd','lsoa11', 'doterm'], dtype={"pcd": "string", "lsoa11": "string", "doterm": "string"})

print("csv read")

def func(code):
    short = code[:2]
    short = re.sub("\d","",short)
    return short

df["pcd"] = df["pcd"].apply(func) #shorten postcode

df = df[df["doterm"].isna()] #remove postcodes with terminated dates
df.drop_duplicates(inplace=True) #remove duplicate short postcode/output area pair
df = df[["pcd",'lsoa11']]

df.to_csv("compressed.csv", index=False)

print("done")

