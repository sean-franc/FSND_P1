import even_fresher_tomatoes
import media


# Six of my favorite movies. As of 01-2016. -SF
pacific_rim = media.Movie("Pacific Rim",
                          "Mechs vs. Kaiju.",
                          "http://clients.w4tr.com/udacity/pacific_rim_poster.jpg",
                          "https://www.youtube.com/watch?v=5guMumPFBag",
                          1)

star_wars = media.Movie("Star Wars",
                        "Everything old is new again.",
                        "http://clients.w4tr.com/udacity/star_wars_poster.jpg",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE",
                        2)

tank_girl = media.Movie("Tank Girl",
                        "Mutant Kangaroos. Badassery. Tank Girl!",
                        "http://clients.w4tr.com/udacity/tank_girl_poster.jpg",
                        "https://www.youtube.com/watch?v=Y3iEgKjh3Nk",
                        4)

lego_movie = media.Movie("The Lego Movie",
                         "Everything is awesome!",
                         "http://clients.w4tr.com/udacity/lego_movie_poster.jpg",
                         "https://www.youtube.com/watch?v=fZ_JOBCLF-I",
                         3)

high_tension = media.Movie("High Tension",
                           "Don't piss off French girls.",
                           "http://clients.w4tr.com/udacity/high_tension_poster.jpg",
                           "https://www.youtube.com/watch?v=XNagUvDPsrI",
                           6)

enter_the_void = media.Movie("Enter the Void",
                             "Don't do drugs.",
                             "http://clients.w4tr.com/udacity/enter_the_void_poster.jpg",
                             "https://www.youtube.com/watch?v=bKRxDP--e-Y",
                             5)

movies = [pacific_rim,
          star_wars,
          tank_girl,
          lego_movie,
          high_tension,
          enter_the_void]

# Sorting list by rank to display movies in order of my most favorite
ranked_movies = sorted(movies, key=lambda movie: movie.my_rating)

# Build the webpage with my favorite movies!
even_fresher_tomatoes.open_movies_page(ranked_movies)
