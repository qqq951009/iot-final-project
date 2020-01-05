import requests
import time
import speech_recognition as sr
import threading
 
def lineNotify_pic(token, msg, picurl):

    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token, 
        #"Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message': msg}
    files = {'imageFile': open(picurl, 'rb')}
    r = requests.post(url, headers = headers, params = payload, files = files)
    return r.status_code 

def lineNotify(token, msg):

    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token, 
        #"Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message': msg}
    #files = {'imageFile': open(picurl, 'rb')}
    r = requests.post(url, headers = headers, params = payload)
    return r.status_code



def loop1():
    for i in data:
        if close == 1: 
            print('gps偵測中')
            lineNotify(token,'gps偵測中') 
            latitude = i['lat'] 
            longetude = i['long'] 
            if(x != latitude or y != longetude):
                lineNotify(token,'your car wsa stolen') 
                print('latitude:'+latitude+',1ongetude:'+longetude) 
                message1 = 'http://maps.google.com/?q='+latitude+','+longetude
                message2 = 'ip address'
                lineNotify(token,message1)
                lineNotify(token,message2)
                lineNotify_pic(token,'bitch',picurl)
            else:
                lineNotify(token,'bicycle save') 
                
        else:
            lineNotify(token,'gps close')
            break
        time.sleep(8)
    time.sleep(1)

def loop2():
    global close
    close = 1
    #obtain audio from the microphone
    r=sr.Recognizer()
    while True:
        with sr.Microphone() as source:

            print("Please wait. Calibrating microphone...") 
            #listen for 5 seconds and create the ambient noise energy level 
            r.adjust_for_ambient_noise(source, duration=5) 
            lineNotify(token,'you can say close to off the gps now ') 
            print("Say something!") 
            audio=r.listen(source) 

        try: 
            print("Google Speech Recognition thinks you said:") 
            result = r.recognize_google(audio, language="en-US") 
            print(result) 
            if result == 'close':
                close = 0
                
                print(close)
                lineNotify(token,'loop2 close')
                break
            else:
                lineNotify(token,'sorry try again')

        except sr.UnknownValueError:
            #lineNotify(token,'can not understand audio please speak again') 
            print("Google Speech Recognition could not understand audio") 
        except sr.RequestError as e: 
            print("No response from Google Speech Recognition service: (0)".format(e))
        time.sleep(2)
        
        


result = " "
picurl="your_path"
data = [
    {
        'lat':'24.967994',
        'long':'121.192498'
    },
    {
        'lat':'24.967994',
        'long':'121.192498'
    },
    {
        'lat':'24.967994',
        'long':'121.192498'
    },
    {
        'lat':'24.967994',
        'long':'121.192498'
    },
    {
        'lat':'24.967994',
        'long':'121.192498'
    },
    {
        'lat':'24.967994',
        'long':'121.192498'
    },
    {
        'lat':'24.968461',
        'long':'121.191029'
    },
    {
        'lat':'24.968461',
        'long':'121.191029'
    },
    {
        'lat':'24.968461',
        'long':'121.191029'
    },
    {
        'lat':'24.968461',
        'long':'121.191029'
    }
]

x = data[1]['lat']
y = data[1]['long']
token = 'your token'
times = 0
flag = 1
token = "your_token"
#obtain audio from the microphone
r=sr.Recognizer()
while times < 3:
    with sr.Microphone() as source:
        print('first in')
        print("Please wait. Calibrating microphone...") 
        #listen for 5 seconds and create the ambient noise energy level 
        r.adjust_for_ambient_noise(source, duration=5) 
        lineNotify(token,'speak') 
        print("Say something!") 
        audio=r.listen(source) 

    try: 
        print("Google Speech Recognition thinks you said:") 
        result = r.recognize_google(audio, language="en-US") 
        print(result) 
        if result == 'open':
            lineNotify(token,'gps on')
            flag = 1
            thread2 = threading.Thread(target=loop2)
            thread2.start()
            loop1()
            
            
        else:
            times += 1
            lineNotify(token,'wrong password'+str(result)+'try again')
            print('failed')

    except sr.UnknownValueError:
        lineNotify(token,'can not understand audio please speak again') 
        print("Google Speech Recognition could not understand audio") 
    except sr.RequestError as e: 
        print("No response from Google Speech Recognition service: (0)".format(e)) 













