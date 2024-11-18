import speech_recognition as sr
import math
import os
from os import path 
from os import remove
from pydub import AudioSegment

def transcribirAudio(audio):
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)),audio)
    r = sr.Recognizer()
    texto=""
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
    
    try:
        texto=r.recognize_google(audio ,language='es-UY')
        #print("Google Speech Recognition thinks you said " + )
       
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
    return texto    

video= input("Ingrese video para transcribir: ")
	
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)),video)


sound = AudioSegment.from_file(AUDIO_FILE)
duracion=len(sound)
cantPartes=math.ceil((duracion/60000))*2
print(cantPartes)
puntodecorte = len(sound) / int(cantPartes)

partesDelAudio=[]
for i in range(1,1+cantPartes):
   inicio=puntodecorte*(i-1)
   final=puntodecorte*(i)
   partesDelAudio.append( sound[inicio:final])

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'audios')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)
   
j=1    
for parte in partesDelAudio:
    parte.export("audios/parte"+str(j)+".wav", format="wav")
    j+=1

for h in range(1,1+cantPartes):
    print("va por parte "+str(h))
    texto=transcribirAudio("audios/parte"+str(h)+".wav")
    remove("audios/parte"+str(h)+".wav")
    with open('ResultadoGoogleSpeechRecognition.txt', 'a')  as f:
        f.write(texto)
        f.close()



