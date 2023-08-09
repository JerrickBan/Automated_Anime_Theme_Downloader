from flask import Flask, render_template, request
from pytube import YouTube
from youtubesearchpython import VideosSearch
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def anime_home():
    if request.method == "POST":

        searchstring = ""

        anime_name = request.form.get("name")
        searchstring += str(anime_name.lower())

        op_or_ed = request.form.get("op_or_ed")
        number = request.form.get("number")
        if op_or_ed == "opening":
            searchstring += f" op{str(number)}"
        else:
            searchstring += f" ed{str(number)}"
        
        # path = request.form.get("path")
        path = "/Users/jerrickban/Desktop/Test"

        print(searchstring)
        link = get_yt_url_from_keywords(searchstring)
        download_link(link, path)
        print(anime_name)
        print(op_or_ed)
        print(number)
        print(path)


    
    return render_template("index.html")


def get_new_op_num():
    file = open("op_number.txt", "r")
    num = int(file.read())
    new_num = num + 1
    file.write(str(new_num))
    return new_num



def get_yt_url_from_keywords(keywords):
    video = VideosSearch(keywords, limit=1)
    link = video.result()["result"][0]["link"]
    print(link)
    return link
    


def download_link(link, path):
    yt = YouTube(link, 
                    use_oauth=False,
                    allow_oauth_cache=True)

    yd = yt.streams.get_highest_resolution()

    yd.download(path)


