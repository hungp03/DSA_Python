class Dictionary:
    def __init__(self) -> None:
        self.dictionary = {}
    
    def get_hash(self, album):
        return album[0]
    
    def add_album(self, album, list_song):
        key = self.get_hash(album)
        if key not in self.dictionary:
            self.dictionary[key] = {}
        self.dictionary[key][album] = list_song
    
    def show_album(self, album):
        key = self.get_hash(album)
        if key in self.dictionary and album in self.dictionary[key]:
            return self.dictionary[key][album]
        else:
            return "Album này không có trong từ điển."
        
list_album = Dictionary()
list_album.add_album('Album 1', [{'song_name': 'Bài1', 'musician': 'Nhạc sĩ 1', 'singer': 'Ca sĩ 1'}, {'song_name': 'Bài2', 'musician': 'Nhạc sĩ 2', 'singer': 'Ca sĩ 2'}])
print(list_album.show_album('Album 1'))  
print(list_album.show_album('Album không tồn tại'))
