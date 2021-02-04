import speech_recognition as sr
from pathlib import Path
from uuid import uuid4
from pydub import AudioSegment
import numpy as np
import os
from django.conf import settings



CURRENT_PATH = Path(settings.MEDIA_ROOT)

# Sound convertor

def convert_mp3_wav(src):
    print((CURRENT_PATH / src).resolve())
    sound = AudioSegment.from_mp3((CURRENT_PATH / src).resolve())

    dest = (CURRENT_PATH / (str(uuid4())+'.wav')).resolve()
    sound.export(dest, format="wav")
    return dest

def remove_dest(dest):
    os.remove(dest)

def mp3_to_str(src):
    AUDIO_FILE = convert_mp3_wav(src)

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
        res = r.recognize_google(audio, language="ru-RU")
        print(res)
    remove_dest(AUDIO_FILE)

# Image convertor

import pytesseract
import cv2
import platform


if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def image_to_str(src):
    src = str((CURRENT_PATH / str(src)).resolve())
    img = cv2.imread(src)
    img = np.array(img, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    config = r"--oem 3 --psm 6"

    data = pytesseract.image_to_data(img, config=config)
    text = ""
    for i, el in enumerate(data.splitlines()):
        if i == 0:
            continue

        el = el.split()

        try:
            # x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
            # cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
            # cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1)
            text+=el[11]+" "
        except IndexError:
            text+="\n"
    # print(pytesseract.image_to_string(img, config=config))
    # cv2.imwrite("Result.png", img)
    return text
