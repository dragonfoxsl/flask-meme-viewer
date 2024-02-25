from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

meme_api_url = "https://meme-api.com/gimme"

def get_meme():	
	response = json.loads(requests.get(meme_api_url).text)
	meme_large = response["preview"][-2]
	postlink = response["postLink"]
	return meme_large, postlink

def get_meme_detailed():
	response = json.loads(requests.get(meme_api_url).text)
	return response

@app.route("/")
def index():
    meme_pic, postlink = get_meme()
    return render_template("index.html", meme=meme_pic, postlink=postlink)

@app.route("/meme_details")
def meme_page():
     response = get_meme_detailed()
     return render_template("details.html", response=response)

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=80, debug=True)