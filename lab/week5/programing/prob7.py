# 작성자: 김민재
# 작성일: 2026.10.13

class Artist:
    def __init__(self, name):
        self.name = name
        self.songs = []


class Song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        artist.songs.append(self)


class Album:
    def __init__(self, name, artist, year):
        self.name = name
        self.artist = artist
        self.year = year
        self.tracks = []

    def add_track(self, name):
        song = Song(name, self.artist)
        self.tracks.append(song)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)


lee = Artist("Lee's Band")

album = Album("첫 번째 앨범", lee, 2020)
album.add_track("첫 번째 노래")
album.add_track("두 번째 노래")

playlist = Playlist("애창곡")

for song in album.tracks:
    playlist.add_song(song)

for song in playlist.songs:
    print(song.name)