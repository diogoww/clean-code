from src.view.first_view import introduction_page
from .constructor.song_register_contructor import song_register_process
from .constructor.playlist_creator_constructor import playlist_creator_process


def start() -> None:
    while True:

        command = introduction_page()
        if command == '1': song_register_process()
        elif command == '2': playlist_creator_process()
        elif command == '5': exit()
        else: print("\n comando não encontrado, tente novamente! \n\n")