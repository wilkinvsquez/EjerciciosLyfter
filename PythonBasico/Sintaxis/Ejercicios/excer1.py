print("--------- Sumas entre distintos tipos de datos ---------")

print("\n--- String + String ---")
print("Hello" + " World")
print("Result: " + str(type("Hello" + " World")))

print("\n--- String + Int ---")
#print("Hello" + 5)  # This will raise a TypeError
print("Result: TypeError: can only concatenate str (not 'int') to str")

print("\n--- Int + string ---")
#print(5 + "Hello")  # This will raise a TypeError
print("Result: TypeError: can only concatenate int (not 'str') to int")

print("\n--- list + list ---")
print([1, 2, 3] + [4, 5, 6])
print("Result: " + str(type([1, 2, 3] + [4, 5, 6])))

print("\n--- list + string ---")
#print([1, 2, 3] + "Hello")  # This will raise a TypeError
print("Result: TypeError: can only concatenate list (not 'str') to list")

print("\n--- float + int ---")
print(3.14 + 5)
print("Result: " + str(type(3.14 + 5)))

print("\n--- bool + bool ---")
print(False + False)
print("Result: " + str(type(False + False)))

print("\n--- tuple + tuple ---")
print((1, 2, 3) + (4, 5, 6))
print("Result: " + str(type((1, 2, 3) + (4, 5, 6))))

print("\n--- tuple + list ---")
#print((1, 2, 3) + [4, 5, 6])  # This will raise a TypeError
print("Result: TypeError: can only concatenate tuple (not 'list') to tuple")

print("\n--- dict + dict ---")
#print({"a": 1} + {"b": 2})  # This will raise a TypeError  
print("Result: TypeError: unsupported operand type(s) for +: 'dict' and 'dict'")

