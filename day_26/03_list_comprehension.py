def get_data(file):
    with open(file) as f:
        data = f.readlines()
        return [x.strip('\n') for x in data]


data1 = get_data('file1.txt')
data2 = get_data('file2.txt')
data3 = [int(x) for x in data1 if x in data2]
print(data3)
