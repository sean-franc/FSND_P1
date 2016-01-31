import webbrowser
import os
import re


'''I heavily modified fresh_tomatoes.py to suit my needs:

- Replaced Bootstrap with Foundation, because I think it's nicer.
- I added a summary and a movie rating in addition to the required data.
- Hamburger menu reveals off-canvas area that displays info about me.
- Separated scripts into their own section of the HTML template.
'''


# Page header and styles
main_page_head = '''\
<!doctype html>
<html class="no-js" lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>SF's Favorite Movies</title>
<link rel="stylesheet" href="http://dhbhdrzi4tiry.cloudfront.net/cdn/sites/foundation.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundicons/3.0.0/foundation-icons.css">
<style>
    body {background-color: #3b3b3b;}
    .flex-video {margin: 0 auto;}
    .reveal{background-color: #3b3b3b}
    .off-canvas-content{background-color: #3b3b3b; color: #dddddd;}
    .lead {color: #999999}
    .callout.primary{background-color: #232323; color: #dddddd;}
    .movie-tile {margin-bottom: 1rem; cursor: pointer;}
    .movie-tile img.thumbnail {margin-bottom: 0.5rem;border-color: #232323;}
    .badge {font-size: inherit; color:#dddddd;}
    .badge.rating{background-color: #232323}
    .badge sup {color: #999999;}
</style>
</head>
'''


# General layout and off-canvas area. Personalized with a bit about me.
main_page_content = '''\
<body>
<!-- trailer -->
<div class="reveal" id="trailer" data-reveal>
    <div class="flex-video widescreen" id="trailer-video-container"></div>
    <button class="close-button" data-close aria-label="Close modal" type="button">
        <span aria-hidden="true">&times;</span>
    </button>
</div>
<!-- end trailer -->

<div class="off-canvas-wrapper">
    <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>
        <div class="off-canvas position-left" id="my-info" data-off-canvas data-position="left">
            <div class="row column">
                <br>
                <img class="thumbnail" src="http://clients.w4tr.com/udacity/sf.jpg" />
                <h5>Sean-Franc Strang</h5>
                <p>Aesthetic problem solver, also known as an art gallerist. Technical 
                problem solver, also known as a solutions architect.</p>
            </div>
        </div>
        <div class="off-canvas-content" data-off-canvas-content>
            <div class="title-bar">
                <div class="title-bar-left">
                    <button class="menu-icon" type="button" data-open="my-info"></button>
                    <span class="title-bar-title">Sean-Franc</span>
                </div>
            </div>
            <div class="callout primary">
                <div class="row column">
                    <h1>SF's Favorite Movies</h1>
                    <p class="lead">Udacity Full Stack Web Developer Nanodegree - Project 1</p>
                </div>
            </div>
            <div class="row small-up-2 medium-up-3 large-up-4">
                {movie_tiles}
            </div>
        </div>
    </div>
</div>
'''


# Scripts and end of html template.
# Modified to work with Foundation. Removed tile animation, it bored me.
# Left console.log lines in order to show my work
main_page_scripts ='''
<script src="https://code.jquery.com/jquery-2.1.4.min.js"></script>
<script src="http://dhbhdrzi4tiry.cloudfront.net/cdn/sites/foundation.js"></script>
<script>
    $(document).foundation();
    $('.movie-tile').on('click', function() {
        console.log('loading video');
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
        var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
          'id': 'trailer-video',
          'type': 'text-html',
          'src': sourceUrl,
          'frameborder': 0
        }));
    });
    $('#trailer').on('closed.zf.reveal', function() {
        console.log('killing video');
        $("#trailer-video-container").empty();
    });
</script>
</body>
</html>
'''


# A single movie tile template.
# Blurb appears when you hover over a tile.
# Badge displays rating.
movie_tile_content = '''\
<div data-tooltip aria-haspopup="true" data-disable-hover='false' tabindex=1 title="{blurb}" class="column movie-tile" data-open="trailer" data-trailer-youtube-id="{trailer_youtube_id}">
    <img class="thumbnail" src="{poster_art}">
    <h5>
        <span class="badge rating">
            <sup>#</sup>{my_rating} 
        </span>
        {movie_title}
    </h5>
</div>
'''

# Modified this portion to add additional content
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_art=movie.poster_art,
            trailer_youtube_id=trailer_youtube_id,
            my_rating=str(movie.my_rating),
            blurb=movie.blurb
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('my_favorite_movies.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content + main_page_scripts)
    output_file.close()

    # Open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
