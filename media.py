import webbrowser

class Movie():
	#initiate the instance that was passed in from entertainment_center file.
    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #instance method that shows the trailer
    def show_trailer(self):
        webbrowser.open(self.tralier_youtube_url)