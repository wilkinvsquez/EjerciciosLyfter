name=input("Please enter your name: ")
last_name=input("Please enter your last name: ")
age=int(input("Please enter your age: "))

print(f"\nHello {name} {last_name}, you are {age} years old.")

match age:
    case age if age <= 2:
        print("You are a baby.")
    case age if age >= 3 and age <= 10:
        print("You are a child.")
    case age if age >= 11 and age <= 12:
        print("You are a pre-teen.")
    case age if age >= 13 and age <= 17:
        print("You are a teenager.")
    case age if age >= 18 and age <= 39:
        print("You are a young adult.")
    case age if age >= 40 and age <= 64:
        print("You are an adult.")
    case _:
        print("You are a senior citizen.")

#if age <= 2:
#    print("You are a baby.")

#elif age >= 3 and age <= 10:
#    print("You are a child.")

#elif age >= 11 and age <= 12:
#    print("You are a pre-teen.")

#elif age >= 13 and age <= 17:
#    print("You are a teenager.")

#elif age >= 18 and age <= 39:
#    print("You are a young adult.")

#elif age >= 40 and age <= 64:
#    print("You are an adult.")

#else:
#    print("You are a senior citizen.")