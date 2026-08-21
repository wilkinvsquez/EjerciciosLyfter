import menu

def main():
    while True:
        user_selection = menu.start()
        if user_selection == 9:
            print("Gracias por su visita, Vuelva pronto!!")
            break



if __name__ == '__main__':
    main()