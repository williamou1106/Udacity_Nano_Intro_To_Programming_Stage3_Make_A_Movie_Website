#import the files in the same folder to use their functions
import media
import fresh_tomatoes

#Create instances using the class "movie" in the file "media"
#Pass in the name of movie, synopsis, movie image, and youtube url
#and assign to their respective instances.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                     "A marine on an alient planet",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


inception = media.Movie("Inception",
                        "A man able to steal information from people's subconsicious by entering their dream",
                        "https://www.movieposter.com/posters/archive/main/101/MPW-50904",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

fight_club = media.Movie("Fight Club",
                         "The first of fight club is you do not talk about fight club",
                         "http://www.impawards.com/1999/posters/fight_club_ver4.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

taken = media.Movie("Taken",
                    "A former CIA agent tries to rescuse his daughter who was taken",
                    "http://www.impawards.com/2012/posters/taken_two_ver2_xlg.jpg",
                    "https://www.youtube.com/watch?v=uPJVJBm9TPA")

step_brothers = media.Movie("Step Brothers",
                            "Two step brothers messing around",
                            "http://www.impawards.com/2008/posters/step_brothers.jpg",
                            "https://www.youtube.com/watch?v=CewglxElBK0")

#Create list to store all the instances from above
movies = [toy_story, avatar, inception, fight_club, taken, step_brothers]
#initialize the webpage by passing in the list
fresh_tomatoes.open_movies_page(movies)
