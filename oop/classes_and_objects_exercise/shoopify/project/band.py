from project.album import Album, Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for alb in self.albums:
            if alb.name == album_name:
                if alb.published:
                    return "Album has been published. It cannot be removed."

                self.albums.remove(alb)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."
    def details(self):
        return "\n".join([f"Band {self.name}", ''.join([x.details() for x in self.albums])])
