from flask import Flask, json
from StatusManager import StatusManager
from State import State

app = Flask(__name__)
# Only have one sensor hooked up right now
sm_washer = StatusManager(4)
sm_dryer = StatusManager(17)
#sm_dryer = sm_washer
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

@app.route('/status/<machine>', methods=['GET'])
def get_status(machine):
    return 'No idea about status of the %s, this is just a method stub' % machine

@app.route('/')
def serve_static():
    return app.send_static_file('index.html')

if __name__ == '__main__':
   app.run(debug=False, host="0.0.0.0")
