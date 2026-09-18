class Bus:
    def __init__(self, max_passengers):
        self.passenger_list = []
        self.max_passengers = max_passengers

    def add_passenger(self, person):
        if len(self.passenger_list)< self.max_passengers:
            self.passenger_list.append(person)
            print("Bienvenido, pase adelante")
        else:
            print("El Bus se encuentra lleno...")

    def remove_passenger(self):
        self.passenger_list.pop()

    def get_list_passengers(self):
         for person in self.passenger_list:
              print(person.name)

class Person():
	def __init__(self, name):
		self.name = name

my_party_bus = Bus(4)
my_party_bus.add_passenger(Person("Wilkin"))
my_party_bus.add_passenger(Person("Peter"))
my_party_bus.add_passenger(Person("Mar"))
my_party_bus.add_passenger(Person("Pepe"))
my_party_bus.add_passenger(Person("Mario"))
print("===== Lista de pasageros =====")
my_party_bus.get_list_passengers()
my_party_bus.remove_passenger()
print("===== Lista de pasageros =====")
my_party_bus.get_list_passengers()