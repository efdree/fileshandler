import json
from playlist import Playlist

class Store:

    def __init__(self, filename):

        self.filename = filename
        self.playlists = Store.load_playlist(self)

    def add_playlist(self, playlist):
        self.playlists.append(playlist)
        Store.save(self)

    def delete_playlist(self, id):
        playlist_found = Store.find_playlist(id)
        self.playlists.delete(playlist_found)
        Store.save()

    def update_playlist(self,id,data):
        print("+"*20, data)
        print("-"*20, id)
        playlist_found = Store.find_playlist(self, id)
        playlist_found.update(**data)
        print("*"*20, playlist_found.description)
        #Store.save(self)

    def find_playlist(self, id):
        return next((playlist for playlist in self.playlists if playlist.id == id), None)
    
    def add_song(self,new_song,id):
        playlist = Store.find_playlist(id)
        playlist["songs"].append(new_song)
        Store.save()

    def update_song(self, id, new_data, playlist_id):
        playlist = Store.find_playlist(playlist_id)
        song = Store.find_song(id, playlist)
        song.update(new_data)
        Store.save()

    def delete_song(self, id, playlist_id):
        playlist = Store.find_playlist(playlist_id)
        playlist["songs"] = [song for song in playlist["song"] if song["id"] != id]
        Store.save()

    def find_song(self, id, playlist):
        found_song = next((song for song in playlist["songs"] if song["id"] == id), None)

    def load_playlist(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            return [Playlist(**playlist_dict) for playlist_dict in data]
    
    def save(self):
        def convert_to_dict(playlist):
            return {
                "id": playlist.id,
                "name": playlist.name,
                "description": playlist.description,
                "songs": [song.__dict__ for song in playlist.songs]
            }
        
        with open(self.filename, 'w') as file:
            playlist_data = [convert_to_dict(playlist) for playlist in self.playlists]
            json.dump(playlist_data, file)