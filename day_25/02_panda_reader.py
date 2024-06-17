import pandas

data = pandas.read_csv('weather_data.csv')

# data frame
print(type(data))

# series
print(type(data['temp']))

# data frame to dictionary
data_dict = data.to_dict()
print(data_dict)

# series to list
data_list = data['temp'].to_list()
print(data_list)

# inbuilt series methods
print(data['temp'].mean())
print(data['temp'].max())

# get temp column data
print(data['temp'])
print(data.temp)

# get row where day is Monday
mon_row = data[data.day == 'Monday']
print(mon_row)

# get row where temp is max
max_temp_row = data[data.temp == data.temp.max()]
print(max_temp_row)

# get temp where day is Monday and convert it in Fahrenheit
mon_temp = data[data.day == 'Monday'].temp[0]
mon_temp = mon_temp * 9 / 5 + 32
print(mon_temp)

# create dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65],
}
data = pandas.DataFrame(data_dict)
print(data)

# create csv from data frame
data.to_csv('student_score.csv')
