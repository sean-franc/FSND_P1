class Movie():
    """This class stores Movie data"""

    
    # Added a rating.
    def __init__(self, title, blurb, poster_art, trailer, my_rating):
        self.title = title
        self.blurb = blurb
        self.poster_art = poster_art
        self.trailer = trailer
        self.my_rating = my_rating
