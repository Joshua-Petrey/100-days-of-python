import pandas as pd

squirrel_data = pd.read_csv('./squirrel_data.csv')

# Define dictionary structure
myDict = {
    'Fur Color': ['Gray', 'Red', 'Black'],
    'count': [squirrel_data["Primary Fur Color"].value_counts()["Gray"],
    squirrel_data["Primary Fur Color"].value_counts()["Cinnamon"],
    squirrel_data["Primary Fur Color"].value_counts()["Black"]]
}

# turn dictionary to DataFrame
dictToDataFrame= pd.DataFrame(myDict)
print(dictToDataFrame)
