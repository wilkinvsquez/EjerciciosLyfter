class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def name(self)-> str:
        return self.__name
    
    @property
    def salary(self)-> str:
        return self.__salary

    @salary.setter
    def salary(self, value : float) -> None:
        if value < 0:
            raise ValueError("El salario no puede ser negativo")
        self.__salary = value

    def promote(self, percentaje):
        self.__salary = self.__salary + (self.__salary * percentaje)

employee = Employee("Ana", 1000)
employee.promote(0.1)  # +10%
print(employee.salary)  # 1100.0