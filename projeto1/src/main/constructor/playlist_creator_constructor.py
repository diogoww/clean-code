from src.view.playlist_creator_view import PlaylistCreatorView
from src.controllers.playlist_creator_controller import PlaylistCreatorController

def playlist_creator_process():
    playlist_creator_view = PlaylistCreatorView()
    playlist_creator_controller = PlaylistCreatorController()

    response = playlist_creator_controller.create_playlist()
    if response["success"]:
        playlist_creator_view.playlist_creator_success(response)
    else:
        playlist_creator_view.playlist_creator_fail(response)