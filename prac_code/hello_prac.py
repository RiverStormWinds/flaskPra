# coding:utf-8


class Foo():
    def __init__(self):
        self.value = {
            'n1': 'hwk',
            'n2': 'sh'
        }

        # for k, v in self.value.items():
        print(self.value)
        for k, v in self.value.items():
            setattr(self, k, v)


f = Foo()
print(f.n1)

