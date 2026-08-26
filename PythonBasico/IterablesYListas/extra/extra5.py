user_list = []
new_list = []

while len(user_list) < 5 :
    user_word = input(f"Digite su palabra numero {len(user_list) + 1}: ")
    user_list.append(user_word)

for word in user_list:
    if len(word) > 4:
        new_list.append(word)

print(new_list)