class SongRegisterController:
    def insert(self, new_song_informations: dict) -> dict:
        self.__verify_songs_infos()
        self.__verify_if_song_already_registered()
        self.__insert_song()
        self.__format_response()
        pass

    def __verify_if_song_already_registered(new_song_informations: dict) -> None:
        pass

    def __verify_songs_infos(new_song_informations: dict) -> None:
        pass

    def __insert_song() -> None:
        pass

    def __format_response() -> None:
        pass