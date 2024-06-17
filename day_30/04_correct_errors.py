# fruits = ['apple', 'pear', 'orange']
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + 'pie')
#     except IndexError:
#         print('Fruit Pie')
#     except TypeError:
#         print('Fruit Pie')
#
#
# make_pie('test')

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]
total_likes = 0
for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        pass

print(total_likes)
