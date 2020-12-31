import pandas as pd

squirrel_data = pd.read_csv('./squirrel_data.csv')

myDict = {
    'Fur Color': ['Gray', 'Red', 'Black'],
    'count': [squirrel_data["Primary Fur Color"].value_counts()["Gray"],
    squirrel_data["Primary Fur Color"].value_counts()["Cinnamon"],
    squirrel_data["Primary Fur Color"].value_counts()["Black"]]
}

dictToDataFrame= pd.DataFrame(myDict)
print(dictToDataFrame)
