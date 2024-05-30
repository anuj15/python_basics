# import random
#
#
# print(0 % 26)
# print(-1 % 26)
#
# # check if we can sort a dict
# dict_auction = {"a": 1, "b": 22, "c": 33, "d": 4}
# print(dict_auction)
# print(sorted(dict_auction, reverse=True))
#
#
# def new_func(parameter):
#     print(f'Parameter: {parameter}')
#
#
# new_func(parameter="Argument")
#
# data = [
#     {
#         'fc': 346,
#     },
#     {
#         'fc': 215,
#     },
#     {
#         'fc': 183,
#     },
# ]
# a = random.choice(data)
# print(a)
# b = random.choice(data)
# while a == b:
#     b = random.choice(data)
# print(b)

class Al:

    def a(self):
        print('a is called')

    def b(self):
        print('b is called')

    def c(self):
        print('c is called')

    def d(self, func):
        func()


al = Al()
al.d(al.c)
