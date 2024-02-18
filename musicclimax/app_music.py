import json
from tabulate import tabulate
from playlist import Playlist
from song import Song
from store import Store

class AppMusic:

    def __init__(self):
        self.store = Store("store.json")
    
    def start(self):
        action = ""
        options = ["create", "show ID", "update ID", "delete ID", "exit"]
        while action not in options:
            AppMusic.print_table(self.store.playlists, title = "Music CLImax", headings=["ID", "List", "Description", "#Songs"] )
            action_selected = AppMusic.menu(options)
            if len(action_selected) == 2:
                action = action_selected[0]
                id = action_selected[1]                  
            else:
                action = action_selected[0]
            if action == "create":
                AppMusic.create_playlist(self)
            elif action == "show":
                AppMusic.show_playlist(self, id)
            elif action == "update":
                AppMusic.update_playlist(self, id)
            elif action == "delete":
                AppMusic.delete_playlist(id)
            elif action == "exit":
                print("Goodbye!")
            else:
                print("Invalid action")
    
    def print_table(list, title, headings):
        table = [headings] + [item.details() for item in list]
        print(tabulate([[title]],tablefmt = "fancy_grid"))
        print(tabulate(table, headers = "firstrow", tablefmt = "grid"))

    def menu(options):
        print(" | ".join(options))
        action_input = input("> ")
        action_split = action_input.split(" ")
        if len(action_split) == 2:
            action, id = action_split
            return [action, int(id)]
        else:
            return action_split
    
    def playlist_form():
        name = input("Name: ")
        description = input("Description: ")
        return {"name": name, "description": description}

    def song_form():
        title = input("Title: ")
        artists = input("Artists: ").split(", ")
        artists = [artist.strip() for artist in artists]
        album = input("Album: ")
        released = input("Released: ")
        return {"title": title, "artists": artists, "album": album, "released": released}
    
    def show_playlist(self, id):
        playlist = self.store.find_playlist(id)
        action = ""
        options = ["create", "update ID", "delete ID", "back"]
        while action != "back":
            AppMusic.print_table(playlist.songs, playlist.name, ["ID", "Title", "Artists", "Album", "Released"])
            action_selected = AppMusic.menu(options)
            if len(action_selected) == 2:
                action = action_selected[0]
                id = action_selected[1]                  
            else:
                action = action_selected[0]
            if action == "create":
                AppMusic.create_song(playlist)
            elif action == "update":
                AppMusic.update_song(id, playlist)
            elif action == "delete":
                AppMusic.delete_song(id, playlist)
            elif action == "back":
                continue
            else:
                print("Invalid action")

    def create_song(self, playlist):
        song_data = AppMusic.song_form()
        new_song = Song(**song_data)
        self.store.add_song(new_song, playlist.id)

    def update_song(self, id, playlist):
        song_data = AppMusic.song_form()
        self.update_song(id, song_data, playlist.id)

    def delete_song(self, id, playlist):
        self.store.delete_song(id, playlist.id)

    def create_playlist(self):
        playlist_hash = AppMusic.playlist_form()
        new_playlist = Playlist(**playlist_hash)
        self.store.add_playlist(new_playlist)

    def update_playlist(self, id):
        playlist_hash = AppMusic.playlist_form()
        self.store.update_playlist(id, playlist_hash)
    
    def delete_playlist(self, id):
        self.store.delete_playlist(id)
