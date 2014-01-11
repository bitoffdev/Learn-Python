class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

twinkle = Song(["Twinkle, twinkle, little star", 
		"How I wonder what you are.",
		"Up above the world so high,",
		"Like a diamond in the sky.",])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

twinkle.sing_me_a_song()
