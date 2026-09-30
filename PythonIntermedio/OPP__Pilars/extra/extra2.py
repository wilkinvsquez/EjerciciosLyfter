from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    def get_role(self):
        return "admin"

    def has_permission(self, permission)-> bool:
        return True

class RegularUser(User):
    ALLOWED_PERMISES = {"read"}

    def get_role(self):
        return "regular"

    def has_permission(self, permission) -> bool:
        if permission in self.ALLOWED_PERMISES:
            return True
        return False


user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permission("delete"))  # True
print(user2.has_permission("delete"))  # False
print(user2.has_permission("read"))    # True
print(user1.get_role())                # admin
print(user2.get_role())                # regular