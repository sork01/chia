import os
import sys
import time

from classes import Chia
from flask import Flask, render_template, request


app = Flask(__name__)
chia = Chia.Chia()


@app.route("/", methods=['GET'])
def getAnime():
    return render_template('anime.html.j2', anime=chia.mainLinks)

@app.route('/show')
def getShow():
    show = request.args.get('show')
    print("här är show " + show)
    return render_template('show.html.j2', show=chia.getEpisodes(show))

@app.route('/episode')
def getLink():
    link = request.args.get('episode')
    return render_template('link.html.j2', link=chia.getLink(link))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
