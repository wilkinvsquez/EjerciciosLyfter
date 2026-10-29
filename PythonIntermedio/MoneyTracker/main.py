import FreeSimpleGUI as sg

def main():
    layout = [[sg.Text("Mirala terminal antes de interactuar")], [sg.Button("Continuar")]]
    window = sg.Window("Demostración de Bloqueo", layout)

    # Iniciamos el Event Loop
    while True:
        # El programa se "detiene" aquí (bloqueo) esperando una acción
        event, values = window.read()
        
        # Si el usuario cierra la ventana, rompemos el ciclo
        if event == sg.WIN_CLOSED:
            break

        # Si ocurre el evento de pulsar "Continuar"
        if event == "Continuar":
            print("Continuar")

    window.close()

if __name__ == "__main__":
    main()