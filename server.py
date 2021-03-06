from flask import Flask, json
from StatusManager import StatusManager
from sensors.State import State
from sensors.SW420 import SW420
from sensors.MockSensor import MockSensor

app = Flask(__name__)
# Using GPIO pin numbers http://raspi.tv/wp-content/uploads/2014/07/Raspberry-Pi-GPIO-pinouts.png
washer_sensor = SW420(4)
dryer_sensor = SW420(17)
sm_washer = StatusManager(washer_sensor)
sm_dryer = StatusManager(dryer_sensor)
sm_washer.start()
sm_dryer.start()

@app.route('/echo/<received>', methods=['GET'])
def echo(received):
   return received + " ... " + received

@app.route('/status', methods=['GET'])
def get_statuses():
    return {
       "washer": sm_washer.get_state(), 
       "dryer": sm_dryer.get_state()
    }

@app.route('/status/washer', methods=['GET'])
def get_washer():
    return sm_washer.get_state()

@app.route('/status/dryer', methods=['GET'])
def get_dryer():
    return sm_dryer.get_state()

@app.route('/')
def serve_static():
    return app.send_static_file('index.html')

if __name__ == '__main__':
   app.run(debug=False, host="0.0.0.0")
