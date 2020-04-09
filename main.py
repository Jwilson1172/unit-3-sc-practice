from package.inherit_class import Employee
# main cnonditional of the program, takes and passes stuff to the Employee
# object and prints some things that were passed, also executes
# the method to calculate the ratio between age and income
if __name__ == '__main__':
    joe = Employee('id-001', 3, 'joe', 25, 'm', 13556.0)
    tarrah = Employee('2', 3, 'tarrah', 27, 'f', 32000.00)
    lori = Employee('2', 3, 'lorri', 51, 'f', 12000.00)
    ed_calc = ((35000) + (((80 * 5) * 4) * 52))
    ed = Employee('2', 3, 'ed', 56, 'f', ed_calc)
    for emp in [joe, tarrah, lori, ed]:
        print(
            f"Employee id:{emp.emp_id}",
            f"Employee name:{emp.name}",
            f"Employee age:{emp.age}",
            f"Employee income to age ratio:%{round(-1*(emp.age_to_incomeR()-100),3)}\n",
            sep='\n')
