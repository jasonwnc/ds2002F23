
# A very simple Flask Hello World app for you to get started with...

from datetime import datetime
from flask import Flask
import pytz

app = Flask(__name__)

@app.route('/api/v1/timeofday/',methods=['GET'])
def timeofday():

     newYorkTz = pytz.timezone("America/New_York")
     current_dateTime = datetime.now(newYorkTz)
     currentTimeStr = current_dateTime.strftime("%H:%M:%S")
     return (currentTimeStr)


@app.route('/')
def hello_world():
    return "Hello from Flask! I'm Alive"
