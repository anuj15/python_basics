# Program to practice lists
line_1 = ['__', '__', '__']
line_2 = ['__', '__', '__']
line_3 = ['__', '__', '__']
treasure_map = [line_1, line_2, line_3]
print('Hide your treasure. X marks the position.')
pos = input('Where do you want to put the treasure?\nOptions: A1, A2, A3\nB1, B2, B3\nC1, C2, C3\n')
row = int(pos[1]) - 1
col = ['a', 'b', 'c'].index(pos[0].lower())
treasure_map[row][col] = 'X'
print(f'{line_1}\n{line_2}\n{line_3}')
