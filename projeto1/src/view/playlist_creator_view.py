import os

class PlaylistCreatorView:
    def playlist_creator_success(self, controller_response: dict) -> None:
        self.__clear()
        print("Playlist Criada com Sucesso! \n")

        for music in controller_response["playlist"]:
            message = '''
                Titulo da Musica: {}
                Artista: {}
                Ano de Publicacao: {}

            '''.format(
                music.title,
                music.artist,
                music.year
            )
            print(message)
    
    def playlist_creator_fail(self, controller_response) -> None:
        self.__clear()

        message = '''
            Erro na criacao da playlist:
            * Erro: {}

        '''.format(
            controller_response["error"]
        )
        print(message)

    def __clear(self):
        os.system("cls||clear")