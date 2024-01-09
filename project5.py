import googletrans
import speech_recognition
import gtts
import playsound
input_lan = input("From language =")
output_lan = input("To language = ")

recog = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice = recog.listen(source)
    text = recog.recognize_google(voice,language=(input_lan))
    print(text)

translator = googletrans.Translator()
translation = translator.translate(text,dest=(output_lan))
print(translation.text)
converted_audio = gtts.gTTS(translation.text, lang=(output_lan))
converted_audio.save("voice.mp3")
playsound.playsound("voice.mp3")

