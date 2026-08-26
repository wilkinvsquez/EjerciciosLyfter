def create_or_update_file(file_name, new_text):
    with open(file_name, 'a') as file:
        file.write(new_text)

def user_request():
    text = input("Inserte el nuevo texto para agregar al archivo: ")
    return text

def main():
    new_text = user_request()
    create_or_update_file("./text4.txt", new_text)

main()