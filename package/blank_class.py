class Person():
    """A class to be a blank base for copying and pasting during the SC
        describes a person
        methods:
        ------------------------
        __init__(self,name:str,age:int,gender:str,income:float)->type(None)

        age_to_incomeR(self)->float
    """
    def __init__(self,
                 name: str = 'Undefined',
                 age: int = 0,
                 gender: str = 'NaN',
                 income: float = 0.0) -> type(None):

        self.name = name
        self.age = age
        self.gender = gender
        self.income = income

    def age_to_incomeR(self):
        return ((self.income - self.age) / self.income) * 100

    def split_name(self):
        if ' ' in self.name.strip():
            self.name_tokenized = self.name.split()
        else:
            raise ValueError("please specify a name that has a first and\
                 last name seperated by a space.\n\
                 e.g <first>.<last> where . == space")


if __name__ == '__main__':
    print("please run as a module with python -m <package name>")
    raise RuntimeError("Must Run As Module **See Logs For Usage**")
