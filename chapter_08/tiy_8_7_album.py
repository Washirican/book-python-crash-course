# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-03
# --------------------------------------------------------------------------- #

def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist_name': artist_name, 'album_title': album_title}

    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

album_0 = make_album('gordi', 'reservoir')
album_1 = make_album('julien baker', 'turn out the lights', 11)
album_2 = make_album('metallica', 'ride the lighting')

print(album_0)
print(album_1)
print(album_2)