from ORM.orm import ORM

'''
class ClassName(ORM):
    def __init__(self):
        pass

'''

class Students(ORM):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        pass
    pass
