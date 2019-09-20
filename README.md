# Gif Search Instructions:
    1. Click on search bar
    2. Type a noun, phrase, or adjective
    3. Click on the search buttton (or press enter)
    4. View gifs based on search

# files:
    /Gif-Search-Engine
        /static
            style.css (styles the html files)
        /templates
            base.html (loads the initial page )
            gif.html (sets template to pull gif images and displayed)
            gifs.html (runs the html file once user puts enters a search)
            index.html (extends base.html)
            random.html (html route for random gifs )

 
# app.py:
    1. Contains routes
    2. Pulls data from tenor api
    3. Displays gif images
# second.py:
    1. Allows us to make our site scalable and run efficiently



app.py explained:
    contains 2 routes
    the 1st route redirects the user to gif search
    2nd route sends you to random gifs
    gifs are loaded from tenor.com using their api and api key


# Resources

You may find the following resources helpful in your development process:

1. [Tenor API Documentation](https://tenor.com/gifapi/documentation) - useful for understanding which URL we want to visit in order to make an API request for GIFs
1. [BEW 1.1 Lesson on Flask](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/#/./Lessons/03-Intro-to-Flask/README)
1. [BEW 1.1 Lesson on Templates](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/#/./Lessons/04-Flask-Templating/README)
1. [BEW 1.1 Lesson on APIs](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/#/./Lessons/05-URLs-HTTP-REST-and-Reading-Errors/README)
