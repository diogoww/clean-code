def introduction_page() -> str:
    message = '''
        Sistema Musical
    * cadastrar musica - 1
    * criar playlist - 2
    * sair - 5
    '''

    print(message)
    command = input("Comando: ")

    return command