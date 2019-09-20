
from flask import Flask, render_template, request
import requests 


lmt = 10                    #sets the correct amount of gif images which is 10
api_key = "FLT5NN3BW81L"    #api key allows us to access the api

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")    # Displays the index.htmt

@app.route('/test_html')
def test_html():
    ''' This function takes the user to a seperate page that loads exactly 10 gifs on a page.
        The gifs will be choosen based on what the user inputs. The gifs will be loaded from the tenor
        website using it's api. Once the user presses enter 
    '''
    search_bar_input = request.args.get('search')
    query_string = "https://api.tenor.com/v1/search?q={}&key={}&limit={}".format(search_bar_input, api_key, lmt)

    r = requests.get(query_string)
    gifs = []
    if r.status_code == 200:            # the clients request has succeeded
        r_json = r.json()
        result_json = r_json["results"]
        for result in result_json:              #this loops through the search results, puts it into a list and prints gifs
            gif_path = result["media"][0]["mediumgif"]["url"]
            gifs.append(gif_path)
        print(gifs)
    else:
        r_json = None
    return render_template("gifs.html", gifs=gifs)

@app.route('/random')
def test_random():
    ''' This route displays a random gif when the user clicks the random button
        load the random gifs using the urls for the smaller GIF sizes '''

    query_string = "https://api.tenor.com/v1/search?q=random&key={}&limit={}".format(api_key, lmt)

    r = requests.get(query_string)
    gifs = []
    if r.status_code == 200:                    # the clients request has succeeded
        
        r_json = r.json()                       #json objects contains the gif results
        result_json = r_json["results"]
        for result in result_json:                  # this loop 
            gif_path = result["media"][0]["mediumgif"]["url"]
            gifs.append(gif_path)
        print(gifs)
    else:
        r_json = None
    return render_template("random.html", gifs=gifs)

if __name__ == '__main__':
    app.run(debug=True) 