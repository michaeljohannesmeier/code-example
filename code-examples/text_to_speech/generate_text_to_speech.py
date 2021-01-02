
import requests
import json
import base64


#Generate a virtualenvironment. On your terminal generate a new folder, call it sql_alchemy and cd into it. Then generate a virtual environment with the command python -m virtualenv venv. If you dont have virtualenv installed already, run pip install virtualenv. Activate the virtual environment with source venv/Scripts/activate.



payload = {
    "input":{
      "text": "and how to create an engine object to connect to the database."
    },
    "voice":{
      "languageCode":"en-gb",
      "name":"en-GB-Standard-A",
      "ssmlGender":"FEMALE"
    },
    "audioConfig":{
      "audioEncoding":"MP3"
    }
  }

params = {"key": ""}

res = requests.post("https://texttospeech.googleapis.com/v1/text:synthesize", data=json.dumps(payload), params=params)
if res.ok:
    res_body = res.json()
    audio_content = res_body["audioContent"]
    audio_mp3 = base64.b64decode(bytes(audio_content, 'utf-8'))
    newFileByteArray = bytearray(audio_mp3)
    file = open('1_4.mp3', 'wb')
    file.write(newFileByteArray)
    file.close()
