import json
from song import Song

class Playlist:

    _id_count = 0

    def __init__(self, name, description, songs = [], id = None):
        self.id = id or Playlist._id_count + 1
        Playlist._id_count = self.id
        self.name = name
        self.description = description
        self.songs = [Song(**song_data) for song_data in songs] if songs else []
    
    def details(self):
        return [self.id, self.name, self.description, f"{len(self.songs)} songs"]

    def to_json(self):
        return {"id": self.id, "name": self.name, "description":self.description, "songs":self.songs}

    def update(self,name, description):
        if name == "":
            self.name = name
        
        if description =="":
            self.description = description

        

