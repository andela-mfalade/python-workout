import webbrowser


class Movie(object):
    def __init__(self, movie_name, story_line, poster_url, trailer_url):
        self.title = movie_name
        self.story_line = story_line
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
