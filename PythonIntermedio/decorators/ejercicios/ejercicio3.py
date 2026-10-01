from datetime import date, datetime

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = datetime.strptime(date_of_birth,"%d/%m/%Y").date()

    @property
    def age(self):
        years = date.today() - self.date_of_birth
        return int(years.days // 365.25)


def adult_only(func):
    def wrapper(user, *args):
        if user.age < 18:
            raise ValueError("El usuario debe ser mayor de edad")

        return func(user, *args)
    return wrapper

@adult_only
def buy_alcohol(user):
    return "Compra autorizada"

adulto = User("04/04/1997")
menor = User("10/05/2015")

print("old: " , buy_alcohol(adulto))
print("young: ", buy_alcohol(menor)) 