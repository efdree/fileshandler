import json

class Song:

    _id_count = 0

    def __init__(self, title, artists, album, released, id= None):
        self.id = id or Song._id_count + 1
        Song._id_count = self.id
        self.title = title
        self.artists = artists
        self.album = album
        self.released = released

    def details(self):
        return [self.id, self.title, self.artists, self.album, self.released]
    
    def to_json(self):
        return {"id": self.id, "title":self.title, "artists": self.artists, "album":self.album, "released":self.released}

    def update(self,title, artists, album, released):
        if title == "":
            self.title = title 
        
        if artists =="":
            self.artists = artists

        if album == "":
            self.album = album

        if released == "":
            self.released = int(released)