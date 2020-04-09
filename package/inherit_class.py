from .blank_class import Person


class Employee(Person):
    def __init__(self, emp_id, standing, *args):
        super().__init__(*args)
        self.emp_id = emp_id
        self.standing = standing
