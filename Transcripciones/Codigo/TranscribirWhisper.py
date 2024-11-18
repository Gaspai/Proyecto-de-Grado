import pywhisper
import os
from deepmultilingualpunctuation import PunctuationModel

from datetime import timedelta
audio= input("Ingrese audio para transcribir: ")
model = pywhisper.load_model("base")
result_transcribe = model.transcribe(audio,fp16=False)
    
AllWords = []

row = result_transcribe["text"].split(' ')
AllWords+=list(row)

line_breaker=20
i=1
#transcripcion
with open(os.path.join(audio + ".txt"),"w",encoding="utf-8") as file:
    for word in AllWords:
        if( i==line_breaker):
            file.write(word.strip('\n')+"\n")
            i=0
        else:
            file.write(word.strip('\n')+" ")
        i+=1
    
#Restauracion de oraciones y puntuacion
with open(os.path.join(audio + ".txt"),encoding="utf-8") as f:
    text = ''.join(f.readlines())
    f.close()


model = PunctuationModel(model = "kredor/punctuate-all")
result_punctuation = model.restore_punctuation(text)

with open('resultadoPuntuacion.txt', 'w',encoding="utf-8") as f:
    f.write(result_punctuation)

#segmentos con marcas de tiempo
segments = result_transcribe["segments"]
for segment in segments:
    startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
    endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
    text = segment['text']
    segmentId = segment['id']+1
    segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"
    with open(os.path.join(audio + ".srt"),"a",encoding="utf-8") as srtFile:
        srtFile.write(segment)

#CANAL_5_NOTICIAS_CENTRAL_20210730_215000\Parte1\CANAL_5_NOTICIAS_CENTRAL_20210730_215000Parte1.wav    
    
#pywhisper CANAL_5_NOTICIAS_CENTRAL_20210803_215000\CANAL_5_NOTICIAS_CENTRAL_20210803_215000Parte3.mp4  --language spanish