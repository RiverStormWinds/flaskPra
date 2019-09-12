# coding:utf-8

# import collections

# card = collections.namedtuple('card', ['rank', 'suit'])

# User = collections.namedtuple('User', ['name', 'age', 'id'])
# namedtuple('User', ['name', 'age', 'id'])，意为创建一个对象-->User，
# 此对象内部具有属性name, age, id
# user = [User(name, age, id)
#         for name in ['hwk', 'ztq', 'wj']
#         for age in ['25', '28', '24']
#         for id in ['111', '222', '333']]
# for i in user:
#     print(i)

# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()

#     def cards(self):
#         return self._cards

#     def __init__(self):
#         self._cards = [card(suit, rank) for suit in self.suits for rank in self.ranks]
#         self.names = {'H': 'hwk',
#                       'Z': 'ztq'}

#     def __len__(self):
#         return len(self._cards)

#     def __getitem__(self, item):
#         # return self.names[item]
#         return self._cards[item]

# fd = FrenchDeck()
# print(fd['H'])


class StrIter(str):
    def __new__(cls, *args, **kwargs):
        return super(StrIter, cls).__new__(cls, *args, **kwargs)

    def __init__(self, string):
        super(StrIter, self).__init__()
        self.string = string
        self.count = len(self.string)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.count = self.count - 1
            return self.string[self.count]
        except IndexError as e:
            return None

s = StrIter('hello world')

for i in s:
    print(i)















