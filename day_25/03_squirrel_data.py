import pandas

# read csv
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# create list from series
colors = data['Primary Fur Color'].dropna().to_list()

# remove duplicates from list
color_list = list(set(colors))

# create list from series
color_count = [colors.count(x) for x in color_list]

# create dict from lists
color_dict = {'Fur Color': color_list, 'Count': color_count}

# create data frame from dict
data_f = pandas.DataFrame(color_dict)

# create csv from data frame
data_f.to_csv('squirrel_data.txt')
