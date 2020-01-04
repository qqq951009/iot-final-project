
from flask import Flask, render_template, Response
from camera import VideoCamera
import RPi.GPIO as GPIO
import time
app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/turnleft')
def turn_left():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    pwm=GPIO.PWM(11,50)
    pwm.start(0)
    duty = 135/18+2
    GPIO.output(11,True)
    pwm.ChangeDutyCycle(duty) 
    time.sleep(1) 
    GPIO.output(11, False) 
    pwm.ChangeDutyCycle(0) 
    pwm.stop() 
    GPIO.cleanup() 
    print('left') 
    return render_template('index.html')

    
@app.route('/center')
def turn_center():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    pwm=GPIO.PWM(11,50)
    pwm.start(0)
    duty = 90/18+2
    GPIO.output(11,True)
    pwm.ChangeDutyCycle(duty) 
    time.sleep(1) 
    GPIO.output(11, False) 
    pwm.ChangeDutyCycle(0) 
    pwm.stop() 
    GPIO.cleanup() 
    print('center') 
    return render_template('index.html')

@app.route('/turnright')
def turn_right():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    pwm=GPIO.PWM(11,50)
    pwm.start(0)
    duty = 45/18+2
    GPIO.output(11,True)
    pwm.ChangeDutyCycle(duty) 
    time.sleep(1) 
    GPIO.output(11, False) 
    pwm.ChangeDutyCycle(0) 
    pwm.stop() 
    GPIO.cleanup() 
    print('right') 
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)

