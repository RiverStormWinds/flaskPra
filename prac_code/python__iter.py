class person:
    def __init__(self):
        self.l=[]
        self.count=0
        self.index=0

    def add_new(self,name,age):
        # personReal=dict(name,age)
        person_real={'name':name,'age':age}
        self.count=self.count+1
        self.l.append(person_real)

    # def __next__(self):
    #     print("__next__")
    #     if(self.index<self.count):
    #         self.index=self.index+1
    #         return self.l[self.index]

    def __iter__(self):
            return iter([self.index  , self.count])


if __name__ == '__main__':
    personS=person()
    personS.add_new("john",8)
    personS.add_new("jane",7)
    personS.add_new("Steve",9)

    for ps in personS:
        # print("ps.name =%s,ps.age=%d" % ps[name],ps.age)
        print(ps)
        # print(len(ps))
        # print(ps.keys())
        # for key in ps.keys():
            # print("key %s,ps[key]=%s" % (key,ps[key]))

