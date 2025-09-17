from src.view.first_view import introduction_page

def start() -> None:
    while True:
        
        command = introduction_page()

        if command == '1': print("inserindo musica")
        elif command == '2': print("criando playlist")
        elif command == '5': exit()
        else: print("\n comando nao encontrado, tente novamente! \n\n")