class Song(object):
    def __init__(song, lyrics):
        song.lyrics = lyrics
    
    def sing_me_a_song(song):
        for line in song.lyrics:
            print(line)

    def sing_forever(song):
        while True:
            Song.sing_me_a_song(song)

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued", 
"So Ill stop right there"])

hehe = Song(['hehe hehe hehe', "aeae aeae aeae", "hi"])

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()