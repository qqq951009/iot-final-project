# iot-final-project 腳踏車防盜模擬

# Introduce of raspberry pi proposal

你有過腳踏車被偷的經驗嗎，後來有找回來嗎?找回來後知道是誰偷了你的車嗎?這個專案除了讓你可以找回車子並且讓你有機會抓到犯人。
簡單介紹一下專案，這個專案在你的車子停好後利用聲控的方式開啟gps定位，當車子不見之後會持續使用gps追蹤，
並且傳送line訊息給你，讓你可以直接開啟googlemap的連結，知道目前車子的所在位置。
另外車上有鏡頭並連接伺服馬達，透過line傳送的網址可以操控鏡頭監看現在是誰偷了你腳踏車，
此外利用face detection偵測人臉，並拍照儲存回傳Line給使用者。不過因為最後進度壓力沒有辦法把GPS模組裝上。

# Item use

* Raspberry pi 
* Jumper Wires, Male to Female
* SG90 Servo motor
* NEO7M APM2.5 GYGPSV1
* Raspberry pi camera module
* MI-305 usb microphone

# Component setup

### 1. camera connection
參考連結:<https://projects.raspberrypi.org/en/projects/getting-started-with-picamera>
### 2. SG90 servo motor connection
* 線路圖
<https://imgur.com/a/7lMsnSS>
 
1. 控制接腳 (橘色) 可連結至任一可用於輸出的腳位，這裡我們使用實體編號 11 的腳位 (其 BCM 編號為 17)。

2. SG90 的工作電壓為 +4.8V 以上，所以我們必須連結至 Raspberry Pi +5V 的腳位，在此我們將 SG90 電源輸入接腳 (紅色) 連結至實體編號 2 的腳位。

3. 接地接腳 (棕色) 必須接地，所以連結至 Raspberry Pi 的實體編號 6 的腳位。

4. 腳位對應關係整理如下：

| SG90 servo motor 伺服馬達接腳       | Raspberry Pi GPIO 腳位      |
| ------------- |:-------------:| 
| 橘色 (控制訊號)   | 實體編號 11 (BCM 編號 17)      |
| 紅色 (電源輸入)     | 實體編號 2 (+5V)     |
| 棕色 (接地)      | 實體編號 6 (接地)    |

### 3.NEO7M APM2.5 GYGPSV1
詳細設定參考連結<https://medium.com/@DefCon_007/using-a-gps-module-neo-7m-with-raspberry-pi-3-45100bc0bb41>
* 線路圖
<https://imgur.com/a/2U1aGQs>
### 4.MI-305 usb microphone
直接插在usb槽即可

# Raspberry pi environment set up
1.下載 flask 套件</br>
  建立網頁讓影像可以在上面串流和操控servo motor
  ```
  pip3 install flask
  ```
  [Flask詳細教學](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/3)

2.下載麥克風所需套件</br>
  * step1. 首先下載speech recognition套件</br>
  好像只能用pip3下載，pip會一直噴錯</br>
  ```
  pip3 install SpeechRecognition
  ```
  * step2. 下載pyaudio套件
  ```
  pip3 install PyAudio
  ```
  如果出現以下錯誤的話
  ```
  fatal error: portaudio.h: No such file or directory
  ```
  改執行
  ```
  sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
  pip install pyaudio
  ```
  若在python中執行`import speech_recognition` 和`import pyaudio`若沒有報錯就代表下載成功

3.下載opencv套件</br>
  參考此連結[Opencv](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/)
  在python中`import cv2`沒報錯的話就下載成功了
  
4.申請linenotify api</br>
  [Line Notify ](https://notify-bot.line.me/zh_TW/) 申請連結</br>
  申請完後務必記下token值，嘗試執行以下程式碼
  ```
  import requests

  def lineNotify(token, msg):

      url = "https://notify-api.line.me/api/notify"
      headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }

      payload = {'message': msg}
      r = requests.post(url, headers = headers, params = payload)
      return r.status_code
  lineNotify(token,'test')
  ```
  若有成功收到Line訊息即可
# Start Programming
