# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-03
# --------------------------------------------------------------------------- #


def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist_name': artist_name, 'album_title': album_title}

    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

while True:
    print('\nPlease, tell me your name.')
    print('(enter \'q\' at any time to quit)')

    artist_name = input('\nEnter Artist Name: ')
    if artist_name == 'q':
        break

    album_title = input('Enter Album Title: ')
    if album_title == 'q':
        break

    number_of_songs = input('Enter number of Songs: ')
    if number_of_songs == 'q':
        break 

    album = make_album(artist_name, album_title, number_of_songs)
    print(album)

