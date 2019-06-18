import urllib

class Movies():
    VALID_RATINGS = {'P','PG','O'}

    def __init__(self,title,description,genre,poster,trailer):
        self.title=title
        self.description=description
        self.genre=genre
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer

    #def show_trailer():
        
