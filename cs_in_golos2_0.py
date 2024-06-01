import pyaudio
import json
import mouse
import keyboard
import pyautogui
from vosk import Model, KaldiRecognizer

model = Model('small_model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']

ctrl_pressed = False
shift_pressed = False


for text in listen():
    print(text)
    if 'вперёд' in text:
        keyboard.press('w')
    elif 'стоп' in text:
        keyboard.release('w')
        keyboard.release('s')
    elif 'назад' in text:
        keyboard.press('s')
    elif 'стреляй' in text:
        mouse.click('left')
    elif 'прицел' in text:
        mouse.click('right')
    elif 'сядь' in text:
        if ctrl_pressed:
            keyboard.release('ctrl')
            ctrl_pressed = False
        else:
            keyboard.press('ctrl')
            ctrl_pressed = True

    elif 'четыре' in text:
        keyboard.press('4')
    elif 'один' in text:
        keyboard.press('1')
    elif 'два' in text:
        keyboard.press('2')
    elif 'три' in text:
        keyboard.press('3')
    elif 'пачка' in text:
        keyboard.press('5')
    elif 'прыжок' in text:
        keyboard.press('space')
    elif 'медленно' in text:
        if shift_pressed:
            keyboard.release('shift')
            shift_pressed = False
        else:
            keyboard.press('shift')
            shift_pressed = True
    elif 'покупка' in text:
        keyboard.press_and_release('b')
    elif 'закончить' in text:
        keyboard.press_and_release('ctrl + F2')
    elif 'права' in text:
        pyautogui.moveTo(960, 1000, duration=2)
    elif 'право' in text:
        pyautogui.moveTo(0, 5, duration=2)
    elif 'калаш' in text:
        keyboard.press_and_release('b, 4, 2, b')
    elif 'выбросить' in text:
        keyboard.press_and_release('g')