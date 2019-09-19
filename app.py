
from flask import Flask, render_template, request
import requests 


lmt = 10
api_key = "FLT5NN3BW81L"

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test_html')
def test_html():
    search_bar_input = request.args.get('search')
    query_string = "https://api.tenor.com/v1/search?q={}&key={}&limit={}".format(search_bar_input, api_key, lmt)

    r = requests.get(query_string)
    gifs = []
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        r_json = r.json()
        result_json = r_json["results"]
        for result in result_json:
            gif_path = result["media"][0]["mediumgif"]["url"]
            gifs.append(gif_path)
        print(gifs)
    else:
        r_json = None
    return render_template("gifs.html", gifs=gifs)

@app.route('/random')
def test_random():
    query_string = "https://api.tenor.com/v1/search?q=random&key={}&limit={}".format(api_key, lmt)

    r = requests.get(query_string)
    gifs = []
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        r_json = r.json()
        result_json = r_json["results"]
        for result in result_json:
            gif_path = result["media"][0]["mediumgif"]["url"]
            gifs.append(gif_path)
        print(gifs)
    else:
        r_json = None
    return render_template("random.html", gifs=gifs)

if __name__ == '__main__':
    app.run(debug=True) 