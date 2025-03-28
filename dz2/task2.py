class Film:
    def __init__ (self, regiccer, name, genre, duration: int, actor):
        self.name = name
        self.genre = genre
        self.duration = duration
        self.regiccer = regiccer
        self.actor = actor
    
    def play(self):
        return "меняются кадры"
    
film_ono = Film('Ono', 'horror', 80, 'Elon_Mask', 'chushka')
print(film_Ono.play(),   film_Ono.name)
    