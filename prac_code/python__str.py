# coding:utf-8
class InputText(object):
    def __str__(self):
        return "</input type='text'>"


class InputEmail(object):
    def __str__(self):
        return "</input type='email'"


class StringField():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)


class LoginForm():
    xyy = StringField(name=InputText())
    lw = StringField(name=InputEmail())


form = LoginForm()

print(form.lw, form.xyy)

