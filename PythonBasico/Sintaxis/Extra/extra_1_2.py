time_in_seconds = int(input("Escriba el tiempo en segundos: "))
reference_time = 10*60  # 10 minutes in seconds
rem_time = 0
if time_in_seconds < reference_time:
    rem_time = reference_time - time_in_seconds
    print(rem_time)
elif time_in_seconds == reference_time:
    print("Igual")
else:
    print("Mayor")