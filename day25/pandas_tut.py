# no library way to turn csv file into a list
data = []
with open('./weather_data.csv', 'r') as f:
    for line in f:
        data.append(line.strip())

print(data)


# using the csv library
import csv

temperatures = []
with open('./weather_data.csv', 'r') as data_file:
    # create csv reader object
    csv_object = csv.reader(data_file)

    # row is a list of all items on a single line
    for row in csv_object:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

print(temperatures)

# using pandas csv reader
import pandas

data3 = pandas.read_csv('./weather_data.csv')
#first row of csv is turned into column headers
#each row has a an index starting at 0
print(data3)
# column of data can be retreived by using column name.
print(data3['temp'])

# DataFrame data structure
print(type(data3))

# DataFrame has methods for checking size of the frame, indexing, re-indexing and iteration, performing statistical operations, reshaping resorting transposing the table,combining comparing merging tables, time-series related methods, plotting , serialzation i/o/ conversion

dict_data = data3.to_dict()
print(dict_data)


# Series


list_of_column_data = data3['condition'].to_list()
print(list_of_column_data)
#or , column headers are converted to attributes
print(data3.condition)

# find average of a series
print(f"The average temprature is {data3['temp'].mean()}")
#max value in series
print(f"The max temprature is {data3['temp'].max()}")

# get row data
print(data3[data3.day == 'Monday'])

# get row where the temp was the highest
hottest_day = data3[data3.temp == data3.temp.max()]
print(hottest_day)

# turn sundays temp to Farenheit
to_farenhiet = (hottest_day.temp * (9/5)) + 32
print(to_farenhiet)

# create Dataframe table from dict
myDict = {
    'students': ['amy', 'steve', 'pablo'],
    'grades': [56,45,99]
}
dataDict = pandas.DataFrame(myDict)

#Turn the DataFrame to a csv file
dataDict.to_csv('./A_csv_file_created_from_a_dictionary.csv')



# print the number of times value appears ina column
print(data3.condition.value_counts()['Sunny'])